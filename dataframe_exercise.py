import pandas as pd
import json
import numpy as np
import requests

approved = requests.get('http://127.0.0.1:8000/approved/api')
data = json.loads(approved.text)

def ensure_500k_rows(data):
    data = pd.DataFrame(data) 
    if len(data) < 500000:
        data = pd.concat([data] * (500000 // len(data) + 1), ignore_index=True)
    return data.head(500000)

print(ensure_500k_rows(data))


def describe_dataset(data):
    print("Dataset Overview:")
    print(data.info())
    print("\nDescriptive Statistics:")
    print(data.describe(include="all"))
    print("\nMissing Values:")
    print(data.isnull().sum())

    


def handle_missing_values(data):
    for column in data.columns:
        if data[column].isnull().sum() > 0:
            if data[column].dtype == "object":
                data[column].fillna(data[column].mode()[0], inplace=True)
            else:
                data[column].fillna(data[column].median(), inplace=True)
    return data



def basic_data_processing(data):
    data.drop_duplicates(inplace=True)
    for column in data.select_dtypes(include=["float64", "int64"]).columns:
        data[column] = (data[column] - data[column].min()) / (data[column].max() - data[column].min())
    return data

def create_features(data):
    if 'created_at' in data.columns:
        data['created_at'] = pd.to_datetime(data['created_at'], errors='coerce')
        data['year'] = data['created_at'].dt.year
        data['month'] = data['created_at'].dt.month
        data['day'] = data['created_at'].dt.day
    if 'password' in data.columns:
        data['is_password_test'] = data['password'].apply(lambda x: 1 if x.lower() == "test" else 0)
    return data


def process_json_dataset(json_data):
    data = ensure_500k_rows(json_data)
    
    describe_dataset(data)
    data = handle_missing_values(data)
    data = basic_data_processing(data)
    data = create_features(data)
    data.to_csv("processed_dataset.csv", index=False)
    print("Processed dataset saved as 'processed_dataset.csv'")
    return data


processed_data = process_json_dataset(data)
