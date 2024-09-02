def user_input():
    department = input("Ingrese el nombre del departamento que desea consultar: ").upper()
    register = int(input("Ingrese el número de registros que desea consultar: "))

    return department, register

def display_data(filtered_df):
    for index, row in filtered_df.iterrows():
        print("Ciudad: {0}, Departamento: {1}, Edad: {2}, sexo: {3}, Estado: {4}, Tipo de contagio: {5}".format(
            row['ciudad_municipio_nom'],
            row['departamento_nom'],
            row['edad'],
            row['sexo'],
            row['estado'],
            row['fuente_tipo_contagio']
        ))