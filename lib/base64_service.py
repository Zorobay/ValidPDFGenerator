import base64
from pathlib import Path


def file_to_base64(file: str, output_filename: str):
    filepath = Path(file)
    with open(file, "rb") as f:
        print(f"Reading {filepath}")

        with open(output_filename, "w") as fout:
            fout.write(base64.b64encode(f.read()).decode("utf-8"))
            print(f"Wrote base64 value to {output_filename}")
