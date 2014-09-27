import urllib2

from django.utils import simplejson
from django.http import HttpResponse
from bs4 import BeautifulSoup


AGENCY_LIST_URL = 'http://webservices.nextbus.com/service/publicXMLFeed?command=agencyList'

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
    return HttpResponse(data, mimetype='application/json')

