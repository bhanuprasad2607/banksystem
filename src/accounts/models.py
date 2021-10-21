from django.db import models
import uuid
from customers.models import CustomersModel


class Transactions(models.Model):
    transaction_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, )
    send_id = models.ForeignKey(CustomersModel, on_delete=models.CASCADE)
    recv_id = models
