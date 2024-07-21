# JSON to SQL
# Min Chan
# Updated 7/7/2024

import json
import sqlite3

db_name = 'session_2.db'
conn = sqlite3.connect(db_name)
c = conn.cursor()
c.execute('DROP TABLE IF EXISTS weather_newyork')
c.execute('CREATE TABLE weather_newyork (date TEXT, mean_temp INT, precip FLOAT, events TEXT)')

fh = open('weather_newyork_dod.json')
dod = json.load(fh)

for row in dod:
    idict = dod[row]
    query = 'INSERT INTO weather_newyork VALUES (?,?,?,?)'
    c.execute(query,(row, idict['mean_temp'], idict['precip'], idict['events']))
conn.commit()
conn.close()

print('Hello, world')

