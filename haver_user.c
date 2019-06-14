#include<stdio.h>
#include<math.h>
void main()
{
    float lat1,lat2,long1,long2;
    //float lat1_rad,lat2_rad,long1_rad,long2_rad;
    float dlat,dlong,term,radius = 6378.1,distance;

    printf("Enter the latitude & longitude of Source: ");
    scanf("%f %f",&lat1,&long1);    
    printf("Enter the latitude & longitude of Destination: ");
    scanf("%f %f",&lat2,&long2); 
   
    lat1 = lat1 * M_PI /180;
    lat2 = lat2 * M_PI /180;

    dlat = lat2 - lat1;
    dlong = (long2 - long1) * M_PI /180;
    dlat = dlat/2; dlong = dlong/2;
    
    term = ( pow(sin(dlat),2) ) + ( pow(sin(dlong),2) * cos(lat1) * cos(lat2) );
    distance = 2 * radius * asin(sqrt(term));
    printf("%f KM\n",distance);
}     
