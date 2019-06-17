#************* Importing Libraries *************#
from tkinter import *
import math
import tkinter
import array
#***********************************************#

#************* Process Function ****************#
def proces():
    source = Entry.get(E1)
    destination = Entry.get(E2)
    radius = 6378.1
    flag = 0

    start = ["Chennai","Madurai","Bangalore","Mumbai","Delhi","Carlsbad","London","Singapore","Tokyo","Wellington"]
    end = ["Chennai","Madurai","Bangalore","Mumbai","Delhi","Carlsbad","London","Singapore","Tokyo","Wellington"]
    latitude = array.array('f',[13.0827,9.9252,12.9716,19.0760,28.7041,33.1581,51.5074,1.3521,35.6762,139.6503])
    longitude = array.array('f',[80.2707,78.1198,77.5946,72.8777,77.1025,117.3506,0.1278,103.8198,41.2865,174.7762])

    for index in range(len(start)):
        if start[index].lower() == source.lower():
            flag = flag + 1
            lat1 = latitude[index] 
            long1 = longitude[index]

        if end[index].lower() == destination.lower():
            flag = flag + 1
            lat2 = latitude[index] 
            long2 = longitude[index]         
    if flag==2:
        lat1 = lat1 * math.pi /180;
        lat2 = lat2 * math.pi /180;

        dlat = lat2 - lat1;
        dlong = (long2 - long1) * math.pi /180;
        dlat = dlat/2    
        dlong = dlong/2

        term = ( pow(math.sin(dlat),2) ) + ( pow(math.sin(dlong),2) * math.cos(lat1) * math.cos(lat2) )
        distance = 2 * radius * math.asin(math.sqrt(term))
        E3.delete(0,END)
        Entry.insert(E3,0,distance)
    else:
        E3.delete(0,END)
        Entry.insert(E3,0,"Invalid Option")
#***********************************************#

#************ Creating GUI *********************#
window = tkinter.Tk()                              #Creating Window
window.title('Haversine Calculator')
                                                   #Labels of Entries
L1 = Label(window,text="Locations:",font='Arial,25,Bold')
L1.grid(row=0,column=0,sticky=W)
L2 = Label(window,text="Chennai   Madurai Bangalore Mumbai Delhi")
L2.grid(row=1,column=0,columnspan=2,sticky=W)
L3 = Label(window,text="Carlsbad  London  Singapore  Tokyo   Wellington")
L3.grid(row=2,column=0,columnspan=2,sticky=W)
L4 = Label(window,text="Enter the Source",font='Arial,25,Bold')     
L4.grid(row=3,column=0,sticky=W)
L5 = Label(window,text="Enter the Destination",font='Arial,25,Bold')
L5.grid(row=4,column=0,sticky=W)
L6 = Label(window,text="Distance (in KM)",fg='Blue',font='Arial,25,Bold')
L6.grid(row=5,column=0,sticky=W)

E1 = Entry(window,bd=5)                            #Entries for Inputs
E1.grid(row=3,column=1)
E2 = Entry(window,bd=5)
E2.grid(row=4,column=1)
E3 = Entry(window,bd=5,bg='yellow',fg='Blue')
E3.grid(row=5,column=1)
                                                   #Button to submit
B = Button(window,text="Submit",bd=5,command=proces,activebackground='light green',font='Bold') 
B.grid(row=6,column=1)

window.mainloop()
#***********************************************#



























