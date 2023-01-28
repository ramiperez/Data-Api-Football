from get_data_api import country_, compe_, teams_, standing_
from db_insert import *
import time

## LLamada a funciones para poblar las bases de datos
if __name__ == '__main__':
    schema_name = 'dbo'
    list_functions = [country_(), compe_(), teams_(), standing_()]
    list_functions_2 = [country_, compe_, teams_, standing_]

    for function in zip(list_functions, list_functions_2):
        create_table(build_schema(df_dataframe(function[0])), schema_name, f'{function[1].__name__}'.rstrip('_'))
        insert_data_table(build_schema(df_dataframe(function[0])), schema_name, f'{function[1].__name__}'.rstrip('_'), df_dataframe(function[0]))