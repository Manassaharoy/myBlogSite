from django.http import HttpResponse, response
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

def Index(request):
    return HttpResponseRedirect(reverse('App_Blog:blog_list'))