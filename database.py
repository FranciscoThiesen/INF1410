#!/bin/python3
import sqlite3
from home import Home


def get_homes_list():
    try:
        conn = sqlite3.connect("data.db")
    except:
        print("Exception hit")
    
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT lat, long, tipo, vagas, descricao from Home
        """
    )

    rows = cursor.fetchall()

    home_lst = []
    for row in rows:
        print(row)
        h = Home(row[0], row[1], row[2], row[3], row[4])
        home_lst.append(h)
    
    return home_lst

        

if __name__=="__main__":
    get_homes_list()