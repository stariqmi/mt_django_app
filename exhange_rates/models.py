from django.db import models

# Create your models here.


class DestinationCountry(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=5)


class Operator(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=200)


class PaymentMethod(models.Model):
    method = models.CharField(max_length=100)


class ReceiveMethod(models.Model):
    method = models.CharField(max_length=100)


class SendAmount(models.Model):
    method = models.DecimalField(decimal_places=2)


class FxFee(models.Model):
    send_amount = models.ForeignKey(SendAmount)
    operator = models.ForeignKey(Operator)
    destination_country = models.ForeignKey(DestinationCountry)
    payment_method = models.ForeignKey(PaymentMethod)
    receive_method = models.ForeignKey(ReceiveMethod)
    fee= models.DecimalField(decimal_places=2)
    timestamp = models.DateTimeField()


class FxRate(models.Model):
    operator = models.ForeignKey(Operator)
    destination_country = models.ForeignKey(DestinationCountry)
    payment_method = models.ForeignKey(PaymentMethod)
    receive_method = models.ForeignKey(ReceiveMethod)
    rate = models.DecimalField(decimal_places=2)
    timestamp = models.DateTimeField()