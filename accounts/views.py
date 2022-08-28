from django.shortcuts import render
from accounts.models import Student,Officer
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers


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
            student = Student.objects.filter(email=email, password=password).values()
            # student_json = serializers.serialize('json', student)
            student_json = list(student)
            print("---------------------------------------------------------------------------------------------------------")
            print(student_json)
            print("---------------------------------------------------------------------------------------------------------")
            request.session['student'] = student_json
            return HttpResponseRedirect('ComplaintPortal/welcome.html',{
                'student': student_json
            })
        else:
            HttpResponseRedirect('accounts/loginStudent.html',{
                'error': 'Kindly check your credentials'
            })

        # return render(request, 'studentLogin.html')

def myprofile(request):
    if request.method == 'GET':
        student = request.session['student'] 
        email =  student['email']
        password = student['password']    

        stu = Student.objects.filter(email=email, password=password).values()
        student_json = serializers.serialize('json', stu)
        return render(request, 'myprofile.html', student_json)

def editprofile(request):
    if request.method == 'GET':
        student = request.session['student'] 
        email =  student['email']
        password = student['password']    

        stu = Student.objects.filter(email=email, password=password).values()
        student_json = serializers.serialize('json', stu)        
        return render(request, 'editprofile.html', student_json)
        
    elif request.method == 'PUT':

        sid = request.PUT['sid']
        name = request.PUT['name']
        phnNum = request.PUT['phnNum'] 
        room = int(request.PUT['room'])
        wing = request.PUT['wing']
        hostel = request.PUT['hostel']
        email = request.PUT['email']  
        password = request.PUT['password']

        student = Student(sid=sid, name=name, phnNum=phnNum, room=room, wing=wing, hostel=hostel, email=email, password=password)
        student.save()
        return HttpResponseRedirect('accounts/myprofile.html')

