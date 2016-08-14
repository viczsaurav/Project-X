from django.shortcuts import render
from django.template import Template
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

# Create your views here.

#Static lists
enginuity = {'5875', '5876','5884','5885',} 
vendors = {'HGST', 'Toshiba','Seagate','WD',}
drives = {'AL12X','AL13X',}
capacity = {'1024','2048','3072','4096',}
firmware = {'firmware1','firmware2','firmware3','firmware4',}
run = {}
posts = [ #fake array of Posts
	{
		'author': {'nickname': 'Kathy Sierra'},
		'body'  : 'Writer of Head First Java..!!'
	},
	{
		'author': {'nickname': 'Bert Bates'},
		'body' : 'Co-author of Head First Java..!!'
	},
	]

def notify(request):
    t = get_template('home.html')
    html = t.render(Context({'enginuity':enginuity, 
    						 'vendors': vendors, 
    						 'drives': drives, 
    						 'capacity': capacity,
    						 'firmware': firmware,}))
    return HttpResponse(html)


def requests(request):    
    t = get_template('compare.html')
    html = t.render(Context({'customer':enginuity, 'post':posts}))
    return HttpResponse(html)

def config(request):
    t = get_template('config.html')
    html = t.render(Context({'customer':enginuity, 'post':posts}))
    return HttpResponse(html)
