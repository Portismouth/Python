# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'gold_log' not in request.session:
        request.session['gold_log'] = []

    response = {
    }

    return render(request, 'index.html', response)

def process(request):

    if request.method == "POST":      
        if request.POST['Building'] == 'farm':
            farm_gold = random.randrange(10, 21)
            print farm_gold
            request.session['gold'] += farm_gold
            request.session['gold_log'].append("you earned "+str(farm_gold)+" farm gold!")
        elif request.POST['Building'] == 'cave':
            cave_gold = random.randrange(5, 11)
            request.session['gold'] += cave_gold
            request.session['gold_log'].append("you earned "+str(cave_gold)+" cave gold!")
        elif request.POST['Building'] == 'house':
            house_gold = random.randrange(2, 6)
            request.session['gold'] += house_gold
            request.session['gold_log'].append("you earned "+str(house_gold)+" house gold!")
        elif request.POST['Building'] == 'casino':
            casino_gold = random.randrange(-50, 50)
            request.session['gold'] += casino_gold
            if casino_gold < 0:
                request.session['gold_log'].append("you lost "+str(casino_gold)+" gold in the casino...")
            else:
                request.session['gold_log'].append("you won "+str(casino_gold)+" gold in the casino!")
        
        return redirect('/')

def reset(request):

    del request.session['gold']
    del request.session['gold_log']

    return redirect('/')
