import requests
import pandas as pd
import logging
from colorama import Fore, Style, init
import urllib3
import time,os
from dotenv import load_dotenv
load_dotenv()
# Initialize colorama
init(autoreset=True)
# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Setup logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)


class DisplayBanner:
    """
    Handles displaying a banner with information about the tool.
    """
    def __init__(self):
        self.banner = [
            Fore.CYAN + Style.BRIGHT + "=" * 60,
            Fore.GREEN + Style.BRIGHT + "📢 ORGANIZATION CONTACT FINDER TOOL",
            Fore.YELLOW + "🚀 Purpose: Help job seekers find email and phone numbers of organizations.",
            Fore.YELLOW + "✨ Future plans: Auto apply jobs, HR data retriever, AI-powered organization search...",
            Fore.CYAN + "=" * 60 + "\n"
        ]

    def display(self):
        """
        Prints the banner to the console with color formatting.
        """
        for line in self.banner:
            print(line)
        time.sleep(1)

class JobSeeker:
    """
    Main class for processing job seeker data, calling APIs to find emails and phone numbers,
    and updating the Excel file with the results.
    """
    def __init__(self):
        """
        Initializes the JobSeeker with configuration from environment variables and loads the Excel file.
        """
        self.excel_file = os.getenv('EXCEL_FILE', 'data.xlsx')
        self.api_key = os.getenv('API_KEY', 'af836ff9f20d62b1db06fb4151233136')
        self.base_url = 'https://api.prospeo.io'
        self.headers = {
            'Content-Type': 'application/json',
            'X-KEY': self.api_key
        }
        try:
            df = pd.read_excel(self.excel_file)
            logger.info(f"📂 Loaded Excel file: {self.excel_file}")
        except Exception as e:
            logger.error(f"Failed to load Excel file: {e}")
            return
        self.df = df
        
    def api_executions(self, data, API_URL):
        """
        Executes a POST request to the given API URL with the provided data and headers.
        Returns the JSON response or an error dict on failure.
        """
        try:
            resp = requests.post(API_URL, json=data, headers=self.headers, verify=False, timeout=15)
            resp.raise_for_status()
            response_json = resp.json()
            logger.debug(f"API Response: {response_json}")
            return response_json
        except Exception as e:
            logger.error(f"API call failed: {e}")
            return {'error': True}

    def call_prospeo_email_finder(self):
        """
        Calls the Prospeo Email Finder API using the current row's first name, last name, and company.
        Returns the API response as a dict.
        """
        EMAIL_FINDER_URL = f"{self.base_url}/email-finder"
        data = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'company': self.company
        }
        try:
            response_json = self.api_executions(data, EMAIL_FINDER_URL)
            logger.debug(f"Email Finder Response: {response_json}")
            return response_json
        except Exception as e:
            logger.error(f"Email Finder API call failed: {e}")
            return {'error': True}

    def call_prospeo_mobile_finder(self):
        """
        Calls the Prospeo Mobile Finder API using the current row's LinkedIn URL.
        Returns the API response as a dict.
        """
        MOBILE_FINDER_URL = f"{self.base_url}/mobile-finder"
        data = {'url': self.linkedin_url}
        try:
            response_json = self.api_executions(data, MOBILE_FINDER_URL)
            logger.debug(f"Mobile Finder Response: {response_json}")
            return response_json
        except Exception as e:
            logger.error(f"Mobile Finder API call failed: {e}")
            return {'error': True}
    
    def run(self):
        """
        Iterates through each row in the Excel file, calls the email and mobile finder APIs,
        updates the DataFrame with the results, and saves the updated file.
        """
        for idx, row in self.df.iterrows():
            self.linkedin_url = row.get('linkedin_url')
            self.first_name = row.get('first_name')
            self.last_name = row.get('last_name')
            self.company = row.get('company')

            if not self.linkedin_url or not self.first_name or not self.last_name or not self.company:
                # Ensure idx is an integer before performing addition
                if isinstance(idx, int):
                    logger.warning(f"⚠️  Skipping row {idx + 2}: missing fields")
                else:
                    logger.warning(f"⚠️  Skipping row: missing fields")
                continue

            logger.info(Fore.BLUE + f"[+] Processing {self.first_name} {self.last_name} at {self.company}")

            # Call Email Finder API
            email_resp = self.call_prospeo_email_finder()
            email = email_resp['response']['email'] if isinstance(email_resp, dict) and 'response' in email_resp and isinstance(email_resp['response'], dict) else ''
            
            # Call Mobile Finder API
            mobile_resp = self.call_prospeo_mobile_finder()
            mobile = mobile_resp['response']['mobile'] if isinstance(mobile_resp, dict) and 'response' in mobile_resp and isinstance(mobile_resp['response'], dict) else ''

            logger.info(Fore.GREEN + f" --> Found Email: {email}, Number: {mobile}")

            # Update DataFrame
            self.df.at[idx, 'email'] = email
            self.df.at[idx, 'number'] = mobile

            time.sleep(1)  # To respect rate limits

        try:
            self.df.to_excel(self.excel_file, index=False)
            logger.info(Fore.GREEN + "[✔️] Excel file updated successfully!")
        except Exception as e:
            logger.error(f"Failed to save Excel file: {e}")

        
if __name__ == '__main__':
    banner = DisplayBanner()
    banner.display()
    job_seeker = JobSeeker()
    job_seeker.run()
