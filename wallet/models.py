from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from .errors import InsufficientBalance
from accounts.models import CustomUser as User
from django.db.models.signals import post_save


Transaction_Type = (
    ('send', 'Send'),
    ('request', 'Request'),
    ('transfer', 'Transfer'),
)


class Currency(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=5)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % (self.name)

class Wallet(models.Model):
    # We should reference to the AUTH_USER_MODEL so that
    # when this module is used and a different User is used,
    # this would still work out of the box.
    #
    # See 'Referencing the User model' [1]
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, null=True, blank=True)

    # This stores the wallet's current balance. Also acts
    # like a cache to the wallet's balance as well.
    current_balance = models.FloatField(default=0.00)

    # The date/time of the creation of this wallet.
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user.email)

    def same_currency(self, wallet):
        wallet.currency == self.currency
    
    def can_send(self, amount):
        return (self.current_balance - amount) >= 0

    def sum(self, amount):
        self.current_balance += amount
        return self.save()

    def remove(self, amount):
        self.current_balance -= amount
        return self.save()

    def create_wallet(sender, instance, created, **kwargs):
        if created:
            Wallet.objects.create(user=instance)
    
    post_save.connect(create_wallet, sender=User)


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    transaction_type = models.CharField(max_length=45, choices=Transaction_Type, default='')
    amount = models.FloatField(default=0.00)
    create_date = models.DateTimeField(auto_now=True, editable=False)
    status = models.CharField(max_length=60, default='pending', blank=True)
    receiver = models.ForeignKey(Wallet, related_name='receiver', on_delete=models.PROTECT, default='')
    creator = models.ForeignKey(Wallet, related_name='creator', on_delete=models.PROTECT, default='')

    def __str__(self):
        return str(self.transaction_id)

    
    def save(self, *args, **kwargs):
        has_enough_money = self.creator.can_send(self.amount)
        same_currency = self.from_wallet.same_currency(self.to_wallet)

        if not has_enough_money:
            return {
                'error': 'Owner wallet must have enought money'
            }
        elif self.amount <= 0:
            return {
                'error': 'Amount must be positive',
            }
        elif not same_currency:
            return {'error': 'Wallets must have the same currency'}
        else:
            #  Update the amount of the wallets
            self.creator.remove(self.amount)
            self.receiver.sum(self.amount)

            return super(Transaction, self).save(*args, **kwargs)
