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

    return render(request,'mainpage.html',results)


def mainpage(request):
    context = article.objects.order_by('-Date')
    results = {'items':context}
    
    return render(request,'mainpage.html',results)

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
        return render(request,'create.html')

# def search(request):
#     return HttpResponse('not Found')

def fullpage(request,article_id):
    context = article.objects.get(pk=article_id)
    contain = {'items':context}

    return render(request,'fullpage.html',contain)