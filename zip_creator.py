import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            archive.write(filepath)


if __name__ == "__main__":
    make_archive(filepaths=["bouns2.2.py", "bouns.2.py"], dest_dir="dest")