from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Course
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import sqlite3


@login_required
def deleteView(request):

    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    #Option 1:
    #cursor.execute("DELETE FROM credit_check_course WHERE course =:course", {"course": request.POST.get('course')})
    cursor.execute("DELETE FROM credit_check_course WHERE course = '%s'" % request.POST.get('course'))
    conn.commit()
    
    #Option 2:
    #course = Course.objects.get(course= request.POST.get('course'))
    #course.delete()

    #Fix flaw: broken access control
    #course = Course.objects.get(course= request.POST.get('course'))
    #if request.user == course.student:
    #	course.delete()

    
    return redirect('/')


@login_required
def addView(request):
        
    Course.objects.create(student=request.user, course=request.POST.get('course'), ssn=request.POST.get('ssn'))
    
    return redirect('/')


@login_required
def startView(request):
    
    courses = Course.objects.filter(student=request.user)

    return render(request, 'credit_check/index.html', {'courses': courses})
