from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from wordnik import *
from collections import defaultdict
from .models import Study
import requests
import json
import os
import sys
import random
from django.utils.html import strip_tags
from threading import Timer
import threading
from django.conf import settings

apiUrl = 'http://api.wordnik.com/v4'
apiKey = 'YOUR API KEY HERE'
client = swagger.ApiClient(apiKey, apiUrl)

word_obj = ['happy', 'easy', 'cold', 'nice', 'full']
word = random.choice(word_obj)

def home(request):
	return render(request, 'my_vocab/home.html')

def index(request):
	correct = 0;
	app_id = settings.APP_ID
	app_key = settings.APP_KEY
	url = ('https://od-api.oxforddictionaries.com:443/api/v1/entries/en/' + word + '/synonyms')
	r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
	syns = json.loads(r.text)
	result = syns["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["synonyms"]	
	if request.method == 'GET':
		return render(request, 'my_vocab/index.html', {'result': result, 'word': word})
	if request.method == 'POST':
		guess = request.POST['guess']
		if not 'guessed' in request.session or not request.session['guessed']:
			request.session['guessed'] = [guess]
		else:
			saved = request.session['guessed']
			saved.append(guess)
			request.session['guessed'] = saved
		guessed = request.session.get('guessed')
		return render(request, 'my_vocab/index.html', {'result': result, 'guessed': guessed, 'word':word})

def guide(request):
	if request.method == 'GET':
		items = Study.objects.all()
		return render(request, 'my_vocab/guide.html', {'items': items})
	elif request.method == 'POST':
		current_user = request.user
		body = request.body
		data = body.decode('utf-8')
		print(data)

		app_id = 'aa279f7b'
		app_key = '1e05d959d527a13590d4bb0c60119ece'
		url = ('https://od-api.oxforddictionaries.com:443/api/v1/entries/en/' + data)
		r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
		defs = json.loads(r.text)
		def_result = defs["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]

		new_item = Study()
		new_item.word = data
		new_item.user_id = current_user.id
		new_item.saved = True
		new_item.definition = def_result
		new_item.save()
		return redirect('guide')

def delete(request, todo_id):
    item = Study.objects.get(id=study_id)
    item.delete()
    return redirect('index')

def signup(request):
    if request.method == 'GET':
    	return render(request, 'my_vocab/signup.html')
    elif request.method == 'POST':
    	username = request.POST['username']
    	password = request.POST['password']
    	firstname = request.POST['firstname']
    	lastname = request.POST['lastname']
    	try:
    		user = User.objects.create_user(username=username, password=password, first_name=firstname, last_name=lastname)
    		if user is not None:
    			return login(request)
    	except:
    		return render(request, 'my_vocab/signup.html', {'error': 'Username already exists'})

def login(request):
    if request.method == 'GET':
    	return render(request, 'my_vocab/login.html')
    elif request.method == 'POST':
    	username = request.POST['username']
    	password = request.POST['password']
    	user = auth.authenticate(username=username, password=password)
    	if user is not None:
    		auth.login(request, user)
    		return redirect('index')
    	else:
    		return render(request, 'my_vocab/login.html', {'error': 'Invalid credentials'})

def logout(request):
    auth.logout(request)
    return redirect('index')

def reset(request):
	word = random.choice(word_obj)
	request.session.flush()
	return redirect('index')






