# Mini Web Scraper with SimHash

## Project Overview

This project is a Python-based web scraper that:

- Takes **two URLs** from the command line
- Fetches their webpage content
- Extracts the body text
- Counts word frequencies
- Computes a **64-bit Polynomial Rolling Hash** for each word
- Generates a **64-bit SimHash fingerprint** for each webpage
- Calculates how many bits are common between the two SimHashes

This project demonstrates document similarity detection used in Information Retrieval systems.

---

## Concepts Used

- Web Scraping (requests, BeautifulSoup)
- Regular Expressions
- Word Frequency Counting
- Polynomial Rolling Hash
- Bit Manipulation
- SimHash Algorithm
- Hamming Distance

---

## how to run

pip install requests beautifulsoup4
python scraper.py <URL1> <URL2>

### Example:
python scraper.py https://example.com
https://iana.org/domains/reserved



## Purpose of This Project

This project demonstrates:

- Document fingerprinting
- Near-duplicate detection
- Core Information Retrieval concepts
- How search engines detect similar web pages

