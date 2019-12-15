from django.shortcuts import render
from django.http import HttpResponse
from firebase import firebase

firebase = firebase.FirebaseApplication('https://nodemcu-7a435.firebaseio.com/', None)


	
# Create your views here.
def home(request):
	return render(request,'base.html')
	#return render(request,'home.html',{'name':'BENNETT UNIVERSITY PARKING AREA'})
	  

def second(request):
	#print(firebase)
	result = firebase.get('/', None)
	#print(result)
	parsed = {}
	for i in result:
		if result[i]==1:
			parsed[i] = "Occupied"
		else:
			parsed[i] = 'Free'
	return render(request,'base1.html', {'data' : parsed})


