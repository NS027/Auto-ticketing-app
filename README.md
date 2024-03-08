# Automatic Ticket Purchasing Program

## Project Overview
This program is an automated script for purchasing tickets from [Damai](https://www.damai.cn/), a popular ticketing website. It's designed for educational purposes to demonstrate the capabilities of web automation using Python and Selenium. This script specifically targets tickets for concerts (e.g., Jay Chou's concert).

## Features
- Automated login using Selenium WebDriver and cookies.
- Automatic page refresh to check ticket availability.
- Seat selection and order processing for available tickets.

## Prerequisites
Before running this script, you'll need:
- Python 3.x installed on your system.
- Selenium WebDriver installed and properly configured.
- Google Chrome browser installed (since the script uses `webdriver.Chrome()`).

## Installation
1. Clone this repository or download the script.
2. Install Selenium: Run `pip install selenium` in your command line.
3. Download the appropriate Chrome WebDriver for your version of Google Chrome from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in the project directory or system path.

## Usage
1. Run the script using Python: `python script_name.py`
2. A Chrome browser window will open, navigate to the Damai login page and ask you to scan a QR code for login.
3. After logging in, the script will save a cookie to facilitate future logins.
4. The script will automatically check for ticket availability and proceed with the purchase process.

## Important Notes
- This script is for educational purposes and should not be used to violate any terms of service of the Damai website.
- The effectiveness of the script depends on various factors like internet speed, website changes, etc.
- Be aware of legal and ethical considerations when using automated scripts for online purchases.

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [issues page](link-to-issues-page) if you want to contribute.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
If you have any queries or suggestions, feel free to reach out (provide contact information).

---

*This README was last updated on [2024-Mar-08].*

