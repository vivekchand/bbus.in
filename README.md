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
```  
  
Example: Open below url in browser:

`http://www.bbus.in/api/v1/search/?from=Banashankari%201st%20Stage/Mysore%20Bank%20Colony&to=Bande%20Nallasandra&how=Minimum%20Number%20of%20Hops`

Sample Response:
```
{
  route4: [
    {
      bus_nos: "34, 34A, 34C, 34F, 34H, 34S, 183A, 314K, TR7",
      To: "Shanthinagar Bus Station",
      From: "Banashankari 1st Stage/Mysore Bank Colony",
      Hop: "1"
    },
    {
      bus_nos: "355E",
      To: "Bande Nallasandra",
      From: "Shanthinagar Bus Station",
      Hop: "2"
    }
  ],
  route5: [],
  route1: [],
  route2: [],
  route3: []
}
```
