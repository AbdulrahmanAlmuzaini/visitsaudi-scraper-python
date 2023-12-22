# VisitSaudi Scraper

## :warning: Disclaimer :warning:

> [!WARNING]
> This Python scraper is provided for educational and informational purposes only.

## Description

This Python script was used to gather data and feed it to `itinerary generation model` employed in this repository **[DarbAI-API-Endpoint](https://github.com/MohammmedAb/DarbAI-API-Endpoint)**, created by **[MohammmedAb](https://github.com/MohammmedAb/)**. The script is designed to scrape JSON responses from VisitSaudi's API, with a specific focus on retrieving data about 6 points of interest for each of the 13 reagions in Saudi Arabia:

POI:

1. **airport**
1. **accommodation**
1. **restaurants**
1. **shopping**
1. **attractions**
1. **experiences**

REGIONS:

1. **Eastern Province**
1. **Riyadh**
1. **Makkah**
1. **Madinah**
1. **Hail**
1. **Tabuk**
1. **Al Jouf**
1. **Northern Borders**
1. **Al Baha**
1. **Aseer**
1. **Al Qassim**
1. **Jazan**
1. **Najran**

The scraper incorporates 3 Python built-in libraries:

1. [**json**](https://docs.python.org/3/library/json.html) for reading and writing JSON files
1. [**urllib**](https://docs.python.org/3/library/urllib.html) for URL handling modules
1. [**os**](https://docs.python.org/3/library/os.html) for accessing OS interface and making directories, and files

and a third-party library:

1. [**requests**](https://requests.readthedocs.io/en/latest/) for sending get requests and queries

## Prerequisites

you need to install latest stable Python version from the offical website

[`Python`](https://www.python.org/downloads/)

Intstall `requests` via ternimal:

`python -m pip install requests`

or

`pip install requests`

## Setup the Project

`git clone https://github.com/AbdulrahmanAlmuzaini/visitsaudi-scraper-python.git`

or

Download the zip file of the project directly.

## How to Use the Project

you can run the script directly from `Terminal` or `CMD`, then all JSON responses will be written to your `Home Directory`. if you would like to modify the paramaters feel free to do so.

## Code Explaintion

There are 8 functions in total:

1. `main()` initiate the scraping process, iterating over regions and returning the total exported files.
1. `create_directory()` creates a directory using path passed to it.
1. `scrape_region()` iterate over POI categories for a region passed to it and returns count of POI files created for that region.
1. `construct_and_join_paths()` contructs and joins paths based on passed parameters, then returns constructed path.
1. `fetch_json()` fetches JSON response from the API, passes it to another function, and returns the number of files written.
1. `get_api_url()` constructs the API URL based on current parameters passed to it from the loop.
1. `export_json_file()` exports and writes JSON responses.
1. `exception_message()` prints formatted exception messages.
