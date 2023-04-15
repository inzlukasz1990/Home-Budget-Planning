from rest_framework import serializers
from home_budget_planning.models import Receipt, Expense
from home_budget_planning.models import ReceiptCategory, ExpenseCategory

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ['id', 'user', 'description', 'amount', 'date', 'category']

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'user', 'description', 'amount', 'date', 'category', 'recurring', 'last_added']

class ReceiptCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptCategory
        fields = ['id', 'name']

class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = ['id', 'name']

