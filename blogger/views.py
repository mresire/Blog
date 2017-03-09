from django.shortcuts import render,redirect
from blogger.models import article
from django.template.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponse

# Create your views here.

def search(request):
    Title = request.POST.get('search')
    results = {}
    results['items'] = article.objects.filter(Title__icontains= Title)

    return render(request,'somewat.html',results)

#def articles(request):objects.all() })

    #return render(request,'articles.html',
    #            {'articles':article.

#def somewat(request, somewat_id=1):
    #return render(request,'article.html',
    #            {'article':article.objects.get(id=somewat_id)})

def page(request):
    results = {}
    results['items'] = article.objects.all()
    #print(results['items'])
    return render(request,'somewat.html',results)

def create(request):
    Title = request.POST.get('title')
    Body = request.POST.get('body')
    Date = request.POST.get('date')
    Author = request.POST.get('author')

    if Title and Body and Date and Author:
        updater = article(Title = Title, Body=Body, Date= Date, Author=Author)
        updater.save()
        return redirect(reverse('Page'))
    else:        
        return render(request,'articles.html')

# def search(request):
#     return HttpResponse('not Found')

def fullpage(request):
    results = {}
    results['items'] = article.objects.all()

    return render(request,'fullpage.html',results)