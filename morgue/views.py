from django.shortcuts import render


from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Gender, Corpse, Room, Next_of_kin

# Create your views here.



def Home(request):
    # doctors = Doctor.objects.all()
    return render(request, 'home.html') 


# def About(request):
#     return render(request, 'about.html') 


# def Contact(request):
#     return render(request, 'contact.html') 

def dashboard(request):
    corpses = Corpse.objects.all()
    if not request.user.is_staff:
        return redirect('login')
    
    co_of_corpses = len(corpses)

    mycontext = {
          'corpses': co_of_corpses
    }
    return render(request, 'index.html', mycontext)

def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']

        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            
            else:
                error = "yes"
        except:
            error = "yes"
    d = {"error": error}
    return render(request, 'login.html', d)


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')

    logout(request)
    return redirect('admin_login')


def view_corpse(request):
    if not request.user.is_staff:
        return redirect('login')
    cpse = Corpse.objects.all()
    d = {'corpse': cpse}
    return render(request, 'view_corpse.html', d)


def delete_corpse(request, did):
    if not request.user.is_staff:
        return redirect('login')
    corpse = Corpse.objects.get(id=did)
    corpse.delete()
    return redirect('view_corpse')


def add_corpse(request):
    error = ""
    gend = Gender.objects.all()
    next_of_kin = Next_of_kin.objects.all()
    rooms = Room.objects.all()
    if not request.user.is_staff:
        return redirect('login')

    if request.method == 'POST':
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        sex = request.POST['gender']
        date_of_death = request.POST['date']
        r = request.POST['room']
        kin_name = request.POST['kin']
        


        gender = Gender.objects.filter(gender=sex).first()
        kin = Next_of_kin.objects.filter(first_name=kin_name).first()
        room = Room.objects.filter(room_no=r).first()


        try:
            d1 = Corpse.objects.create(first_name=f_name, last_name=l_name, 
            gender=gender, next_of_kin=kin, room=room, date_of_death=date_of_death)
            d1.save()
            error = "no"
        
        except:
            error = "yes"
    d = {"error": error, "gender": gend, 'kin': next_of_kin, 'rooms': rooms}
    return render(request, 'add_corpse.html', d)



