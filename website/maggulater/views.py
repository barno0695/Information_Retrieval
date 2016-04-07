from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect
import pickle

def processing(author_id):
	print "Processing"

def getid(request):
	return HttpResponse(request.session['id'])

def result(request, author_id):
	processing(author_id)
	request.session['id'] = author_id
	return render(request, "result.html")

def getresult(request):
	DICT = []
	with open('pickle_files/ranked_' + request.session['id'] + '.pickle', 'rb') as handle:
		DICT = pickle.load(handle)
	print DICT
	return HttpResponse(DICT)

def getallauthors(request):
	DICT = []
	with open('pickle_files/authors_dictionary.pickle', 'rb') as handle:
		DICT = pickle.load(handle)
	print DICT
	return HttpResponse(DICT)

def home(request):
	return render(request , 'home.html')
