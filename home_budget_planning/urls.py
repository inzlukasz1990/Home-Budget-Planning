from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('expenses/', views.expenses, name='expenses'),
    path('add_receipt/', views.add_receipt, name='add_receipt'),
    path('receipts/', views.receipts, name='receipts'),
    path('edit_expense/<int:expense_id>/', views.edit_expense, name='edit_expense'),
    path('delete_expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('edit_receipt/<int:receipt_id>/', views.edit_receipt, name='edit_receipt'),
    path('delete_receipt/<int:receipt_id>/', views.delete_receipt, name='delete_receipt'),
    path('receipt_categories/', views.receipt_categories, name='receipt_categories'),
    path('add_receipt_category/', views.add_receipt_category, name='add_receipt_category'),
    path('edit_receipt_category/<int:category_id>/', views.edit_receipt_category, name='edit_receipt_category'),
    path('delete_receipt_category/<int:category_id>/', views.delete_receipt_category, name='delete_receipt_category'),
    path('expense_categories/', views.expense_categories, name='expense_categories'),
    path('add_expense_category/', views.add_expense_category, name='add_expense_category'),
    path('edit_expense_category/<int:category_id>/', views.edit_expense_category, name='edit_expense_category'),
    path('delete_expense_category/<int:category_id>/', views.delete_expense_category, name='delete_expense_category'),
]

