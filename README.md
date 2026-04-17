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

## Disclaimer

This tool is for educational and informational purposes only. The author is not responsible for any financial decisions made based on the data retrieved by this scraper. Always verify data from official sources before making investment decisions.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve this project.

## Support

For issues, questions, or suggestions, please open an issue on the repository.
