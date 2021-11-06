from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import *

# Create your views here.


def admin(request):
    context = {"categories": Category.objects.all()}
    return render(request, 'BetApplication/admin.html', context)


def rules_info(request):
    context = {"categories": Category.objects.all()}
    return render(request, 'BetApplication/rules-info.html', context)


def rules(request):
    context = {"categories": Category.objects.all()}
    return render(request, 'BetApplication/rules.html', context)


def matches(request):
    discipline = request.GET['discipline']
    matches = Match.objects.filter(
        category=Category.objects.get(name_of_category=discipline))
    for match in matches:
        print(match.first_team)
    context = {
        'matches': matches,
        'err': "",
        'discipline': discipline,
        "categories": Category.objects.all()
    }
    return render(request, 'BetApplication/matches.html', context)


def support(request):
    context = {"categories": Category.objects.all()}
    return render(request, 'BetApplication/support.html', context)


def logging_out_view(request):
    logout(request)
    return redirect("main")


def enter(request):
    context = {}
    if request.method == "POST":
        action = request.POST['action']
        if action == "register":
            if request.POST['password'] != request.POST['confirmpassword']:
                context['err'] = "Passwords are not matching!"
                return render(request, 'BetApplication/enter.html', context)
            user = User.objects.create_user(
                request.POST['email'], request.POST['fullname'], request.POST['password'])
            user.save()
            customUser = CustomUser(
                user=user, phone=request.POST['phone-number'], balance=0)
            customUser.save()
        elif action == "login":
            user = authenticate(
                username=request.POST['email'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect("main")
            else:
                context['err'] = "No user with such a login and password"
    return render(request, 'BetApplication/enter.html', context)


def my_bet(request):
    context = {"categories": Category.objects.all()}
    return render(request, 'BetApplication/my_bet.html', context)


def bet_place(request):
    match = Match.objects.get(id=int(request.GET['id']))
    context = {"categories": Category.objects.all(), 'match': match}
    return render(request, 'BetApplication/bet_place.html', context)


def index(request):
    context = {"categories": Category.objects.all()}
    for category in context['categories']:
        print(category)

    return render(request, 'BetApplication/index.html', context)
