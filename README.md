# OCFT - Organization Contact Finder Tool

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

## 📢 Overview

OCFT (Organization Contact Finder Tool) is a Python-based utility designed to help job seekers find email addresses and phone numbers of organization contacts. It leverages the Prospeo API to fetch contact information based on details provided in an Excel spreadsheet.

## 🚀 Features

- **Email Finding**: Discover professional email addresses using first name, last name, and company information
- **Mobile Number Discovery**: Find phone numbers associated with LinkedIn profiles
- **Batch Processing**: Process multiple contacts from an Excel file in one run
- **Excel Integration**: Automatically updates your Excel spreadsheet with the discovered information
- **User-Friendly Output**: Colorful console interface with clear status messages and progress tracking

## 🤖 How to Create a Telegram Bot and Get Its Token

To use the Telegram bot features in OCFT, you need to create your own Telegram bot and obtain its token:

1. Open the Telegram app and search for "BotFather".
2. Start a chat with BotFather and send the command `/newbot`.
3. Follow the instructions to choose a name and username for your bot.
4. After creation, BotFather will provide you with a bot token (a string like `123456789:ABCdefGhIJKlmNoPQRstuVwXyZ`).
5. Copy this token and add it to your `.env` file as follows:
   ```
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   ```

Keep your Telegram bot token secure and do not share it publicly.

## 🗝️🗝 How to Create a PROSPEO API key

To use OCFT, you need a valid Prospeo API key. Follow these steps to obtain one:

1. Visit the Prospeo website: [https://prospeo.io](https://prospeo.io)
2. Sign up for a free account or log in if you already have one.
3. Navigate to your dashboard or account settings.
4. Look for the "API Keys" section.
5. Click "Generate API Key" and copy the key provided.
6. Add this key to your `.env` file as follows:
   ```
   PROSPEO_API_KEY=your_prospeo_api_key_here
   ```

Keep your API key secure and do not share it publicly.

## 📋 Requirements

- Python 3.6+
- Required Python packages:
  - requests
  - pandas
  - colorama
  - urllib3
  - python-dotenv

## 🔧 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ravikant1918/ocft.git
   cd ocft
   ```

2. Install required dependencies:

   ```bash
   pip install requests pandas colorama urllib3 python-dotenv
   ```

3. Create a `.env` file in the root directory with the following variables:
   ```
   API_KEY=your_prospeo_api_key
   EXCEL_FILE=path_to_your_excel_file.xlsx
   ```

## 📊 Excel File Format

Your Excel file should contain the following columns:

- `first_name`: First name of the target contact
- `last_name`: Last name of the target contact
- `company`: Company name where the person works
- `linkedin_url`: LinkedIn profile URL of the target contact
- `email`: Column where found emails will be stored (can be empty initially)
- `number`: Column where found phone numbers will be stored (can be empty initially)

## 🔍 Usage

Simply run the main script:

```bash
python main.py
```

The tool will:

1. Display a banner with information about the tool
2. Load your Excel file specified in the `.env` file
3. Process each row in the file, calling the Prospeo API to find emails and phone numbers
4. Update the Excel file with the discovered information

## 🔄 How It Works

1. The tool reads contact information from your Excel file
2. For each contact, it calls two Prospeo API endpoints:
   - `/email-finder`: Uses first name, last name, and company to find email addresses
   - `/mobile-finder`: Uses LinkedIn URL to find phone numbers
3. Retrieved information is added to the Excel file
4. The updated Excel file is saved back to disk

## ⚠️ Notes

- The tool requires a valid Prospeo API key
- API rate limits are respected with a 1-second delay between requests
- Make sure your Excel file has all the required columns properly formatted

## 🔮 Future Plans

- Auto apply for jobs
- HR data retriever
- AI-powered organization search
- Additional API integrations for more comprehensive contact information

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

- **Ravi Kant Yadav** - [ravikant1918](https://github.com/ravikant1918)
- **Nikhil Goyal** - [cyberRuptor](https://github.com/cyberRuptor)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
