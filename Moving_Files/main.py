import os
import time

import numpy as np
import pandas as pd


def generate_data(category):
    """This function was used to create the sample input."""

    time.sleep(1)

    n = 100
    column1 = np.random.choice(["A", "B", "C"], n)
    column2 = np.random.randint(0, 101, n)

    df = pd.DataFrame(
        {"Column1": column1, "Column2": column2}
    )

    timestamp = int(time.time())
    filename = f"{timestamp}_{category}.xlsx"

    df.to_excel(
        os.path.join("data/input/", filename),
        index=False
    )


def main():
    for _ in range(10):
        for c in ["A", "B", "C"]:
            generate_data(c)


if __name__ == "__main__":
    main()
