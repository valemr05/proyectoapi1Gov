import api.data as api
import ui.user as ui

def main():
    department, register = ui.user_input()
    client = api.get_client()
    data = api.get_data(department, register, client)
    filtered_df = api.filter_data(data)
    ui.display_data(filtered_df)
    
main()
