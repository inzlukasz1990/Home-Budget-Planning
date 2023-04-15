from rest_framework import generics
from home_budget_planning.models import Expense, Receipt
from home_budget_planning.models import ReceiptCategory, ExpenseCategory
from .serializers import ReceiptSerializer, ExpenseSerializer
from .serializers import ReceiptCategorySerializer, ExpenseCategorySerializer

class ReceiptListCreateAPIView(generics.ListCreateAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

class ReceiptRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

class ExpenseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ReceiptCategoryListAPIView(generics.ListAPIView):
    queryset = ReceiptCategory.objects.all()
    serializer_class = ReceiptCategorySerializer

class ExpenseCategoryListAPIView(generics.ListAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer


