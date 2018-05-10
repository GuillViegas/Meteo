import glob
import os
import sys
import rpy2.robjects as robjects
import psycopg2

coordinates = sys.argv[1]

robjects.r['load'](coordinates)

index = 0
for coordinate in robjects.r['coordinates'][0]:
	lt = robjects.r['coordinates'][0][index]
	lg = robjects.r['coordinates'][1][index]

	con = psycopg2.connect(host='localhost', database='meteo', user='postgres', password='123456')
	cur = con.cursor()
	
	sql = "INSERT INTO Station (simulated, geom) VALUES ('1', GeomFromEWKT('SRID=4674;POINT("+str(lt)+" "+str(lg)+")')) RETURNING id;"
	cur.execute(sql)
	id_station = cur.fetchone()[0]
	print("station: " + str(id_station))
	con.commit()
	
	index += 1

con.close()
