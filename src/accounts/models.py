from django.db import models
import uuid


class Transactions(models.Model):
    transaction_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    send_account = models.BigIntegerField(null=True)
    recv_account = models.BigIntegerField(null=True)
    trans_amt = models.BigIntegerField(null=True)
    trans_date_time = models.DateTimeField(auto_now=True)
