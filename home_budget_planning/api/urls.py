from django.urls import path
from .views import ReceiptListCreateAPIView, ReceiptRetrieveUpdateDestroyAPIView, ExpenseListCreateAPIView, ExpenseRetrieveUpdateDestroyAPIView
from .views import ReceiptCategoryListAPIView, ExpenseCategoryListAPIView

urlpatterns = [
    path('receipts/', ReceiptListCreateAPIView.as_view(), name='receipt_api_list_create'),
    path('receipts/<int:pk>/', ReceiptRetrieveUpdateDestroyAPIView.as_view(), name='receipt_api_retrieve_update_destroy'),
    path('expenses/', ExpenseListCreateAPIView.as_view(), name='expense_api_list_create'),
    path('expenses/<int:pk>/', ExpenseRetrieveUpdateDestroyAPIView.as_view(), name='expense_api_retrieve_update_destroy'),
    path('receipt-categories/', ReceiptCategoryListAPIView.as_view(), name='receipt_category_api_list'),
    path('expense-categories/', ExpenseCategoryListAPIView.as_view(), name='expense_category_api_list'),   
]

