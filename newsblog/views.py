# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect,render_to_response
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from newsapi import NewsApiClient
from django.contrib import messages
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def index(request):
	return render_to_response('newsblog/index.html')


def mainpg(request):
    return render_to_response('newsblog/mainpg.html')

def search(request):
    if request.method=="GET":
       count=0
       var=request.GET.get('u')
       newsapi = NewsApiClient(api_key="e3af2b7c171c4a8a9101eb0c4bae5280")   
       topheadlines= newsapi.get_everything(q=var,language='en')
       articles = topheadlines['articles']
 
       desc = []
       news = []
       img = []
       link= []

       for i in range(len(articles)):
         myarticles = articles[i] 
         content=myarticles['description']
         if var in content:
           count+=1 
           news.append(myarticles['title'])
           desc.append(myarticles['description'])
           img.append(myarticles['urlToImage'])
           link.append(myarticles['url'])
        
       print (desc)
       mylist = zip(news, desc, img, link)   
       if count==0:
         return HttpResponse("No results found")
       else:
         return render(request, 'newsblog/newsource.html', context={"mylist":mylist})
        


def business(request):
    newsapi = NewsApiClient(api_key="e3af2b7c171c4a8a9101eb0c4bae5280")
    topheadlines = newsapi.get_top_headlines(category='business',language='en',country='in')
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
    link= []
    name="business"

    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        link.append(myarticles['url'])
        
    mylist = zip(news, desc, img, link)
    return render(request, 'newsblog/newsource.html', context={"mylist":mylist,"name":name})


def technical(request):
    newsapi = NewsApiClient(api_key="e3af2b7c171c4a8a9101eb0c4bae5280")
    topheadlines = newsapi.get_top_headlines(category='technology',language='en',country='in')
    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    link= []
    name="technology"

    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        link.append(myarticles['url'])
    
    mylist = zip(news, desc, img, link)
    return render(request, 'newsblog/newsource.html', context={"mylist":mylist,"name":name})



def international(request):
    newsapi = NewsApiClient(api_key="e3af2b7c171c4a8a9101eb0c4bae5280")
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
    link= []
    name= "international"

    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        link.append(myarticles['url'])
    

    mylist = zip(news, desc, img, link)
    return render(request, 'newsblog/newsource.html', context={"mylist":mylist,"name":name})



def entertainment(request):
    newsapi = NewsApiClient(api_key="e3af2b7c171c4a8a9101eb0c4bae5280")
    topheadlines = newsapi.get_top_headlines(category='entertainment',language='en',country='in')
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
    link= []
    name='entertainment'
 
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        link.append(myarticles['url'])
 
    mylist = zip(news, desc, img, link)
    return render(request, 'newsblog/newsource.html', context={"mylist":mylist,"name":name})



def sports(request):
    newsapi = NewsApiClient(api_key="e3af2b7c171c4a8a9101eb0c4bae5280")
    topheadlines = newsapi.get_top_headlines(category='sports',language='en',country='in')
    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    link= []
    name="sports"
 
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        link.append(myarticles['url'])
 
    mylist = zip(news, desc, img, link)
    return render(request, 'newsblog/newsource.html', context={"mylist":mylist,"name":name})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect('/mainpg')

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "newsblog/register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "newsblog/register.html",
                  context={"form":form})


def PostList(request):
    object_list = Post.objects.filter(status=1).order_by('-created_on')
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    return render(request,
                  'mainpg.html',
                  {'page': page,
                   'post_list': post_list})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/mainpg')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    return render(request = request,
                    template_name = "newsblog/login.html",
                    context={"form":form})    


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')

   