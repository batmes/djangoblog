from django.shortcuts import render,redirect
from . forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.
def register(request):
   form = RegisterForm(request.POST or None)
   if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
            
        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()

        login(request,newUser)
        messages.info(request,"Kayıt işlemi başarılı bir şekilde gerçekleşti..")
        return redirect("index")
   else:
    context = {"form" : form}
    return render(request,"register.html",context)
       
"""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            newUser = User(username = username)
            newUser.set_password(password)
            newUser.save()

            login(request,newUser)
            return  redirect("index")
        else:
            context = {
        "form" : form
        }
        return render(request,"register.html",context)

    else:
        form = RegisterForm()
        context = {
        "form" : form
        }
    return render(request,"register.html",context)
"""
def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username,password = password)
        #eşitlik sağlanması durumunda user değişkenine verileri atma işlemi
        if user is None: #kullanıcı yoksa
            messages.info(request,"Kullanıcı Adı veya Şifre Hatalı.")
            return render(request,"login.html",context)
        #kullanıcı varsa
        messages.success(request,"Başarıyla Giriş Yaptınız.")
        login(request,user)
        return redirect("index")
        
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Çıkış İşlemi Başarılı.")
    return redirect("index")