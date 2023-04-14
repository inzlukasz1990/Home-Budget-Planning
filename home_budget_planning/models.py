from django.contrib.auth import get_user_model
from django.db import models

class ReceiptCategory(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Expense(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateField()
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='expense_photos/', blank=True, null=True)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, null=True)
    recurring = models.BooleanField(default=False)
    last_added = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.description} - {self.amount} on {self.date}"

class Receipt(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateField()
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='receipt_photos/', blank=True, null=True)
    category = models.ForeignKey(ReceiptCategory, on_delete=models.CASCADE, null=True)
    recurring = models.BooleanField(default=False)
    last_added = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.description} - {self.amount} on {self.date}"

