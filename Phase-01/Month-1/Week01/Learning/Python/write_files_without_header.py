from pathlib import Path
import csv

def find_csv_files(directory):
    for path in Path(directory).absolute().rglob("*.csv"):
        yield path

def read_csv_content_without_header(csv_directory):
    with open(csv_directory, "r") as f:
        content = csv.reader(f)
        next(content, "Nothing found")
        for row in content:
            yield row 

def write_csv_content(csv_directory):
    new_path = (Path(csv_directory).parent / "without_header")
    new_path.mkdir(exist_ok=True)
    with open(new_path / csv_directory.name, "w", newline="") as f:
        csv_writer = csv.writer(f)
        for row in read_csv_content_without_header(csv_directory):
            csv_writer.writerow(row)
    print(f"Removed header from {csv_directory.name}.")

files_path = [path for path in find_csv_files(".")]

for path in files_path:
    write_csv_content(path)