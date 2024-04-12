from datetime import datetime
from typing import Optional
from django.db import models

class FilterCriteria(models.Model):
    AccountNumber = models.CharField(max_length=100, null=True, blank=True)
    TransactionId = models.CharField(max_length=100, null=True, blank=True)
    TransferStatus = models.BooleanField(null=True, blank=True)
    TransactionType = models.CharField(max_length=100, null=True, blank=True)
    CommissionDate = models.DateTimeField(null=True, blank=True)
    CommissionState = models.CharField(max_length=100, null=True, blank=True)
    OpperationStartDate = models.DateTimeField(null=True, blank=True)
    OpperationEndDate = models.DateTimeField(null=True, blank=True)

class ListItem(models.Model):
    Uetr = models.CharField(max_length=100)
    AccountNumber = models.CharField(max_length=100)
    TransactionId = models.CharField(max_length=100)
    TransactionType = models.CharField(max_length=100)
    OpperationDate = models.CharField(max_length=100)
    CommissionId = models.CharField(max_length=100)
    CommissionDate = models.CharField(max_length=100)
    TransferStatus = models.BooleanField()
    CommissionApplied = models.BooleanField()
    CommissionState = models.CharField(max_length=100)
    DebitorCountry = models.CharField(max_length=100)
    FeeCode = models.CharField(max_length=100)
    CreditAmount = models.FloatField()
    CreditorIban = models.CharField(max_length=100)