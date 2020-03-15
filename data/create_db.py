import sqlite3

#run this file once to create tables

conn = sqlite3.connect('tweet_manage.db')  
c = conn.cursor() # The database will be saved in the location where this 'py' file is saved

# Create table - apirelease
c.execute('''CREATE TABLE apirelease([version] varchar(30) primary key,
                                        [buildtime] date,
                                        [links] varchar2(30), [methods] varchar2(30))''')
c.execute('''CREATE TABLE users(
                                    username varchar2(30),
                                    emailid varchar2(30),
                                    password varchar2(30), full_name varchar(30),
                                    id integer primary key autoincrement)''')
          

                 
conn.commit()

# Note that the syntax to create new tables should only be used once in the code (unless you dropped the table/s at the end of the code). 
# The [generated_id] column is used to set an auto-increment ID for each record
# When creating a new table, you can add both the field names as well as the field formats (e.g., Text)

