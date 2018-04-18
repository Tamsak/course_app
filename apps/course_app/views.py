# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from models import *

def index(request):
    courses = { 'courses': Course.objects.all()}
    return render(request, 'course_app/index.html', courses)
def add(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
    else:
        Course.objects.create(name=request.POST['name'],desc=request.POST['desc'])
    return redirect('/')
def remove(request,id):
    courses= { 'courses' : Course.objects.filter(id=id)}
    return render(request, 'course_app/remove.html',courses)
def delete(request,id):
    if request.POST['answer'] == "No":
        return redirect('/')
    if request.POST['answer'] == "Yes! I want to delete this":
        Course.objects.get(id=id).delete()
    return redirect('/')