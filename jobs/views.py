from django.shortcuts import render

from .models import Job

def home(request):
    #Get all the jobs by creating a variable jobs and setting it to job object
    jobs =  Job.objects 
    #{} is a dictionary
    return render(request, 'jobs/home.html', {'jobs':jobs}) 
    
