from django.shortcuts import render, render_to_response

def index(request):
    return render_to_response("index.html")

def work(request):
    return render_to_response('work.html')

def edu(request):
    return render_to_response('education.html')
