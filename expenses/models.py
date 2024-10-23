from django.db import models
from django.conf import settings

class Expense(models.Model):
    payer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.payer.name} - {self.description} (${self.total_amount})"

class Split(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    split_amount = models.DecimalField(max_digits=10, decimal_places=2)
    split_method = models.CharField(max_length=50)  # 'equal', 'percentage', 'exact'

    def __str__(self):
        return f"{self.user.name} owes ${self.split_amount} for {self.expense.description}"
