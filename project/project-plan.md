# Project Plan

## Summary

This project aims to explore the correlation between crimes and ATM locations in Berlin, by analyzing the Berlin Crimes dataset and the Berlin-Brandenburg Infrastructure ATM dataset.

## Rationale

The analysis will help identify if there is any relationship between the presence of ATM locations and the occurrence of crimes in Berlin. This information can be useful for law enforcement agencies to better allocate their resources and enhance public safety.

## Datasources

Datasource1: Berlin-Brandenburg Infrastructure ATM <br />
Metadata URL: https://mobilithek.info/offers/573328201445421056 <br />
Data URL: https://cloud4.aero/v1/files/mclick_dnotam.zip <br />
Data Type: xlsx
The dataset contains information about the location of ATMs in Berlin. This dataset will be used to geocode the ATM locations and join it with the Berlin Crimes dataset.

Datasource2: Crimes in Berlin <br />
Metadata URL: https://www.kaggle.com/datasets/danilzyryanov/crime-in-berlin-2012-2019/download?datasetVersionNumber=4 <br />
Data URL: https://www.kaggle.com/datasets/danilzyryanov/crime-in-berlin-2012-2019?select=Berlin_crimes.csv <br />
Data Type: xlsx
The dataset contains information about the crimes committed in Berlin from 2012 to 2019. This dataset will be used to explore the correlation between the crimes and ATM locations in Berlin.



## Work Packages


1. Find useful open data sources.
2. Data Collection and Preprocessing : This involves downloading and preprocessing the Berlin Crimes and Berlin-Brandenburg Infrastructure ATM datasets.
3. Clean and explore data.
4. Geocoding: This involves geocoding the ATM locations to obtain their latitude and longitude, which will be used to spatially join them with the Berlin Crimes dataset.
5. Analyze dataset and identify correlations : Finding correlation between the crimes and ATM locations in Berlin. 
6. Build data pipelines.
7. Visualization: This involves creating visualizations to communicate the findings of the analysis.
