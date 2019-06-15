#************* Importing Libraries *************#
from tkinter import *
import math
import tkinter
#***********************************************#

#************* Process Function ****************#
def proces():
    lat1 = float(Entry.get(E1))
    long1 = float(Entry.get(E2))
    lat2 = float(Entry.get(E3))
    long2 = float(Entry.get(E4))
    radius = 6378.1

    lat1 = lat1 * math.pi /180;
    lat2 = lat2 * math.pi /180;

    dlat = lat2 - lat1;
    dlong = (long2 - long1) * math.pi /180;
    dlat = dlat/2    
    dlong = dlong/2

    term = ( pow(math.sin(dlat),2) ) + ( pow(math.sin(dlong),2) * math.cos(lat1) * math.cos(lat2) )
    distance = 2 * radius * math.asin(math.sqrt(term))
    Entry.insert(E5,0,distance)
#***********************************************#

#************ Creating GUI *********************#
window = tkinter.Tk()                              #Creating Window
window.title('Haversine Calculator')

L1 = Label(window,text="Source Co-ordinates:")     #Labels of Entries
L1.grid(row=0,column=0,sticky=W)
L2 = Label(window,text="Latitude (in deg)")
L2.grid(row=1,column=0,sticky=W)
L3 = Label(window,text="Longitude (in deg)")
L3.grid(row=2,column=0,sticky=W)
L4 = Label(window,text="Destination Co-ordinates:")
L4.grid(row=3,column=0,sticky=W)
L5 = Label(window,text="Latitude (in deg)")
L5.grid(row=4,column=0,sticky=W)
L6 = Label(window,text="Longitude (in deg)")
L6.grid(row=5,column=0,sticky=W)
L7 = Label(window,text="Distance (in KM)")
L7.grid(row=6,column=0,sticky=W)

E1 = Entry(window,bd=5)                            #Entries for Inputs
E1.grid(row=1,column=1)
E2 = Entry(window,bd=5)
E2.grid(row=2,column=1)
E3 = Entry(window,bd=5)
E3.grid(row=4,column=1)
E4 = Entry(window,bd=5)
E4.grid(row=5,column=1)
E5 = Entry(window,bd=5)
E5.grid(row=6,column=1)
                                                   #Button to submit
B = Button(window,text="Submit",bd=5,command=proces) 
B.grid(row=7,column=1)

window.mainloop()
#***********************************************#



























