# Google Ads Auto Clicker

## Overview
The Google Ads Auto Clicker is a Python script that automates browsing and interaction with advertisements on a specified YouTube channel using Selenium and the Microsoft Edge WebDriver. The script mimics user behavior by visiting the channel, scrolling through the page, and clicking on ads found within the page.

## Features
- **Automated Browsing**: Visits a specified YouTube channel multiple times.
- **Ad Interaction**: Identifies and clicks on Google Ads within iframes.
- **Random User-Agent**: Mimics different browsers to prevent detection.
- **Multi-threading**: Simulates multiple concurrent visitors to the website.
- **Scrolling**: Automatically scrolls down the page to load additional ads.

## Requirements
- Python 3.x
- Selenium
- Microsoft Edge WebDriver
- Edge browser installed on your machine

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/BS-World/Google-Ads-auto-clicker.git
   cd Google-Ads-auto-clicker

2. **Install Dependencies**:
   You need to install the required packages. It’s recommended to use a virtual environment. 
   ```bash
   pip install selenium
   ```

3. **Download Microsoft Edge WebDriver**:
   - Download the appropriate version of the Edge WebDriver that matches your Edge browser version from [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
   - Place the `msedgedriver.exe` in a directory of your choice (e.g., `D:/Driver_Notes/`).

## Configuration
- Update the `EDGE_DRIVER_PATH` in the script to point to the location of `msedgedriver.exe`.
- Modify the `urls` list to include any other YouTube channels you want to target.
- Adjust the `user_agents` list as needed for more variety in user-agent strings.

## Usage
Run the script using Python:
```bash
python auto_clicker.py
```

The script will:
- Randomly visit the specified YouTube channel.
- Search for ad containers and click on any found ads.
- Scroll through the page to load more content.

## Important Notes
- **Ethical Use**: This script is intended for educational purposes. Be sure to comply with the terms of service of the websites you interact with and avoid causing harm or generating excessive load on any server.
- **Detection Risks**: Automated browsing may lead to detection and potential bans from websites. Use with caution.

## Contributing
Contributions are welcome! If you have suggestions for improvements or features, feel free to create an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Selenium](https://www.selenium.dev/) - For browser automation.
- [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) - For controlling the Edge browser.

## Contact
For any questions or inquiries, please reach out to [bhanubiswas98@gmail.com].

```


### Instructions
- Replace `auto_clicker.py` with the actual filename of your script.
- Update the contact email with your own.
- Feel free to add any additional sections (e.g., screenshots, FAQs) or details that might enhance the README for your audience.
