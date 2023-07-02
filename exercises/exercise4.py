import os
import urllib.request
import zipfile
import pandas as pd
import sqlite3

# Step 1 download function to download the ZIP file
def download_zip_file(url, file_path):
    urllib.request.urlretrieve(url, file_path)

# Step 2 unzip function to extract the data.csv file from the downloaded ZIP file
def unzip_file(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

# Step 3 data processing function to reshape and transform the dat
def data_transformation():
    # Read the CSV file
    # reading in the csv file
    df = pd.read_csv("data.csv", sep=";", decimal=",", index_col=False,usecols=["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)","Batterietemperatur in °C", "Geraet aktiv"])

    # renaming columns
    df = df.rename(columns={"Temperatur in °C (DWD)": "Temperatur", "Batterietemperatur in °C": "Batterietemperatur"})

    # transforming data
    df["Temperatur"] = df["Temperatur"] * 9 / 5 + 32
    df["Batterietemperatur"] = df["Batterietemperatur"] * 9 / 5 + 32

    return df
# Step 4  data validation function
def Data_Validations(df):
    # Validate Geraet column
    df = df[df["Geraet"] > 0 &(df["Monat"] > 0)]
    return df
# Step 5 function to write the data to the SQLite database
def Load_data(df, db_path, table_name):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

# Step 6 main function
def main():
    # Set the file paths
    db_path = "temperatures.sqlite"
    zip_file_path = "mowesta-dataset-20221107.zip"
    csv_file_path = "data.csv"

    # Step 1: Download the ZIP file
    download_zip_file("https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip", zip_file_path)
    print("download_zip_file successfully.")
    # Step 2: Unzip the file and get the CSV file path
    unzip_file(zip_file_path, ".")

    print("unzip_file successfully.")

    # Step 3: data_transformation
    df = data_transformation()
    print("data_transformation successfully.")

    # Step 4: Data_Validations
    df = Data_Validations(df)
    print("Data_Validations successfully.")

    # Step 5: Load_data
    Load_data(df, db_path, "temperatures")
    print("data loaded successfully.")

    print("Data pipeline runs successfully.")



# -- Main --
if __name__ == "__main__":
    main()
