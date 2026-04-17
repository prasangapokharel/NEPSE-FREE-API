# Nepse Free API - Stock Data Scraper

A Python web scraper for fetching real-time Nepali stock market data from nepalipaisa.com.

## Features

- **Real-time Stock Data**: Fetch current stock prices and market indices
- **Comprehensive Information**: Retrieve LTP (Last Traded Price), volume, price ranges, and averages
- **Fundamental Data**: Access company sector, dividend information, and year-over-year changes
- **Error Handling**: Robust error handling for network and parsing issues
- **Simple API**: Easy-to-use class-based interface

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. Clone or download the repository:
```bash
git clone <repository-url>
cd Nepse-Free-Api
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Example

```python
from main import Stock

# Create an instance of the Stock class
api = Stock()

# Fetch data for a specific stock symbol
result = api.get_data("ADBL")

# Display the results
for key, value in result.items():
    print(f"{key}: {value}")
```

### Available Stock Symbols

Common Nepali stock symbols include:
- `ADBL` - Arun Valley Trading Co.
- `NABIL` - Nabil Bank Limited
- `NTC` - Nepal Telecommunications Authority
- `EBL` - Everest Bank Limited
- `SCB` - Standard Chartered Bank Nepal
- And many more...

### Parameters

- `symbol` (str): Stock symbol to fetch data for. Default is "ADBL"

### Return Value

The `get_data()` method returns a dictionary containing:

| Key | Description |
|-----|-------------|
| `nepse_index` | Current NEPSE Index value |
| `nepse_change` | NEPSE Index change |
| `company_name` | Name of the company |
| `sector` | Company sector classification |
| `ltp` | Last Traded Price |
| `change` | Price change from previous close |
| `day_range` | Day's trading range |
| `volume` | Trading volume |
| `avg_120_days` | 120-day average price |
| `avg_180_days` | 180-day average price |
| `vwap_180_days` | 180-day Volume Weighted Average Price |
| `weeks_52_range` | 52-week price range |
| `one_year_change` | 1-year price change percentage |
| `last_updated` | Last data update timestamp |
| `dividend_fy` | Recent dividend fiscal year |
| `bonus_dividend` | Bonus dividend information |
| `cash_dividend` | Cash dividend information |

## Running the Script

Run the script directly from the command line:

```bash
python main.py
```

This will fetch and display ADBL stock data by default.

## Demo

### Live Terminal Output

The script provides clean, formatted output directly in your terminal:

![ADBL Stock Data Demo](demo/output.png)

### Output Example

```
=== ADBL Stock Data (as of latest scrape) ===

Nepse Index                   : 2,838.40
Nepse Change                  : 5.36
Company Name                  : Agricultural Development Bank Limited (ADBL)
Sector                        : Commercial Banks
Ltp                           : 318.00
Change                        : -0.40 (-0.13 %)
Day Range                     : 313.10 - 322.00
Volume                        : 29,709
Avg 120 Days                  : 305.56
Avg 180 Days                  : 306.56
Vwap 180 Days                 : High
Weeks 52 Range                : 272.30 - 344.90
One Year Change               : High
Share Outstanding             : 143,055,192
Beta                          : -
Paid Up Capital               : 14,305,519,200.00
1 Year Price Change           : 9%
Market Cap                    : 45,491,551,056.00
180 Day Vwap                  : Rs. 311.15
Eps                           : 9.89 (Q2, FY 82/83)
30 Days Av                    : 91,829
P E Ratio                     : 32.15
Bvps                          : 190.14
P B                           : 3.13
Recent Dividend               : FY 81/82
Last Updated                  : As of Fri, 17 Apr 2026 | 03:00:00 PM
Dividend Fy                   : FY 81/82
Bonus Dividend                : 3.25%
Cash Dividend                 : 9.75%
```

## Error Handling

The scraper handles two types of errors:

1. **Request Errors**: Network connectivity issues, timeouts, or invalid responses
2. **Parsing Errors**: Issues with HTML parsing or missing elements

Both errors are returned in the response dictionary with an `error` key:

```python
result = api.get_data("INVALID")
if "error" in result:
    print(f"Error: {result['error']}")
```

## Requirements

- `requests` - HTTP library for making web requests
- `beautifulsoup4` - HTML/XML parsing library
- `certifi` - SSL certificate validation

## Dependencies

All dependencies are listed in `requirements.txt` and can be installed with:

```bash
pip install -r requirements.txt
```

## Notes

- The scraper respects the website by using proper User-Agent headers
- Requests have a 15-second timeout to prevent hanging
- The script includes error handling for network failures and parsing issues
- Data is fetched from nepalipaisa.com in real-time

## License

This project is open source and available under the MIT License.

## Important Notice

⚠️ **EDUCATIONAL USE ONLY** ⚠️

This project is developed solely for **educational purposes**. It is not intended for production use or real-time financial decision-making due to:

- **Lack of Sandbox Testing**: This scraper has not been tested in a sandboxed environment or with official APIs. Web scraping may be subject to changes in website structure without notice.
- **No Warranty**: The author provides no guarantee about the accuracy, completeness, or timeliness of the scraped data.
- **Terms of Service**: Users are responsible for ensuring their use of this tool complies with nepalipaisa.com's Terms of Service and applicable laws.
- **Data Reliability**: Web-scraped data may be incomplete, delayed, or inaccurate.

## Disclaimer

This tool is for educational and informational purposes only. The author is not responsible for any financial decisions made based on the data retrieved by this scraper. Always verify data from official sources before making investment decisions. Use at your own risk.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve this project.

## Support

For issues, questions, or suggestions, please open an issue on the repository.
