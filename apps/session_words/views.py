from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime

def index(request):

    return render(request,'session_words/index.html')

def add_word(request):
   
    if request.method == 'POST':
        myrequest =  request.POST
        request.session['word']=myrequest['word']
        request.session['color']=myrequest['color']
        
        # special case for checking existence of key
        if 'size' in myrequest:
            request.session['size']=myrequest['size']
        else:
            request.session['size']='normal'
        
        request.session['styling'] = '{} {}'.format(request.session['color'], request.session['size'])
        
        new_word = {
            'styling': "{} {}".format(request.session['color'], request.session['size']) ,
            'word':  request.session['word'],
            'time': strftime("%b %d %Y %I:%M %p", localtime())  
            }
        
        if 'words' not in request.session:
            request.session['words']=[ new_word ]
        else :
            request.session['words'].insert(0, new_word)

    return redirect('/session_words')

def reset(request):

    if request.method=='GET':       
        request.session.clear()
    return redirect('/session_words')
