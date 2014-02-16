bbus.in
=======

BMTC Bus Route Search http://www.bbus.in/

bbus.in API:
------------


```
GET http://bbus.in/api/v1/search/?from={FROM_STOP}&to={TO_STOP}&how={HOW}

{FROM_STOP} & {TO_STOP} can be any of the values here:
http://bbus.in/static/bus_list.json

{HOW} can be any of the following values:

  Minimum Number of Hops
  Maximum Bus Route Availability
  Via Terminal Bus Stations Only
  Direct Routes Only
  Shortest Distance
  
  
Example try this:

GET http://www.bbus.in//api/v1/search/?from=Banashankari%201st%20Stage/Mysore%20Bank%20Colony&to=Bande%20Nallasandra&how=Minimum%20Number%20of%20Hops

```
