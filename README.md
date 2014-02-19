bbus.in [![Stories in Ready](https://badge.waffle.io/vivekchand/bbus.in.png?label=ready)](https://waffle.io/vivekchand/bbus.in)
=======

BMTC Bus Route Search http://www.bbus.in/

bbus.in API:
-------------------


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
  route5: [
      {
        bus_nos: "34D, 34F, 34H, 34S, 43, 188, 188B, 314K, TR7",
        Hop: "1",
        From: "Banashankari 1st Stage/Mysore Bank Colony",
        To: "Urvashi Talkies"
      },
      {
        bus_nos: "346F",
        Hop: "2",
        From: "Urvashi Talkies",
        To: "Bande Nallasandra"
      }
  ],
  route4: [],
  route3: [],
  route2: [],
  route1: []
}
```
Local Setup:
------------
```python
pip install -r requirements.txt
python manage.py runserver
```

Todo:
-----
* Show map of bus route on clicking any bus no. 
* Show timings of bus at the particualr bus stop

Thanks to:
----------
`Narasimha Datta: bbus.in is very much based on http://www.narasimhadatta.info/bmtc_query.html` 

