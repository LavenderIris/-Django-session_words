from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime
from django.contrib import messages

from .models import *

def index(request):
    data = Description.objects.all()
    courses = Course.objects.all()
    print "data", data, 'courses', courses
   
    
    return render(request,'index.html', {"courses": Course.objects.all() })

def add(request):
    if request.method == 'POST':
        c_errors = Course.objects.basic_validator(request.POST)
        d_errors = Description.objects.basic_validator(request.POST)
        print "Errors", c_errors, d_errors
        if len(c_errors)  | len(d_errors):
            print "in errors place" 
            for tag, error in c_errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            for tag, error in d_errors.iteritems():
                messages.error(request, error, extra_tags=tag)
        else:
            myrequest = request.POST
            mycourse = Course.objects.create(name = myrequest['name'])
            mycourse.save()
            d = Description.objects.create(course = mycourse, desc=myrequest['desc'])
            d.save()
    return redirect('/')

def destroy(request, id):
    print "Destroy", id
    return render(request, 'show_destroy.html',  {"course": Course.objects.get(id=id) })

def delete(request, id):
    print "Delete", id
    item = Course.objects.get(id=id)
    item.delete()

    return redirect('/')
