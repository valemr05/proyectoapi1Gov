def user_input():
    department = input("Ingrese el nombre del departamento que desea consultar: ").upper()
    register = int(input("Ingrese el número de registros que desea consultar: "))

    return department, register
def display_data(filtered_df):
    for index, row in filtered_df.iterrows():
        print("Ciudad: {0}, Departamento: {1}, Edad: {2}, Tipo de contagio: {3}, Estado: {4}, Recuperado: {5}".format(
            row['ciudad_municipio_nom'],
            row['departamento_nom'],
            row['edad'],
            row['fuente_tipo_contagio'],
            row['estado'],
            row['recuperado']
        ))
