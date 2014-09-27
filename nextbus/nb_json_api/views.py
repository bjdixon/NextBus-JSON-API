import urllib2

from django.utils import simplejson
from django.http import HttpResponse
from bs4 import BeautifulSoup

FEED_URL = 'http://webservices.nextbus.com/service/publicXMLFeed'
AGENCY_LIST_URL = FEED_URL + '?command=agencyList'
ROUTE_LIST_URL = FEED_URL + '?command=routeList'
STOP_LIST_URL = FEED_URL + '?command=routeConfig'
PREDICTIONS_URL = FEED_URL + '?command=predictions'

def view_agency_list(request):
    soup = BeautifulSoup(urllib2.urlopen(AGENCY_LIST_URL).read())
    agency_list = []
    for agency in soup.find_all('agency'):
        agency_list.append({
            'title': agency['title'],
            'id': agency['tag'],
            'region': agency['regiontitle'],
            })
    data = simplejson.dumps(agency_list)
    return HttpResponse(data, content_type='application/json')

def view_routes_list(request, agency_id):
    soup = BeautifulSoup(urllib2.urlopen(ROUTE_LIST_URL + '&a=' + agency_id).read())
    route_list = []
    for route in soup.find_all('route'):
        route_list.append({
            'number': route['tag'],
            'title': route['title'].split('-')[1],
        })
    data = simplejson.dumps(route_list)
    return HttpResponse(data, content_type='application/json')

def view_stops_list(request, agency_id, route_number):
    soup = BeautifulSoup(urllib2.urlopen(
            STOP_LIST_URL + '&a=' + agency_id + '&r=' + route_number
        ).read())
    stop_list = []
    for stop in soup.route.find_all('stop'):
        try:
            stop_list.append({
                'id': stop['stopid'],
                'name': stop['title'],
            })
        except KeyError:
            # title not found so skip
            pass
    data = simplejson.dumps(stop_list)
    return HttpResponse(data, content_type='application/json')

def view_predictions(data, agency_id, route_number, stop_id):
    soup = BeautifulSoup(urllib2.urlopen(
            PREDICTIONS_URL + 
            '&a=' + agency_id +
            '&routeTag=' + route_number +
            '&stopId=' + stop_id
        ).read())
    predictions = []
    for prediction in soup.find_all('prediction'):
        predictions.append({
            'branch': prediction['branch'],
            'vehicle': prediction['vehicle'],
            'seconds': prediction['seconds'],
            'minutes': prediction['minutes'],
        })
        data = simplejson.dumps(predictions)
        return HttpResponse(data, content_type='application/json')

