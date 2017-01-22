from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .money_calculator import money_made


def index(request):
    return render(request,'total_revenue/index.html')

#total revenue view
def money_view(request):
    output = money_made()
    context = {'output':output}
    return render(request,'total_revenue/seemymoney.html',context)
