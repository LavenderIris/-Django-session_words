from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
    return render(request,'ninja_gold/index_ninja_gold.html')

def process_money(request):
    if request.method == 'POST':
        myrequest =  request.POST
        color = 'green'
        if myrequest['building'] =='farm':
            gold_earned = random.randint(10, 20)
        elif myrequest['building'] =='cave':
            gold_earned = random.randint(5, 10)
        elif myrequest['building'] =='house':
            gold_earned = random.randint(2, 5)
        elif (myrequest['building']=="casino"):
            gold_earned = random.randint(-50, 50)
            if gold_earned<0:
                color='red'

        mytime=strftime("%Y/%m/%d %H:%M:%S", gmtime())

        if 'activity' not in request.session:
            request.session['activity']= [['Earned {} gold from the {}! ({})'.format(gold_earned, myrequest['building'], mytime), color ]]
        else:
            request.session['activity'].append(['Earned {} gold from the {}! ({})'.format(gold_earned, myrequest['building'], mytime), color])

        request.session['gold']+= gold_earned
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')