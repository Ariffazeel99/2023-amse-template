import pandas as pd
from sqlalchemy import create_engine
# Step 1: read data 
def data_extraction(url_path):
    print("1-Extraction of data")
    #Data Extraction
    try:
        df = pd.read_csv(url_path,on_bad_lines='skip',delimiter=';')
    except Exception as e:
        print("ERROR reading file:", str(e))
        return None
    print("1-Extraction of data done")
    return df
def data_transformation(data):
    print("2 -Data Transformation")
    #Data Transformation
    try:
        # Step 1 : Drop the Status column
        print("2.1-drop the Status column")
        data = data.drop('Status', axis=1)
        # Step 2 : Drop all rows with invalid values
        print("2.2-Drop all rows with invalid values")
        data['Breite'] = data['Breite'].str.replace(',', '.').astype(float)
        data['Laenge'] = data['Laenge'].str.replace(',', '.').astype(float)
        print("2.3-Verkehr column with FV, RV, nur DPN only")
        # Step 3 : Verkehr column with "FV", "RV", "nur DPN" only
        data = data[(data["Verkehr"].isin(["FV", "RV", "nur DPN"]))&(data["Laenge"].between(-90, 90))].dropna()
        print("2.4 -Range -90 to 90")
        # Step 4 : Range -90 to 90
        data = data[(data["Breite"].between(-90, 90))].dropna()
        print("2.5 -IFOPT")
        # Step 5 : IFOPT conditions
        data = data[(data["IFOPT"].str.match(r"^[A-Za-z]{2}:\d+:\d+(?::\d+)?$"))].dropna()
        print("2.6 -Data types updates")
        # Step 5 : Data types updates
        data_types = {
            "NAME": str,
            "EVA_NR": int,
            "DS100": str,
            "Breite": float,
            "Verkehr": str,
            "Laenge": float,
            "IFOPT": str,
            "Betreiber_Nr": int,
            "Betreiber_Name": str
        }
        data = data.astype(data_types)
    except Exception as e:
        print("ERROR reading file:", str(e))
        return None
    return data
def data_load(data, table):
    print("Step 3 - SQLite DB")
    engine = create_engine("sqlite:///trainstops.sqlite")
    data.to_sql(table,engine,if_exists = "replace",index=False)
if __name__ == "__main__":
    # 1  Data Extraction
    url_path = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"
    data = data_extraction(url_path)
    # 2 Data Transformation
    data= data_transformation(data)
    # 3 Data Loading
    data_load(data, "trainstops")


