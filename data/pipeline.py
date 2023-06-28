import pandas as pd
from sqlalchemy import create_engine
import numpy as np

def extract_data():
    # Extract data from web
    Munster = pd.read_excel('https://fazeelarif.com/Fahrzeugbestand-Regierungsbezirk-Muenster-2018-2022.xlsx')
    AutoScout24 = pd.read_excel('https://fazeelarif.com/AutoScout24.xlsx')
    return Munster, AutoScout24

def replace_null_values(df1, df2):
    print("Replacing NULL Values... ")
    # Replace Nan values with 0
    df1.replace(np.nan, 0, inplace=True)
    df2.replace(np.nan, 0, inplace=True)

# def transform_columns(df1, df2):
#     # Renaming the columns to English titles
#     print("Transformation... ")
#     df2.rename(columns={
#         "Jahr": "Year",
#         "unbe-kannt": "Unknown",
#         "insgesamt": "In Total",
#         "davon zweirädrige Kfz": "Two Wheel Vehicle",
#         "davon leichte vierrädrige Kfz": "Four Wheeler",
#         "darunter weibliche Halter": "Female Vehicle",
#         "und zwar mit Allrad-antrieb": "All Wheel Drive",
#     }, inplace=True)

    # Removing unwanted columns
    #df2.drop(columns=["Regierungsbezirk", "Hubraum bis 1.399 cm³", "PKW-Dichte je 1.000 Einwohner"], inplace=True)

def save_to_database(df1, df2):
    # Land data to Database
    print("-- Loading to database -- ")
    dataEngine = create_engine("sqlite:///MunsterAutoScout24.sqlite")
    df1.to_sql("Munster", dataEngine, if_exists="replace",index=False)
    df2.to_sql("AutoScout24", dataEngine, if_exists="replace",index=False)

# Main program
if __name__ == "__main__":
    MunsterData, AutoScout24Data = extract_data()
    replace_null_values(MunsterData, AutoScout24Data)
    #transform_columns(MunsterData, AutoScout24Data)
    save_to_database(MunsterData, AutoScout24Data)
