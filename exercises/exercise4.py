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
    df = df[df["Geraet"] > 0]

    df = df[df['Monat'].between(1, 12)]

    # Validate Hersteller to be non-empty strings
    df = df[df['Hersteller'].apply(lambda x: isinstance(x, str) and x.strip() != "")]

    # Validate Model to be non-empty strings
    df = df[df['Model'].apply(lambda x: isinstance(x, str) and x.strip() != "")]

    # Validate Temperatur and Batterietemperatur to be numeric and non-null
    df = df[df['Temperatur'].apply(lambda x: pd.to_numeric(x, errors='coerce') is not None)]
    df = df[df['Batterietemperatur'].apply(lambda x: pd.to_numeric(x, errors='coerce') is not None)]

    # Validate Geraet aktiv to be either "Ja" or "Nein"
    df = df[df['Geraet aktiv'].isin(['Ja', 'Nein'])]

    return df
# Step 5 function to write the data to the SQLite database
def Load_data(df, db_path, table_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # Define the table name and schema
    table_name = table_name
    table_schema = [
        ("Geraet", "BIGINT"),
        ("Hersteller", "TEXT"),
        ("Model", "TEXT"),
        ("Monat", "TEXT"),
        ("Temperatur", "FLOAT"),
        ("Batterietemperatur", "FLOAT"),
        ("Geraet_aktiv", "TEXT")
    ]
    # Create the table
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
    for column, data_type in table_schema:
        create_table_query += f"{column} {data_type}, "
    create_table_query = create_table_query.rstrip(", ") + ")"

    cursor.execute(create_table_query)

    # Commit the changes and close the connection
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.commit()
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
