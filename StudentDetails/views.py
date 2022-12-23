from django.shortcuts import render
from .models import StudentDetails
from .forms import InsertStudentDetails
from django.http import HttpResponseRedirect

# Create your views here.
def show(r):
    stud = StudentDetails.objects.all()
    return render(r, 'StudentDetails/show.html', {'stud':stud})

def insert(r):
    form = InsertStudentDetails()
    if r.method == 'POST':
        form = InsertStudentDetails(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return  render(r, 'StudentDetails/insert.html', {'form':form})

def update(r, id):
    stud = StudentDetails.objects.get(id=id)
    if r.method == 'POST':
        form = InsertStudentDetails(r.POST, instance = stud)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    return render(r, 'StudentDetails/update.html', {'stud':stud})

def delete(r, id):
    stud = StudentDetails.objects.get(id=id)
    stud.delete()
    return HttpResponseRedirect('/')