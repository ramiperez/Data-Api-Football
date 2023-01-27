import get_data_api

def connection_string(driver, server, database):
    cnxn_str = (f"""Driver={driver};
                Server={server};
                Database={database};
                Trusted_Connection=yes;""")
    return cnxn_str
