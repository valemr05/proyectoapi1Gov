import pandas as pd
from sodapy import Socrata


def get_client():
    client = Socrata("www.datos.gov.co", None)

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
        "sexo", 
        "estado", 
        "fuente_tipo_contagio"
    ]
    filtered_df = results_df[columns_to_display]

    return filtered_df
