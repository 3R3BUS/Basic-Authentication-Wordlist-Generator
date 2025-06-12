# Basic Auth Generator

This tool is a Python script that reads a wordlist file, processes each word by adding a specified prefix (e.g., `admin:`), Base64 encodes the result, removes the padding, and saves the modified list into an output file. It’s particularly useful for generating wordlists for basic authentication brute-forcing.

## Features:
- Takes a prefix (e.g., `admin:`) and a wordlist as input.
- Encodes each entry in the wordlist with a Base64-encoded string (`prefix:<word>`).
- Removes Base64 padding (`==`).
- Can process up to the first 25,000 lines from the wordlist.
- Outputs the modified list to a specified file (or defaults to `updated-rock.txt`).

---

## Requirements:

- Python 3.x
- A wordlist file (e.g., `/usr/share/wordlists/rockyou.txt`)

---

## Usage:

### Command Line Syntax:

```bash
python3 basic-auth-generator.py <prefix-username> <input/wordlist> <-o optional output filename>
