from django.shortcuts import render
from django.http import HttpResponseRedirect
from customers.models import CustomersModel


def account_details(request, pk):
    customer = CustomersModel.objects.filter(id=pk).get()
    print(customer)
    context = {
        'acc': customer,
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


def send(request, id, rid):
    for i in account:
        if id == i['acc_no']:
            send_detail = i
        if rid == i['acc_no']:
            recv_detail = i

    if 'cancel' in request.POST:
        return HttpResponseRedirect('transfer', args=(id,))

    context = {
        'account': account,
        'send': send_detail,
        'recv': recv_detail,
        'firstname': 'Rama Krishna'
    }
    return render(request, 'accounts/send.html', context)
