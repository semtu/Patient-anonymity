import json
import math
import os
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class anonymity_restore:
    """
    This is a class for the anonymity_restore function

    Attributes:
        data_path (str): Specify path to data.
    """

    def __init__(self, data_path: str):
        """
        The constructor for the class.
        """
        self.DATA_PATH = os.path.join(BASE_DIR, data_path)
        try:
            self.df = pd.read_excel(self.DATA_PATH, index_col=0)
            with open(
                os.path.join(BASE_DIR, "data/column_names.json"), "r"
            ) as jsonFile:
                self.column_names = json.load(jsonFile)
        except FileNotFoundError:
            print("Data sheet not found")
        except OSError:
            print("Error opening data sheet")

    def restore_column(self):
        """
        This function restores the original data. It merges the columns dropped and those from
        the remove function using the usingID as a key

        Returns: ''
        """
        try:
            dropped_columns = pd.read_csv(
                os.path.join(BASE_DIR, "data/temp_db.csv"), index_col=0
            )
            self.df = pd.merge(self.df, dropped_columns, on="uniqueID")
            self.df = self.df[self.column_names]
            self.df.to_excel(os.path.join(BASE_DIR, "restored.xlsx"), "Sheet1")
        except (FileNotFoundError, OSError) as error:
            print(error)
        return


if __name__ == "__main__":
    restore_obj = anonymity_restore("removed.xlsx")
    restore_obj.restore_column()
