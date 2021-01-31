from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.


glb = ' '
class login:

    def login(self,request):
        if request.method == 'POST':
            username = request.POST['username']
            pass1 = request.POST['password']

            au = auth.authenticate(username=username, password=pass1)

            if au is not None:
                auth.login(request, au)
                global glb
                glb = au
                return redirect('/')
            else:
                messages.info(request, 'username or password wrong')
                return redirect(login)
        else:
            return render(request, 'login.html')

    def sendname(self):
        global glb
        au=glb
        return au



log=login()#object of login class




def register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name= request.POST['last_name']
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password2']
        email = request.POST['email']

        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                print('username taken')
            elif User.objects.filter(email=email).exists():
                print('email taken')
            else:

                user = User.objects.create_user(username=username, password=pass1, email=email, first_name=first_name,
                                                last_name=last_name)
                user.save()
                print('user created')




        else:
            print('password did not match')

        return redirect('/') #redirect again to indexpage
    else:
        return render(request,'register.html')



