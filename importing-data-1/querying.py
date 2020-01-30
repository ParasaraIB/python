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

# === Pandas and SQL queries ===

# import packages
from sqlalchemy import create_engine
import pandas as pd
# create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')
# execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM Album', engine)
# print head of DataFrame
print(df.head())
# open engine in context manager and store query result in df1
with engine.connect() as con :
    rs = con.execute('SELECT * FROM Album')
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()
# confirm that both methods yield the same result
print(df.equals(df1))

# === Pandas for more complex querying ===

# import packages
from sqlalchemy import create_engine
import pandas as pd
# create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')
# execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM Employee WHERE EmployeeId >= 6 ORDER BY BirthDate', engine)
# print head of DataFrame
print(df.head())

# === Relationships between tables: INNER JOIN ===

# open engine in context manager
# perform query and save the results to DataFrame: df
with engine.connect() as con :
    rs = con.execute('SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID = Artist.ArtistID')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
# print head of DataFrame df
print(df.head())

# === Filtering INNER JOIN ===

# execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000', engine)
# print head of DataFrame
print(df.head())
