from datetime import datetime

from django.db import transaction

from .models import PurchaseHistory

def make_buy(who_buy, what_buy):
    if who_buy.balance < what_buy.price:
        raise(ValueError('Not enough money'))

    who_buy.balance -= what_buy.price
    who_buy.save()


def create_history(who_buy, what_buy):
    history_buy = PurchaseHistory.objects.create(
        owner=who_buy,
    )
    history_buy.save()
    history = history_buy.id
    return history


def make_history(who_buy, what_buy, history):
    one_history = PurchaseHistory.objects.filter(id=history).update(
        date_purchase=datetime.now(),
        purchase_price=what_buy.price,
        name=what_buy.name,
    )