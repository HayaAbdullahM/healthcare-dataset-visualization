import pandas as pd

df = pd.read_csv('data/healthcare_dataset.csv')


def genders():
    genders = {
        'Female' : len(df[df["Gender"]=="Female"]["Gender"]),
        'Male' : len(df[df["Gender"]=="Male"]["Gender"]),
    }
    return genders

def medical_condition():
    return df["Medical Condition"].value_counts().to_dict()

def insurance_provider():
    return df["Insurance Provider"].value_counts().to_dict()

def blood_types():
    return df["Blood Type"].value_counts().to_dict()


def blood_medical():
    return df.groupby(['Blood Type', 'Medical Condition']).size().unstack()