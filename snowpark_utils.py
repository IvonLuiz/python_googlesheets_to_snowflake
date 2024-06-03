from config import *
from snowflake.snowpark.session import Session
from snowflake.connector.errors import OperationalError

connection_params = {
        "account": account_id,
        "user": username,
        "password": password,
        "role": role,
        "warehouse": warehouse,
        "database": database,
        "schema": schema
    }

def ConnectSession():
    print('Starting connection...')
    session = None
    
    try:
        session = Session.builder.configs(connection_params).create()
        print("Connected to Schema:", session.get_fully_qualified_current_schema())
    except OperationalError as e:
        print(f"Failed to connect to Snowflake: {e}")
    
    return session



# class Snowflake():
    
#     def __init__(self):
#         print('Starting connection...')
#         try:
#             self.session = Session.builder.configs(connection_params).create()
#             print("Connected to Schema:", self.session.get_fully_qualified_current_schema())
#         except OperationalError as e:
#             print(f"Failed to connect to Snowflake: {e}")


#     def close(self):
#         if self.session:
#             self.session.close()
    
#     def query(self, query):
#         return self.session.sql(query)
    
#     # def red(stage):
#     #     df_cab = session.read.parquet(stage)
        
#     #     return def_cab

#     def close(self):
#         self.session.close()
    
    
# def create_table(session: Session, query): 
#     # CREATE TABLE
#     create_table_query = query
    
#     session.sql(create_table_query).collect()
#     # SELECT TABLE
#     create_table_query  = f"""
#        SELECT 
#               *
#        FROM TEST_DB.TEST_SCHEMA.CALL_CENTER_COPY;
#     """
#     call_center_table = session.sql(create_table_query).collect()
#     return call_center_table