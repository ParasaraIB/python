# === Creating a database engine ===

# import file directory
import os
# get information about current directory
print(os.getcwd())
# open directory in which the data is stored
os.chdir(r'D:\Data Science\Data Camp\Importing Data')
# import necessary module
from sqlalchemy import create_engine
# create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# === Get information about tables in the database ===

# import necessary module
from sqlalchemy import create_engine
# create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')
# save the table names to a list: table_names
table_names = engine.table_names()
# print the table names
print(table_names)
