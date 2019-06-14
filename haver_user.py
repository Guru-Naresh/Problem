import math

if __name__ == "__main__":

    lat1 = float(input("Enter the latitude of Source: "))
    long1 = float(input("Enter the longitude of Source: "))
    lat2 = float(input("Enter the latitude of Destination: "))
    long2 = float(input("Enter the longitude of Destination: "))
    radius = 6378.1

    lat1 = lat1 * math.pi /180;
    lat2 = lat2 * math.pi /180;

    dlat = lat2 - lat1;
    dlong = (long2 - long1) * math.pi /180;
    dlat = dlat/2    
    dlong = dlong/2

    term = ( pow(math.sin(dlat),2) ) + ( pow(math.sin(dlong),2) * math.cos(lat1) * math.cos(lat2) )
    distance = 2 * radius * math.asin(math.sqrt(term))
    print(distance,"K.M")

