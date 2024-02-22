# Valid PDF Generator

## Description

A small tool that generates valid PDFs of a specified number of pages. Each page is generated to closely approximate 1MB, so that 100 pages ≈ 100 MB.

## Setup

### Python
Developed using Python 3.12.

### Dependencies
Dependencies are handled by [Poetry](https://python-poetry.org/docs/). To install dependencies, run `poetry install`.
## Usage

### Generate PDF

```commandline
$ poetry run python .\main_generate_pdf.py --help

Usage: main_generate_pdf.py [OPTIONS] PAGES

  Generates a valid PDF by specifying number of pages. Each page is
  approximately 1MB in size. Can also output base64 encoding of generated PDF.

Options:
  --base64  Also output base64 encoded representation of the pdf in a separate
            file.
  --help    Show this message and exit.
```

### PDF to Base64 string

```commandline
$ poetry run .\main_to_base64.py --help

Usage: main_to_base64.py [OPTIONS] FILE

Options:
  --help  Show this message and exit.
```
