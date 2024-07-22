import os
import shutil
import time

import numpy as np
import pandas as pd

FOLDER_INPUT = "data/input/"
FOLDER_OUTPUT = "data/output/"


def generate_data(process_type):
    """This function was used to create the sample input."""

    time.sleep(1)

    n = 100
    column1 = np.random.choice(["X", "Y", "Z"], n)
    column2 = np.random.randint(0, 101, n)

    df = pd.DataFrame(
        {"Column1": column1, "Column2": column2}
    )

    timestamp = int(time.time())
    filename = f"{timestamp}_{process_type}.xlsx"

    df.to_excel(
        os.path.join("data/input/", filename),
        index=False
    )


def get_list_files():
    """Lists all files in the input folder."""
    files = os.listdir(FOLDER_INPUT)

    return files


def get_process_type(file):
    """Parses the name of the process given in the file name."""
    return file.split("_")[1][:-4]


def create_folders(files):
    """Creates for each process a folder in the output folder
       of this project.
    """
    # Creates a set of all process names
    names_folders = set(
        [get_process_type(f) for f in files]
    )

    # If the folders do not exist we create them
    for name in names_folders:
        try:
            os.mkdir(os.path.join(FOLDER_OUTPUT, name))
        except FileExistsError:
            pass


def copy_files_to_folders(files):
    """Copies each file into the corresponding folder in the
       output directory.
    """
    for f in files:
        process_type = get_process_type(f)
        shutil.copyfile(
            os.path.join(FOLDER_INPUT, f),
            os.path.join(FOLDER_OUTPUT, process_type, f)
        )


def main():
    # Get all files in the input folder
    files = get_list_files()

    # Prepare the output folder by creating subdirectories
    # for each process
    create_folders(files)

    # Copy files to the destinations in the output folder
    copy_files_to_folders(files)


if __name__ == "__main__":
    main()
