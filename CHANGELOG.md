# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-04-17

### Added
- Initial release of NEPSE-FREE-API
- Core Stock class for fetching real-time stock data
- Support for 335+ Nepali stock symbols
- Comprehensive error handling for network and parsing errors
- Real-time NEPSE index data fetching
- Company fundamental data (P/E ratio, P/B ratio, dividend info, etc.)
- Professional README with badges and documentation
- Symbol.csv with clean list of all available symbols
- Setup.py for package installation
- Contributing guidelines and templates
- MIT License
- Demo screenshot showing terminal output
- Support for multiple stock queries
- Batch processing capability
- CSV export examples

### Features
- Fetch LTP (Last Traded Price)
- Get price change and percentage change
- Day range information
- Trading volume data
- 120-day and 180-day average prices
- VWAP (Volume Weighted Average Price)
- 52-week price range
- 1-year price change
- Company sector information
- Dividend information (cash and bonus)
- Market capitalization
- EPS and P/E ratio
- BVPS and P/B ratio
- Last update timestamp

### Documentation
- Comprehensive README with 513 lines
- API Reference documentation
- Advanced usage examples
- Error handling guide
- Installation instructions
- Quick start guide
- Contributing guidelines
- Issue templates for bugs and features
- Pull request template

## Future Releases

### [1.1.0] - Planned
- [ ] Caching mechanism for frequently accessed data
- [ ] REST API wrapper
- [ ] Command-line interface (CLI)
- [ ] Real-time data streaming
- [ ] Excel export functionality
- [ ] JSON export functionality
- [ ] Historical data storage
- [ ] Data visualization

### [2.0.0] - Planned
- [ ] Web dashboard
- [ ] Database integration
- [ ] Advanced analytics
- [ ] Portfolio tracking
- [ ] Alert system
- [ ] API authentication
- [ ] Rate limiting

---

## Notes

### Version 1.0.0 Release Notes

This is the initial release of NEPSE-FREE-API. The project has been thoroughly tested with:
- Python 3.7, 3.8, 3.9, 3.10, 3.11
- Multiple stock symbols
- Various network conditions
- Error scenarios

#### Known Limitations
- Educational use only (not for production)
- Dependent on nepalipaisa.com website structure
- No real-time alerts or notifications
- Limited historical data (current day only)
- Web scraping risks (website may change structure)

#### Breaking Changes
None (initial release)

---

## How to Report Issues

If you encounter bugs or issues:
1. Check existing issues first
2. Create a detailed bug report with:
   - Python version
   - Operating system
   - Steps to reproduce
   - Expected vs actual behavior
   - Error messages/tracebacks

## How to Request Features

To request new features:
1. Check existing feature requests
2. Submit a detailed feature request with:
   - Clear description
   - Use case/benefit
   - Proposed implementation (optional)
   - Alternative solutions (if any)
