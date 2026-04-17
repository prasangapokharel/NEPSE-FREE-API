import requests
from bs4 import BeautifulSoup
import certifi
from datetime import datetime


class Stock:
    """
    A web scraper class for fetching Nepali stock market data from nepalipaisa.com
    """

    def get_data(self, symbol="ADBL"):
        """
        Fetch stock data for a given company symbol

        Args:
            symbol (str): Stock symbol (e.g., "ADBL", "NABIL", "NTC")

        Returns:
            dict: Dictionary containing stock information or error message
        """
        url = f"https://nepalipaisa.com/company/{symbol}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
        }

        try:
            res = requests.get(url, headers=headers, verify=certifi.where(), timeout=15)
            res.raise_for_status()
            soup = BeautifulSoup(res.text, "html.parser")

            data = {}

            # 1. NEPSE Index
            nepse_index = soup.select_one("#liIndex p")
            data["nepse_index"] = (
                nepse_index.get_text(strip=True) if nepse_index else "Not found"
            )

            nepse_change = soup.select_one("#liDiff span")
            data["nepse_change"] = (
                nepse_change.get_text(strip=True) if nepse_change else "Not found"
            )

            # 2. Company Name & Basic Info
            company_name = soup.select_one("h1")
            data["company_name"] = (
                company_name.get_text(strip=True) if company_name else "Not found"
            )

            # Contact / Basic Details
            sector = soup.find("catg", string="Sector:")
            data["sector"] = (
                sector.find_parent("p")
                .get_text(strip=True)
                .replace("Sector:", "")
                .strip()
                if sector
                else "Not found"
            )

            # 3. Last Traded Price (LTP) + Change
            ltp_block = soup.select_one(".co-highlight-block.ltp span")
            if ltp_block:
                full_text = ltp_block.get_text(strip=True, separator=" ")
                parts = full_text.split()
                data["ltp"] = parts[0] if parts else "Not found"
                data["change"] = " ".join(parts[1:]) if len(parts) > 1 else "Not found"
            else:
                data["ltp"] = "Not found"
                data["change"] = "Not found"

            # 4. Day Range, Volume, Averages
            day_range = soup.find("p", string="Trade Day Range")
            data["day_range"] = (
                day_range.find_next("span").get_text(strip=True)
                if day_range
                else "Not found"
            )

            volume_tag = soup.find("p", string="Volume")
            data["volume"] = (
                volume_tag.find_next("span").get_text(strip=True)
                if volume_tag
                else "Not found"
            )

            avg_120 = soup.find("p", string="120 Days Avg Price")
            data["avg_120_days"] = (
                avg_120.find_next("span").get_text(strip=True)
                if avg_120
                else "Not found"
            )

            avg_180 = soup.find("p", string="180 Days Avg Price")
            data["avg_180_days"] = (
                avg_180.find_next("span").get_text(strip=True)
                if avg_180
                else "Not found"
            )

            vwap_180 = soup.find("p", string="180 Day VWAP")
            data["vwap_180_days"] = (
                vwap_180.find_next("span").get_text(strip=True)
                if vwap_180
                else "Not found"
            )

            # 5. 52 Weeks Range & 1 Year Change
            weeks_range = soup.find("p", string="52 Weeks Range")
            data["weeks_52_range"] = (
                weeks_range.find_next("span").get_text(strip=True)
                if weeks_range
                else "Not found"
            )

            year_change = soup.find("p", string="1 Year Price Change")
            data["one_year_change"] = (
                year_change.find_next("span").get_text(strip=True)
                if year_change
                else "Not found"
            )

            # 6. Market Summary Section (Most Important Fundamentals)
            summary_blocks = soup.select(".indices.summary-turnover")

            for block in summary_blocks:
                title_tag = block.select_one(".title")
                value_tag = block.select_one(".value")
                if title_tag and value_tag:
                    title = title_tag.get_text(strip=True).replace("title=", "").strip()
                    value = value_tag.get_text(strip=True)

                    key = (
                        title.lower()
                        .replace(" ", "_")
                        .replace("/", "_")
                        .replace("(", "")
                        .replace(")", "")
                    )
                    data[key] = value

            # 7. Last Updated Time
            last_updated = soup.select_one(".co-date p")
            data["last_updated"] = (
                last_updated.get_text(strip=True) if last_updated else "Not found"
            )

            # 8. Recent Dividend
            dividend_section = soup.find(
                "p", string=lambda t: t and "Recent Dividend" in t
            )
            if dividend_section:
                data["dividend_fy"] = (
                    dividend_section.find_next("p", class_="value").get_text(strip=True)
                    if dividend_section.find_next("p", class_="value")
                    else ""
                )

                bonus = soup.find("p", string="Bonus")
                cash = soup.find("p", string="Cash")
                if bonus:
                    data["bonus_dividend"] = bonus.find_next(
                        "p", class_="value"
                    ).get_text(strip=True)
                if cash:
                    data["cash_dividend"] = cash.find_next(
                        "p", class_="value"
                    ).get_text(strip=True)

            return data

        except requests.exceptions.RequestException as e:
            return {"error": f"Request failed: {str(e)}"}
        except Exception as e:
            return {"error": f"Parsing error: {str(e)}"}


if __name__ == "__main__":
    api = Stock()
    result = api.get_data("ADBL")  # You can change symbol e.g. "NABIL", "NTC" etc.

    print("=== ADBL Stock Data (as of latest scrape) ===\n")
    for key, value in result.items():
        print(f"{key.replace('_', ' ').title():<30}: {value}")
