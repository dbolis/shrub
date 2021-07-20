import in_radius
import time
import pymysql
from dbCredentials import endpoint, username, password, database_name

def earthquake_api(long2, lat2, radius, time_start, time_end, magnitutde):

    connectionObject = pymysql.connect(host=endpoint, user=username, passwd=password, db=database_name)

    fetchCursor = connectionObject.cursor()
    fetchCursor.execute(f"SELECT mag, longitude, latitude, time FROM Earthquakes.Earthquakes WHERE time >= {time_start}")
    data = fetchCursor.fetchall()
    # row[0]: mag, row[1]: long1, row[2]: lat1, row[3]: time
    for row in data:
        if magnitutde<=row[0] and in_radius.in_radius(float(row[1]), float(row[2]), long2, lat2, radius) and time_start<=row[3]<=time_end:
            return True
    

    return False


