from django.shortcuts import render

# Create your views here.

account = [
    {
        'id': 1,
        'acc_no': 443323455,
        'cust_id': '4ds564',
        'cust_name': 'Annie',
        'balance': 0,
    },
    {
        'id': 2,
        'acc_no': 443323456,
        'cust_id': '4ds565',
        'cust_name': 'Katie',
        'balance': 10000.56,
    },
    {
        'id': 3,
        'acc_no': 443323457,
        'cust_id': '4ds566',
        'cust_name': 'Ellen',
        'balance': 0,
    },
    {
        'id': 4,
        'acc_no': 443323458,
        'cust_id': '4ds567',
        'cust_name': 'Rebecca',
        'balance': 0,
    },
    {
        'id': 5,
        'acc_no': 443323459,
        'cust_id': '4ds568',
        'cust_name': 'Corine',
        'balance': 0,
    }
]


def customers(request):
    context = {'account': account}
    return render(request, 'customers/customer.html', context)
