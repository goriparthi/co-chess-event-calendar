# Colorado Chess Event Calendar

This project provides an automated solution for generating an iCalendar (iCal) file with details of upcoming scholastic chess tournaments in Colorado. The script scrapes event data from the Colorado State Chess Association's website and creates an iCal file that can be subscribed to, ensuring you stay updated with the latest event information.

## Features

- **Automated Event Extraction**: The script fetches event details including titles, dates, times, locations, and descriptions from the Colorado Chess Association's scholastic tournament page.
- **iCal File Generation**: An `.ics` file is generated, which can be imported into most calendar applications.
- **Event Updates**: The script marks events with a last modified timestamp, ensuring that updates are reflected in subscribed calendars.
- **Customizable Details**: The script includes time control, registration details, round times, and comments in the event description.

## Usage

1. **Prerequisites**:
   - Python 3.6 or higher
   - Required Python packages (see `requirements.txt`)

2. **Setup**:
   - Clone this repository:
     ```bash
     git clone https://github.com/goriparthi/co-chess-event-calendar.git
     cd co-chess-event-calendar
     ```

   - Create and activate a virtual environment:
     ```bash
     python3 -m venv myenv
     source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
     ```

   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. **Running the Script**:
   - To generate the iCal file, simply run:
     ```bash
     python script.py
     ```

   - The generated iCal file, `Colorado_Scholastic_Chess_Events.ics`, will be saved in the project directory.

4. **Subscribing to the Calendar**:
   - Upload the `.ics` file to a hosting service or GitHub Pages, and use the URL to subscribe to the calendar in your preferred calendar application.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with improvements or new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

This project is inspired by the need to stay informed about scholastic chess events in Colorado. Special thanks to the Colorado State Chess Association for providing the data source.

---

Feel free to reach out if you have any questions or suggestions!
