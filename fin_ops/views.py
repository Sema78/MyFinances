from datetime import datetime
from django.shortcuts import render, redirect
from .models import FinOperation
from django.views.decorators.http import require_http_methods
from .forms import FinOperationForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    finops = FinOperation.objects.all()
    
    return render(request, 'MyFinances/index.html', {'finops_today': finops,\
        'title': 'Report'})

def add_finops(request):
    submitted = False
    if request.method == 'POST':
        form = FinOperationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
            
    else:
        form = FinOperationForm
        if 'submitted' in request.GET:
            submitted = True

    form = FinOperationForm
    return render(request, 'fin_ops/add_finops.html', {'form': form, 'submitted': submitted})
    #return HttpResponse('Add Financial Operations Here')

@require_http_methods(['POST'])
def add(request):
    wallet = request.POST['wallet']
    category = request.POST['category']
    exp_or_inc = request.POST['expance or income']
    date = request.POST['date']
    sum = request.POST['sum']
    comment = request.POST['comment']
    finop = FinOperation(wallet_account = wallet, op_category=category,\
        is_expance=exp_or_inc, date=date, sum=sum, comment=comment)
    """ FinOperation.wallet_account = wallet
    FinOperation.op_category = category
    FinOperation.is_expanses = exp_or_inc
    FinOperation.date_created = date
    FinOperation.sum = sum
    FinOperation.comment = comment """
    finop.save()
    return redirect('index')
