import requests
from bs4 import BeautifulSoup
from ics import Calendar, Event
import arrow
import hashlib
import warnings
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single InsecureRequestWarning from urllib3 needed
warnings.simplefilter('ignore', InsecureRequestWarning)

# URL of the page containing the tournament schedule
url = "https://www.coloradochess.com/tournament/scholastic"

# Function to extract event IDs from the HTML content
def extract_event_ids(url):
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    event_ids = []
    
    # Find all <tr> tags where the event ID is contained in the JavaScript function call
    for row in soup.find_all('tr', style=True):
        if 'TournamentController.loadScholastic' in row['onclick']:
            # Extract the event ID using string manipulation
            event_id = row['onclick'].split('(')[1].split(')')[0]
            event_ids.append(event_id)
    
    print(f"Extracted Event IDs: {event_ids}")
    return event_ids

# Function to fetch event details
def fetch_event_details(event_id):
    api_url = f"https://www.coloradochess.com/tournament-api/load/{event_id}&filter=scholastic"
    response = requests.get(api_url, verify=False)
    if response.status_code == 200:
        print(f"Successfully fetched details for event ID {event_id}")
    else:
        print(f"Failed to fetch details for event ID {event_id}")
    return response.json()

# Function to generate a unique identifier for each event
def generate_uid(event_id, event_name, start_date):
    uid_base = f"{event_id}-{event_name}-{start_date}"
    uid_hash = hashlib.md5(uid_base.encode()).hexdigest()
    return uid_hash

# Define the timezone for Mountain Time
MT_TIMEZONE = "America/Denver"

# Function to strip HTML tags and extract text
def clean_html(raw_html):
    soup = BeautifulSoup(raw_html, "html.parser")
    return soup.get_text().strip()

# Extract event IDs
event_ids = extract_event_ids(url)

# Create a calendar
cal = Calendar()

# Current timestamp in UTC for last modified
now = arrow.utcnow()

# Loop through each event ID and fetch details
for event_id in event_ids:
    details = fetch_event_details(event_id).get("tournament", {})
    if not details:
        print(f"No details found for event ID {event_id}")
        continue

    # Create an event
    event = Event()
    event.name = f"♟️ {details.get('title').strip()}"

    # Set event begin date and time in Mountain Time
    start_date = details.get('startDate')
    event.begin = arrow.get(f"{start_date} 08:00", 'YYYY-MM-DD HH:mm', tzinfo=MT_TIMEZONE).isoformat()
    
    # Set event end date and time in Mountain Time (8 AM to 4 PM)
    event.end = arrow.get(f"{start_date} 16:00", 'YYYY-MM-DD HH:mm', tzinfo=MT_TIMEZONE).isoformat()

    # Set event location, trimming any extra spaces
    event.location = details.get("site", "").strip()

    # Set event description with HTML stripped and trimmed
    description_parts = [
        f"Time Control: {details.get('timeControl').strip()}",
        f"Registration: {details.get('registration').strip()}",
        f"Round Times: {details.get('roundTimes').strip()}",
        f"Comments: {clean_html(details.get('comments') or '')}"
    ]
    event.description = "\n\n".join(part for part in description_parts if part)

    # Set event URL using the provided format
    event.url = f"http://www.coloradochess.com/newtourn.shtml?id={event_id}"

    # Generate a unique identifier (UID) for the event
    event.uid = generate_uid(event_id, event.name, start_date)
    
    # Set the last modified time to the current script run time
    event.last_modified = now

    print(f"Adding event: {event.name}, UID: {event.uid}, Start: {event.begin}, End: {event.end}, URL: {event.url}, Last Modified: {event.last_modified}")
    # Add event to calendar
    cal.events.add(event)

# Save calendar to file
calendar_path = "Colorado_Scholastic_Chess_Events.ics"
with open(calendar_path, 'w') as f:
    f.writelines(cal.serialize_iter())

print(f"iCAL file created: {calendar_path}")
