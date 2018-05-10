import glob
import os
import sys
import psycopg2

input_workspace = sys.argv[1]

print(input_workspace)
for file in glob.glob(os.path.join(input_workspace, '*.txt')):
	f = open(file).readlines()
	
	name = f[3].split(':')[1].split('-')[0].strip()
	lt = float(f[4].split(':')[1].strip())
	lg = float(f[5].split(':')[1].strip())
	altitude = int(float(f[6].split(':')[1].strip()))

	con = psycopg2.connect(host='localhost', database='meteo', user='viegas', password='')
	cur = con.cursor()
	
	sql = "INSERT INTO Station (simulated, geom) VALUES ('0', GeomFromEWKT('SRID=4674;POINT("+str(lt)+" "+str(lg)+")')) RETURNING id_station;"
	cur.execute(sql)
	id_station = cur.fetchone()[0]
	print("station: " + str(id_station))
	con.commit()

	sql = "INSERT INTO MeteoStation (name, description, station_id_station, altitude) VALUES ('"+name+"', '', "+str(id_station)+", "+str(altitude)+");"
	cur.execute(sql)
	con.commit()
	#print(file)