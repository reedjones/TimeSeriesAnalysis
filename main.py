import pandas as pd
import csv, os, pathlib, json

fp = "C:\\Users\\reedj\\Documents\\StratusDATA\\NEWDATAFolder\\5_1_2022_DATEAEXPORT.csv"


def get_data():
    return pd.read_csv(fp)
