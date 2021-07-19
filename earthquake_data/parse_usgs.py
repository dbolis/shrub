import requests
import json
import pdb
import pymysql
import dbCredentials

# Connect to DB

def updateDB(event=None, context=None):

    endpoint = dbCredentials.endpoint
    username = dbCredentials.username
    password = dbCredentials.password
    database_name = dbCredentials.database_name


    # Select the usgs ID

    connectionObject = pymysql.connect(host=endpoint, user=username, passwd=password, db=database_name)

    fetchCursor = connectionObject.cursor()
    fetchCursor.execute("SELECT usgsID FROM Earthquakes")
    idColumn = fetchCursor.fetchall()

    usgsIds=set()

    for id in idColumn:
        usgsIds.add(id[0])

    # check USGS API

    response = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson")
    geo_json = json.loads(response.content)
    earthquakes = geo_json['features']

    # Parse and update DB

    for item in earthquakes:

        # check if item exists in table
        if item["id"] not in usgsIds:

        # parse relevant properties
            print("~~~~~~~~~~~~~~~~~~~~~~~")
            usgsID = item["id"]
            print(id)
            place = item["properties"]["place"]
            print(place)
            magnitude = item["properties"]["mag"]
            print(magnitude)
            longitude = item["geometry"]["coordinates"][0]
            print(longitude)
            latitude = item["geometry"]["coordinates"][1]
            print(latitude)
            time = item["properties"]["time"]

        # update DB

            insertCursor = connectionObject.cursor()
            insertStatement = "INSERT INTO Earthquakes (usgsID,place,mag,longitude,latitude,time) VALUES (%s,%s,%s,%s,%s,%s)"
            insertCursor.execute(insertStatement,(usgsID,place,magnitude,longitude,latitude,time))
            connectionObject.commit()


