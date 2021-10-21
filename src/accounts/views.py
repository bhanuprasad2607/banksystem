from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from customers.models import CustomersModel
from django.contrib import messages


def account_details(request, pk):
    customer = CustomersModel.objects.filter(id=pk).get()
    print(customer)
    context = {
        'acc': customer,
    }
    return render(request, 'accounts/acc_details.html', context)


def transfer(request, pk):
    customer = CustomersModel.objects.filter(id=pk).get()
    customers = CustomersModel.objects.all()
    context = {
        'account': customers,
        'acc': customer,
    }
    return render(request, 'accounts/transfer.html', context)


def send(request, id, rid):
    customer = CustomersModel.objects.filter(id=id).get()
    recv_customer = CustomersModel.objects.filter(id=rid).get()
    if 'send' in request.POST:
        request_amt = int(request.POST.get('amount'))

        if request_amt <= customer.total_amt:
            # Operation in updating the amount of sender and recevier
            send_amt = customer.total_amt-request_amt
            recv_amt = recv_customer.total_amt+request_amt

            # Update the total amount in bank Details
            send_customer = CustomersModel.objects.filter(
                id=id).update(total_amt=send_amt)
            recv_customer_amt = CustomersModel.objects.filter(
                id=rid).update(total_amt=recv_amt)

        # Passing Error messages for the below cases
        # Amount exceeded for sender total amount
        # Cancellation of Transaction by customer
        else:
            messages.warning(
                request, 'Insufficient Balance, Please Check and try again.')
            return HttpResponseRedirect(request.path_info)

    if 'cancel' in request.POST:
        return HttpResponseRedirect('transfer', args=(id,))

    context = {
        'send': customer,
        'recv': recv_customer,
    }
    return render(request, 'accounts/send.html', context)
