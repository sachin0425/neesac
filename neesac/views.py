from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    nstext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    if removepunc == 'on':
        punctuations = '''@#$%^&*<>/?\|[]{}()'''
        analyzed = ""
        for char in nstext:
            if char not in punctuations:
                analyzed = analyzed + char


        params={'purpose':'Neesac','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse('error')
   