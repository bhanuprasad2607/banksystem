from django.shortcuts import render
from django.http import HttpResponseRedirect
from customers.models import CustomersModel
from django.contrib import messages
from .models import Transactions
from django.db.models import Q


def account_details(request, pk):
    customer = CustomersModel.objects.filter(id=pk).get()
    transactions = Transactions.objects.filter(
        Q(send_account=customer) | Q(recv_account=customer))

    context = {
        'acc': customer,
        'transactions': transactions,
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


# def send(request, id, rid):
#     customer = CustomersModel.objects.filter(id=id).get()
#     recv_customer = CustomersModel.objects.filter(id=rid).get()
#     if 'send' in request.POST:
#         request_amt = int(request.POST.get('amount'))

#         if request_amt <= customer.total_amt:
#             # Operation in updating the amount of sender and recevier
#             send_amt = customer.total_amt-request_amt
#             recv_amt = recv_customer.total_amt+request_amt

#             # Update the total amount in bank Details
#             send_customer = CustomersModel.objects.filter(
#                 id=id).update(total_amt=send_amt)
#             recv_customer_amt = CustomersModel.objects.filter(
#                 id=rid).update(total_amt=recv_amt)
#             transaction(customer, recv_customer, request_amt)

#         # Passing Error messages for the below cases
#         # Amount exceeded for sender total amount
#         # Cancellation of Transaction by customer
#         else:
#             messages.warning(
#                 request, 'Insufficient Balance, Please Check and try again.')
#             return HttpResponseRedirect(request.path_info)

#     if 'cancel' in request.POST:
#         return HttpResponseRedirect('transfer', args=(id,))

#     context = {
#         'send': customer,
#         'recv': recv_customer,
#     }
#     return render(request, 'accounts/send.html', context)


# def transaction(customer, recv_customer, request_amt):
#     transaction = Transactions(send_account=customer.acc_number,
#                                recv_account=recv_customer.acc_number, trans_amt=request_amt)
#     transaction.save()

def send(request, id, rid):
    customer = CustomersModel.objects.filter(id=id).get()
    print(customer.total_amt)
    recv_customer = CustomersModel.objects.filter(id=rid).get()
    print(request.POST)
    if 'send' in request.POST:

        request_amt = request.POST.get('amount')
        if request_amt != "":
            request_amt = float(request_amt)
            if request_amt <= customer.total_amt:
                transaction = Transactions(
                    send_account=customer, recv_account=recv_customer, trans_amt=request_amt)
                transaction.save()
                messages.success(
                    request, "Successfully transfered the amount,To go to customers click cancel")
                return HttpResponseRedirect(request.path_info)
                # Passing Error messages for the below cases
            # Amount exceeded for sender total amount
            # Cancellation of Transaction by customer
            else:
                messages.warning(
                    request, 'Insufficient Balance, Please Check and try again.')
                return HttpResponseRedirect(request.path_info)
        else:
            messages.warning(request, 'Please enter a valid Input')
            return HttpResponseRedirect(request.path_info)

    if 'cancel' in request.POST:
        return HttpResponseRedirect('transfer', args=(id,))

    context = {
        'send': customer,
        'recv': recv_customer,
    }
    return render(request, 'accounts/send.html', context)
