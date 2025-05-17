from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
# from django.contrib.auth import authenticate, login ,logout
# from django.contrib.auth.forms  import UserCreationForm
from django.contrib import messages
from django.urls import reverse, reverse_lazy

# Create your views here.
def index(request):
    return render(request, "rbase/index.html", )

def register(request):
    page = "register"
#     form = UserCreationForm()
    context = {
         "page":page,
          # 'form': form 
    }
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
                if User.objects.filter(username=username):
                     messages.info(request, "Username already used !")
                     return redirect("register")
                elif User.objects.filter(email=email):
                     messages.info(request, "Email already used !")
                     return redirect("register")
                else:
                     user = User.objects.create_user(username=username, email=email, password=password)
                     user.save()
                     return redirect("login")

        else:
            messages.info(request, "Password did not match")
            return redirect("register")


    else:
        return render(request, "register_login.html", context)

def loginPage(request):
     page = "login"
     context = {
          "page": page,
     }

     if request.method == "POST":
          username = request.POST['username']
          password = request.POST['password']

          user = auth.authenticate(username=username, password=password)
          # also           user = authenticate(request, username=username, password=password)

          
          if user is not None:
               # login (request, user)
               auth.login(request, user)
               return redirect("/")
          
          else:
               messages.info(request, "Invalid credentials !")
               return redirect("login")

     else:
          return render(request, "register_login.html", context)
     
def logout(request):
     l = reverse('login')
     auth.logout(request)
     return redirect(l)