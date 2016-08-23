
import os.path
import datetime
import re
import urllib
import urllib2
import requests
import json

from django.shortcuts import render
from django.template import Template
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt


enrolURL="https://apex.oracle.com/pls/apex/viczsaurav/iDeals/"
configURL="https://apex.oracle.com/pls/apex/viczsaurav/iDeals/"

def notify(request):
    t = get_template('home.html')
    html = t.render()
    return HttpResponse(html)

@api_view(['POST'])
def user(request): 
    if request.method == 'POST':
        try:            
            data = JSONParser().parse(request)
            userid = data[0].get("userid")
            action = data[0].get("action")
            print data, userid, action

            # Contact Enroll app to fetch userData
            getUserDataFromEnrolURL = enrolURL+"getuser/"+ str(userid)
            print "Fetching User data from url: ", getUserDataFromEnrolURL
            getUserDataFromEnrolResponse = requests.get(getUserDataFromEnrolURL)
            userData = getUserDataFromEnrolResponse.json()
            print "User Data: ", userData['items']

            # # Contact Config app to fetch User Preference
            getUserPrefFromConfigURL = configURL+"getuserpref/"+ str(userid) + "/" +str(action)
            print "Fetching User data from url: ", getUserPrefFromConfigURL
            getUserPrefFromConfigResponse = requests.get(getUserPrefFromConfigURL)
            userPref = getUserPrefFromConfigResponse.json()
            print "User Pref: ", userPref['items']
            return Response(True)
        except:
            return Response(False)


# def requests(request):    
#     t = get_template('compare.html')
#     html = t.render(Context({'customer':enginuity, 'post':posts}))
#     return HttpResponse(html)

# def config(request):
#     t = get_template('config.html')
#     html = t.render(Context({'customer':enginuity, 'post':posts}))
#     return HttpResponse(html)
