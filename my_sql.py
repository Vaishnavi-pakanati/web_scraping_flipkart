
import mysql.connector as my_sql

def sql_connection(host_name, user_name, pswd, db_name):
    db_con = my_sql.connect(
        host=host_name,
        user=user_name,
        password=pswd,
        database=db_name
    )

    return db_con


def create_table(table_name):
    create_qry="""create table if not exists  """ + table_name +""" ( name varchar(100) default NULL,rating varchar(20) default NULL,
    review varchar(50) default NULL,extra varchar(20) default NULL,price varchar(10) default NULL, link varchar(1000) default NULL)"""
    return create_qry


# def insert_data(table_name):
#     #     insert_qry='insert into '+table_name+ ' values '+ "1*"%s" for i in range(len(data[0]))]
#     insert_qry = "insert into " + table_name + " values ('%s','%s','%s','%s','%s','%s')"
#
#     return insert_qry
