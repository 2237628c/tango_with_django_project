# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from rango.models import Category
from rango.models import Page
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages': page_list}
    
    return render(request, 'rango/index.html',  context = context_dict)
             
def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Adam Christie'}
    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        #can we find a category slug with given name
        category = Category.objects.get(slug=category_name_slug)

        #retrieve all its associated pages
        pages = Page.objects.filter(category=category)

        #adds results list to template under name pages
        context_dict['pages'] = pages

        #add category object from database to dictionary
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context_dict)
    

