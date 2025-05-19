# Regex Pattern Examples in Python

## Project Overview

This small Python project shows **how to recognise and extract everyday text patterns** with the standard `re` module.  It can be used as a learning reference or as a starting‑point utility for cleaning or mining raw text.

The script accepts a text file or a raw string, applies a set of pre‑written regular expressions, and prints every match it finds, grouped by category.

---

## Patterns Covered
**Category:**
- Email addresses: Standard formats with optional sub‑domains and country‑code TLDs
- Hashtags: Words starting with # (supports CamelCase)
- URLs: HTTP/HTTPS links with optional sub‑domains and paths
- Phone Numbers: North‑American style with separators like "() – ."
- Credit‑card numbers: 16‑digit numbers split by spaces or hyphens

> **Note**: The regexes are intentionally readable rather than fully production‑hardened; they aim to teach the basics and may not catch every edge‑case.

---

## Quick Start

1. **Clone or download** the repository.
2. Ensure you have **Python 3.8+** installed.
3. Run the demo script:

```bash
python main.py sample_input.txt
```

---

## Limitations & Future Ideas

* Patterns are tuned for English/US formats; localisation is possible.
* Phone numbers are North‑American only – consider using a library such as **`phonenumbers`** for global support.
* Credit‑card pattern ignores checksum validation; Luhn‑check could be added.

---

## Author

*Maurice NSHIMYUMUKIZA* – Kigali, Rwanda
