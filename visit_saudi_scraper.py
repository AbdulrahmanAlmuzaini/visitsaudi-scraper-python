import requests
import json
import os
from urllib.parse import urlencode

# Constants and configuration
BASE_API_URL = "https://map.visitsaudi.com/api/pointsOfInterest?"
LOCALE = "en"
TYPE = "city"
CATEGORY_TYPES = ["airport", "accommodation", "restaurants", "shopping", "attractions", "experiences"]
REGION_CODE_VALUES = {
    "EAS": "Eastern Province",
    "RUH": "Riyadh",
    "MAK": "Makkah",
    "MED": "Madinah",
    "HAS": "Hail",
    "TUU": "Tabuk",
    "AJF": "Al Jouf",
    "NOB": "Northern Borders",
    "BAH": "Al Baha",
    "ASR": "Aseer",
    "AQM": "Al Qassim",
    "JEC": "Jazan",
    "NJN": "Najran"
}

PROCESS_STARTED_MESSAGE = "\n[Scraping process started]"
PROCESS_COMPLETED_MESSAGE = "\n[Scraping process completed]"

# Contruct and join paths based on passed path
def construct_and_join_paths(*path):
    return os.path.expanduser(os.path.join(*path))

# Setting the main directory in user or home directory, this directory hold all exported data
MAIN_DIRECTORY_NAME = "VisitSaudi_Scraped_JSONs"
MAIN_DIRECTORY_PATH = construct_and_join_paths(MAIN_DIRECTORY_NAME)

# Create directory using passed path
def create_directory(directory_path):
    try:
        os.makedirs(directory_path, exist_ok=True)
    except OSError as exception:
        print(f"Failed to make directory \nPath:{directory_path} {exception_message(exception)}")

# Sets region directory path, iterate over each category, and return file count
def scrape_region(region, file_count):
    region_directory_path = construct_and_join_paths(MAIN_DIRECTORY_PATH, region)
    create_directory(region_directory_path)
    for category in CATEGORY_TYPES:
        file_count = fetch_json(region_directory_path, region, category, file_count)
    return file_count

# Fetches json response from the VisitSaudi API based on passed region and category, and return file count
def fetch_json(region_directory_path, region, category, file_count):
    try:
        # Sending a GET request to the API, and check if the request was successful
        response = requests.get(get_api_url(region, category))
        response.raise_for_status()
    except requests.exceptions.RequestException as exception:
        print(f"exception occured with API request {exception_message(exception)}")
    else:
        # if response status was OK (200) then proceed
        if response.ok:
            # Store JSON-encoded content of the repsonse into a variable
            json_content = response.json()
            # Set a file name for current region and category
            file_name = f"exported_JSON_{region}_{category}.json"
            export_json_file(json_content, construct_and_join_paths(region_directory_path, file_name))
            file_count += 1
        else:
            print(f"Failed to fetch data for \nRegion: {region}\nCategory: {category}\nStatus Code: {response.status_code}\nReason: {response.reason}")
    return file_count

# Constructs and returns the API URL based on passed region and category
def get_api_url(region, category):
    # URL structure .../pointsOfInterest?regions=region_code&locale=en&type=city&categories=category_type
    # example: .../pointsOfInterest?regions=AQM,HAS&locale=en&type=city&categories=attractions,experiences
    # query_parameters holds the parameters that will be sent to the api
    query_parameters = {
        "regions": region,
        "locale": LOCALE,
        "type": TYPE,
        "categories": category
    }
    return f"{BASE_API_URL}{urlencode(query_parameters)}"

# Export JSON data to file
def export_json_file(json_content, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(json_content, file, indent=4)
        print(f"JSON file successfully exported to {file_path}")
    except Exception as exception:
        print(f"Failed to export JSON file \nPath: {file_path} {exception_message(exception)}")

# return string contains expception class and type of exception
def exception_message(exception):
    return f"\nException Class: {type(exception).__name__} \nException: {exception}"

# Main function to initiate the scraping process
def main(file_count):
    create_directory(MAIN_DIRECTORY_PATH)
    for region in REGION_CODE_VALUES:
        print(f"\nScraping {REGION_CODE_VALUES[region]} ({region}):")
        file_count = scrape_region(region, file_count)
    return file_count
    
if __name__ == "__main__":
    print(PROCESS_STARTED_MESSAGE)
    file_count = 0
    file_count = main(file_count)
    print(PROCESS_COMPLETED_MESSAGE)
    print(f"\nTotal regions scraped: {int(file_count/len(CATEGORY_TYPES))}")
    print(f"Total files exported: {file_count}")