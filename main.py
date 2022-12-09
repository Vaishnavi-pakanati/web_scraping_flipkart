from scrap import *
from my_sql import *

links=innerpage_links("div","_2kHMtA","a","_1fQZEK")

data=details(links)

db=sql_connection("localhost","root","Sri@3998","ss")

cur=db.cursor()

# cur.execute("drop table flipkart_data")

cr_qry=create_table("flipkart_data")

cur.execute(cr_qry)

for i in range(1,len(data)):
    insert_qry= "insert into flipkart_data values {0} ".format(data[i])
    cur.execute(insert_qry)


db.commit()

