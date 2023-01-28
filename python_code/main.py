from get_data_api import country_, compe_, teams_, standing_
from db_insert import *
import time
if __name__ == '__main__':
    schema_name = 'dbo'
    list_functions = [country_, compe_, teams_, standing_]

    for function in list_functions:
        build_schema_ = build_schema(df_dataframe(function.__name__))
        create_table_s = schema_create_table(build_schema_)
        insert_table_s = schema_insert_table(build_schema_)
        create_table(build_schema_, schema_name, f'{function.__name__}'.rstrip('_'))
        time.sleep(15)
        insert_data_table(build_schema_, schema_name, f'{function.__name__}'.rstrip('_'), df_dataframe(function.__name__))
        time.sleep(50)

        # build_schema_countries = build_schema(df_dataframe(country_))
        # create_table_s = schema_create_table(build_schema_countries)
        # insert_table_s = schema_insert_table(build_schema_countries)
        # create_table_db = create_table(build_schema_countries, schema_name, 'country')
        # insert_table_db = insert_data_table(build_schema_countries, schema_name, 'country', df_dataframe(country_))