from django.shortcuts import render
from customers.views import account
# Create your views here.


def account_details(request, pk):
    for i in account:
        if pk == i['acc_no']:
            acc_detail = i

    context = {
        'acc': acc_detail,
        'firstname': 'Rama Krishna'
    }
    return render(request, 'accounts/acc_details.html', context)


def transfer(request, pk):
    for i in account:
        if pk == i['acc_no']:
            acc_detail = i

    context = {
        'account': account,
        'acc': acc_detail,
        'firstname': 'Rama Krishna'
    }
    return render(request, 'accounts/transfer.html', context)


def send(request,id,rid):
    for i in account:
        if rid == i['acc_no']:
            acc_detail = i

    context = {
        'account': account,
        'acc': acc_detail,
        'firstname': 'Rama Krishna'
    }
    return render(request,'accounts/send.html',context)