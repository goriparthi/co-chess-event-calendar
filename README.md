# Colorado Chess Event Calendar

This project provides an automated solution for generating an iCalendar (iCal) file with details of upcoming scholastic chess tournaments in Colorado. The script scrapes event data from the Colorado State Chess Association's website and creates an iCal file that can be subscribed to, ensuring you stay updated with the latest event information.

## Features

- **Automated Event Extraction**: The script fetches event details including titles, dates, times, locations, and descriptions from the Colorado Chess Association's scholastic tournament page.
- **iCal File Generation**: An `.ics` file is generated, which can be imported into most calendar applications.
- **Event Updates**: The script marks events with a last modified timestamp, ensuring that updates are reflected in subscribed calendars.
- **Customizable Alerts**: Each event includes an alert set for 9 AM the day before, which includes the event's title.
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
   - You can use the provided `run.sh` script to automatically activate the virtual environment and run the Python script:
     ```bash
     ./run.sh
     ```

   - The script performs the following:
     - Checks for the existence of the virtual environment directory (`venv`) and the script (`script.py`).
     - Activates the virtual environment.
     - Runs the `script.py` to generate the iCal file.
     - Deactivates the virtual environment after execution.

   - The generated iCal file, `Colorado_Scholastic_Chess_Events.ics`, will be saved in the project directory.

4. **Hosting and Subscribing to the Calendar**:
   - The generated `.ics` file is hosted on GitHub Pages. You can subscribe to the calendar using the following options:
     - **Subscribe via iCal (webcal)**: Click the button below to subscribe directly to the calendar.
       - [Subscribe via iCal](webcal://goriparthi.github.io/co-chess-event-calendar/Colorado_Scholastic_Chess_Events.ics)
     - **Download .ics File**: Download the calendar file and manually import it into your calendar application.
       - [Download .ics File](https://goriparthi.github.io/co-chess-event-calendar/Colorado_Scholastic_Chess_Events.ics)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with improvements or new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

This project is inspired by the need to stay informed about scholastic chess events in Colorado. Special thanks to the Colorado State Chess Association for providing the data source.

---

Feel free to reach out if you have any questions or suggestions!
