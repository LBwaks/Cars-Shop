from django.shortcuts import get_object_or_404
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from.models import Bid

@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        # payment was successful
        bid = get_object_or_404(Bid, id=ipn.invoice)

        # if order.total_cost() == ipn.mc_gross:
            # mark the order as paid
        bid.status = 'SOLD'
        bid.save()