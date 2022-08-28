from django.shortcuts import render
from ComplaintPortal.models import Student
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def register(request):
    if request.method == 'GET':

        return render(request, 'registerStudent.html')

    elif request.method == 'POST':

        sid = request.POST['sid']
        name = request.POST['name']
        phnNum = request.POST['phnNum'] 
        room = int(request.POST['room'])
        wing = request.POST['wing']
        hostel = request.POST['hostel']
        email = request.POST['email']  
        password = request.POST['password']

        if Student.objects.filter(email=email).exists():
            HttpResponseRedirect('accounts/registerStudent.html',{
                'error': 'you already have the account, kindly proceed to Login page'
            })
        else:
            student = Student(sid=sid, name=name, phnNum=phnNum, room=room, wing=wing, hostel=hostel, email=email, password=password)
            student.save()
            return HttpResponseRedirect('accounts/login.html')


def login(request):
    if request.method == 'GET':

        return render(request, 'loginStudent.html')
        
    elif request.method == 'POST':

        email = request.POST['email']  
        password = request.POST['password']

        if Student.objects.filter(email=email, password=password).exists():
            stu = Student.objects.filter(email=email, password=password).values()
            return HttpResponseRedirect('ComplaintPortal/welcome.html',{
                'student': stu
            })
        else:
            HttpResponseRedirect('accounts/registerStudent.html',{
                'error': 'you already have the account, kindly proceed to Login page'
            })

        return render(request, 'studentLogin.html')
