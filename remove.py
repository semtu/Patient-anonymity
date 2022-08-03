import json
import math
import os
import pandas as pd
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class anonymity_remove:
    """
    This is a class for the anonymity_remove function

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
                os.path.join(BASE_DIR, "data/column_names.json"), "w"
            ) as jsonFile:
                json.dump(self.df.columns.to_list(), jsonFile)
        except FileNotFoundError:
            print("Data sheet not found")
        except OSError:
            print("Error opening data sheet")

    def uniqueID(self):
        """
        This function creates a uniqueID column

        Returns: The dataframe object
        """
        n = len(self.df)
        digits = int(math.log10(n)) + 1
        self.df["uniqueID"] = ["{0}".format(str(i + 1).zfill(digits)) for i in range(n)]
        return self.df

    def remove_column(self, columns=list()):
        """
        This function removes specified columns

        Parameters:
            Columns: Specify the columns to be removed from the data in a python list.
                     If no column value is entered, an empty list is passed and no column is removed.

        Returns: ''
        """
        if isinstance(columns, list):
            try:
                self.uniqueID().drop(columns, axis=1).to_excel(
                    os.path.join(BASE_DIR, "removed.xlsx"), "Sheet1"
                )
                columns.append("uniqueID")
                self.df[columns].to_csv(
                    os.path.join(BASE_DIR, "data/temp_db.csv")
                )  # Stores columns to be removed in temporary database
            except KeyError:
                for column in columns:
                    if column not in self.df.columns:
                        print(f" {column} is not a valid column name in the data.")
        return


if __name__ == "__main__":
    columns = ["name", "age", "city"]
    remove_obj = anonymity_remove("data.xlsx")
    remove_obj.remove_column(columns)
