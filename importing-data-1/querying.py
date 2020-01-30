# === SQL queries ===

# import file directory
import os
# get information about current directory
print(os.getcwd())
# open directory in which the data is stored
os.chdir(r'D:\Data Science\Data Camp\Importing Data')
# import packages
from sqlalchemy import create_engine
import pandas as pd
# create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')
# open engine connection: con
con = engine.connect()
# perform query: rs
rs = con.execute('SELECT * FROM Album')
# save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())
# close connection
con.close()
# print head of DataFrame df
print(df.head())

# === Customizing SQL queries ===

# open engine in context manager
# perform query and save results to DataFrame: df
with engine.connect() as con :
    rs = con.execute('SELECT LastName, Title from Employee')
    df = pd.DataFrame(rs.fetchmany(3))
    df.columns = rs.keys()
# print the length of the DataFrame df
print(len(df))
# print the head of the DataFrame df
print(df.head())

# === Filtering database records using SQL's WHERE ===

# create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')
# open engine in context manager
# perform query and save results to DataFrame: df
with engine.connect() as con :
    rs = con.execute('SELECT * FROM Employee WHERE EmployeeId >= 6')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
# print the head of the DataFrame df
print(df.head())

# === Ordering SQL records with ORDER BY ===

# create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')
# open engine in context manager
with engine.connect() as con :
    rs = con.execute('SELECT * FROM Employee ORDER BY BirthDate')
    df = pd.DataFrame(rs.fetchall())
# set the DataFrame's column names
df.columns = rs.keys()
# print head of DataFrame
print(df.head())
