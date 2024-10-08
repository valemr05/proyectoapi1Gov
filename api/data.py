import pandas as pd
from sodapy import Socrata
import numpy as np

def get_client():
    client = Socrata("www.datos.gov.co", "aLhzYIB1v3AjOH6WQU6PaXv4H")

    return client


def get_data(department, register, client):
    results = client.get("gt2j-8ykr", limit=register, departamento_nom=department)
    results_df = pd.DataFrame.from_records(results)

    return results_df


def filter_data(results_df):
    
    columns_to_display = [
        "ciudad_municipio_nom", 
        "departamento_nom", 
        "edad", 
        "fuente_tipo_contagio",
        "estado", 
        "recuperado"
    ]

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
     #imputing missing values
    results_df.replace("N/A", np.nan, inplace=True)
    results_df= results_df.dropna(subset=["ciudad_municipio_nom", 
        "departamento_nom", 
        "edad", 
        "fuente_tipo_contagio",
        "estado", 
        "recuperado"])
    
    return results_df[columns_to_display]

    
