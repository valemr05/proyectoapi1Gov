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

def display_verification (filtered_df, register):
    moreInfo = str(input("Desea ver la información secundaria del conjunto de datos (S: Sí / N: No): ")).upper()
    if moreInfo == "S":
        verification (filtered_df, register)
    else:
        print("Información ingresada inválida")

def verification(filtered_df, register):
    print("Column Names::",filtered_df.columns.values.tolist())
    print("Column Data Types::\n",filtered_df.dtypes)
    print("Columns with Missing Values::",filtered_df.columns[filtered_df.isnull().any()].tolist())
    missing_rows = filtered_df.isnull().any(axis=1).sum()
    print("Number of rows with Missing Values:", missing_rows)
    missing_indices = filtered_df.index[filtered_df.isnull().any(axis=1)].tolist()[0:register]
    print("Sample Indices with missing data:", missing_indices)

    print("General Stats::")
    print(filtered_df.info())
    print("Summary Stats::" )
    print(filtered_df.describe())
