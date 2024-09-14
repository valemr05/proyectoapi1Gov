import api.data as api
import ui.user as ui
import numpy as np


def main():
    department, register = ui.user_input()
    client = api.get_client()
    data = api.get_data(department, register, client)

    #imputing missing values
    data.replace("N/A", np.nan, inplace=True)
    data = data.dropna(subset=["ciudad_municipio_nom", 
        "departamento_nom", 
        "edad", 
        "fuente_tipo_contagio",
        "estado", 
        "recuperado"])
    
    filtered_df = api.filter_data(data)
    ui.display_data(filtered_df)

main()
