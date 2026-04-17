from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nepse-free-api",
    version="1.0.0",
    author="Prasanga Pokharel",
    description="A lightweight web scraper for fetching real-time Nepali stock market data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prasangapokharel/NEPSE-FREE-API",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Education",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Internet :: WWW/HTTP",
        "Development Status :: 3 - Alpha",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
        "beautifulsoup4>=4.9.0",
        "certifi>=2021.0.0",
    ],
    keywords="nepse stock market nepal scraper web finance",
)
