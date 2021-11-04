from django.shortcuts import render
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


def enter(request):
    context = {"categories": Category.objects.all()}
    return render(request, 'BetApplication/enter.html', context)


def my_bet(request):
    context = {"categories": Category.objects.all()}
    return render(request, 'BetApplication/my_bet.html', context)


def bet_place(request):
    context = {"categories": Category.objects.all()}
    return render(request, 'BetApplication/bet_place.html', context)


def index(request):
    context = {"categories": Category.objects.all()}
    for category in context['categories']:
        print(category)

    return render(request, 'BetApplication/index.html', context)
