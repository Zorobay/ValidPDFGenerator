from pathlib import Path

import click
import base64

@click.command()
@click.argument("file")
def run(file:str):

    filepath = Path(file)
    with open(file, "rb") as f:
        print(f"Reading {filepath}")
        output_filename = f"{filepath.stem}_base64.txt"

        with open(output_filename, "w") as fout:
            fout.write(base64.b64encode(f.read()).decode("utf-8"))
            print(f"Wrote base64 value to {output_filename}")


if __name__ == '__main__':
    run()
