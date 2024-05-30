from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from teachapp.models import usercreate
from django.contrib import messages

def home(request):
    return render(request,'home.html')
def creates(request):
    if request.method=='POST':
        firstname=request.POST['n1']
        lastname=request.POST['n2']
        usern=request.POST['n3']
        email=request.POST['n4']
        password=request.POST['n5']
        conform_password=request.POST['n6']
        adress=request.POST['n7']
        age=request.POST['n8']
        number=request.POST['n9']
        images=request.FILES.get('n10')
        if password==conform_password:
            if User.objects.filter(username=usern).exists():
                messages.info(request,'Username Exists')
            else:
       
                user=User.objects.create_user(
                            first_name=firstname,
                            last_name=lastname,
                            username=usern,
                            email=email,
                            password=password)
                user.save()
                tech=usercreate(address=adress,age=age,number=number,image=images)
                tech.user=user
                tech.save()
        else:
            messages.info(request,'Passsword doesnt match!')
    return redirect('/')
        


