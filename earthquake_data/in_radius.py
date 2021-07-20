import math

def in_radius(long1, lat1, long2, lat2, radius):
    
    '''
    input: (long of earthquake [deg], lat of earthquake [deg], long of customer [deg], lat of customer [deg], radius [m])
    output: bool. True if distance from quake within radius. 
    '''

    R = 6378.1e3 # earth's radius

    # convert to radians
    long1_rad = long1*math.pi/180
    long2_rad = long2*math.pi/180
    lat1_rad = lat1*math.pi/180
    lat2_rad = lat2*math.pi/180

    del_long = long2_rad - long1_rad
    del_lat = lat2_rad - lat1_rad

    a = math.sin(del_lat/2)**2+math.cos(lat1_rad)*math.cos(lat2_rad)*math.sin(del_long/2)**2 # haversine formula

    c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a)) #archaversine

    distance=R*c # distance between coordinates
    
    # print(long1_rad,long2_rad,lat1_rad,lat2_rad)
    # print(del_long, del_lat)
    # print("-----------")
    # print(distance)


    print("IN RADIUS")
    return distance<=radius



