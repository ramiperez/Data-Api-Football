from datetime import datetime
import db_connection
import get_data_api
import pyodbc
import json
import pandas as pd


key = open("credentials.txt", "r").read().split('\n')

driver= " ".join(map(str,key))[10:39]

server= " ".join(map(str,key))[51:73]

database=" ".join(map(str,key))[85:93]


# Recibo una función para construir el dataframe
def df_dataframe(data_field):
    df = pd.DataFrame(data_field, columns = list(data_field[0].keys()))
    return df

# Recibo un df para construir el schema de la table
def build_schema(df):
    return pd.io.json.build_table_schema(df)

# Transformación tipo datetime para campos específicos
def convert_to_date(data):
    return datetime.strptime(data, '%Y-%m-%d')

# Función para mapear tipos de datos de los campos
def schema_create_table(schema):
    fields_dt = []
    for d in schema['fields']:
        if d['type'] == 'string':
            d['type'] = 'text'
        if d['type'] == 'integer':
            d['type'] = 'bigint'
        if d['name'] == 'index':
            d['name'] = 'id'
            fields_dt.append(d['name'].lower() + ' ' +d['type'].upper() + ' IDENTITY(1,1) PRIMARY KEY' )
        if not d['name'] == 'id':
            fields_dt.append(d['name'].lower() + ' ' + d['type'].upper())    
    return fields_dt

# Función para mapear los campos en el VALUES() del INSERT INTO
def schema_insert_table(schema_):
    fields = []
    for d in schema_['fields']:
        if d['name'] == 'index':
            pass
        else:
            fields.append(d['name'].lower())
    return fields

# Función para realizar un create table en sql server
def create_table(fields_, schema, table):
    cnxn = pyodbc.connect(db_connection.connection_string(driver, server, database))
    cursor = cnxn.cursor()
    sql_create = f'CREATE TABLE {database}.{schema}.{table}(' + ', '.join(schema_create_table(fields_)) + ')'
    cursor.execute(sql_create)
    cnxn.commit()
    cursor.close()
    del cnxn
    return sql_create

# Función para realizar un insert into en sql server
def insert_data_table(fields, schema, table, df):
    cnxn = pyodbc.connect(db_connection.connection_string(driver, server, database))
    cursor = cnxn.cursor()
    data_json= json.loads(df.to_json(orient='values'))
    data_values = ", ".join(map(str, data_json))
    data_values = data_values.replace('[', '(').replace(']', ')')
    sql_insert = f'INSERT INTO {database}.{schema}.{table}(' + ', '.join(schema_insert_table(fields)) + f') VALUES{data_values}'
    cursor.execute(sql_insert)
    cnxn.commit()
    cursor.close()
    del cnxn
    return sql_insert
