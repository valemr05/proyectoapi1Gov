def user_input():
    department = input("Ingrese el nombre del departamento que desea consultar: ").upper()
    register = int(input("Ingrese el número de registros que desea consultar: "))

    return department, register

def display_data(filtered_df):
    renamed_df = filtered_df.rename(columns={
        "ciudad_municipio_nom": " Ciudad ",
        "departamento_nom": " Departamento ",
        "edad" : "edad",
        "fuente_tipo_contagio": "Tipo de Contagio",
        "estado": "Estado",
        "recuperado": "Recuperado"
    })
    print(renamed_df)


