#include<stdio.h>
#include<math.h>
void main()
{
    float lat1,lat2,long1,long2;
    float dlat,dlong,term,radius = 6378.1,distance;

    lat1 = 51.5007; long1 = 0.1246;
    lat2 = 40.6892; long2 = 74.0445;
    
    lat1 = lat1 * M_PI /180;
    lat2 = lat2 * M_PI /180;

    dlat = lat2 - lat1;
    dlong = (long2 - long1) * M_PI /180;
    dlat = dlat/2; dlong = dlong/2;
    
    term = ( pow(sin(dlat),2) ) + ( pow(sin(dlong),2) * cos(lat1) * cos(lat2) );
    distance = 2 * radius * asin(sqrt(term));
    printf("%f KM\n",distance);
}     
