NextBus-JSON-API
================

The nextbus api but as JSON instead of XML. I'ts only a subset for now whilst I experiment a little. 

URL mapping
-----------

**/api/**

Returns a list of participating agencies

**/api/{agency_id}/**

Returns a list of routes for {agency_id}

**/api/{agency_id}/{route_number}/**

Returns a list of stops for {agency_id} on route {route_number}

**/api/{agency_id}/{route_number}/{stop_id}/**

Returns a list of predicted arrivals for {agency_id} on route {route_number} at stop {stop_id}

-------------

This project consumes the public xml feed provided by http://cts.cubic.com/en-us/solutions/real-timepassengerinformation/nextbus,inc.aspx which is subject to data usage limits

