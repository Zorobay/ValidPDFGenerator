import time
from pathlib import Path

import click

from lib import pdf_service, base64_service


@click.command(
    short_help="The argument PAGES specifies the total number of pages. Each page is approximately 1MB. Can also output base64 encoding of generated PDF.")
@click.argument('pages', default=None, type=int)
@click.option('--base64', is_flag=True, help="Also output base64 encoded representation of the pdf in a separate file.")
def run(pages: int, base64: bool):
    """
    Generates a valid PDF by specifying number of pages. Each page is approximately 1MB in size.
    """
    print("Producing document with {} pages.".format(pages))

    filename = "{}MB.pdf".format(pages)
    print("\nGenerating...")
    start = time.time()
    pdf_service.create_pdf(filename, pages)
    end = time.time()

    size_bytes = Path(filename).stat().st_size
    print("Generated '{}' ({:.3f}MB) in {:.3f}s".format(filename, size_bytes / (1000 * 1000), end - start))

    if base64:
        base64_filename = f"{Path(filename).stem}_base64.txt"
        print(f"\nGenerating base64 representation to {base64_filename}")
        base64_service.file_to_base64(filename, base64_filename)


if __name__ == '__main__':
    run()
