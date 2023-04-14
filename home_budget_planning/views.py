from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Expense, Receipt
from .forms import ExpenseForm, ReceiptForm
import datetime
from functools import wraps
from django.http import HttpResponseForbidden
from .models import ReceiptCategory, ExpenseCategory
from .forms import ReceiptCategoryForm, ExpenseCategoryForm
from django.db.models import Sum
from collections import defaultdict
import json

def get_monthly_balance(receipts, expenses):
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year

    total_receipts = receipts.filter(date__month=current_month, date__year=current_year).aggregate(Sum('amount'))['amount__sum'] or 0
    total_expenses = expenses.filter(date__month=current_month, date__year=current_year).aggregate(Sum('amount'))['amount__sum'] or 0

    return total_receipts - total_expenses

def administrator_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_administrator:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You do not have permission to access this page.")
    return _wrapped_view

def home(request):
    return render(request, 'home_budget_planning/home.html', {})

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expenses')
    else:
        form = ExpenseForm()
    return render(request, 'home_budget_planning/add_expense.html', {'form': form})

@login_required
def expenses(request):
    expenses = Expense.objects.filter(user=request.user)
    balance = get_monthly_balance(Receipt.objects.filter(user=request.user), expenses)

    # Calculate expense data for the general chart
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year
    general_chart_data = [0.0] * 12
    for expense in expenses.filter(date__year=current_year):
        general_chart_data[expense.date.month - 1] += float (expense.amount)

    # Calculate expense data for the category-wise chart
    expense_categories = ExpenseCategory.objects.filter(user=request.user)
    category_chart_data = defaultdict(int)
    for expense in expenses.filter(date__year=current_year):
        category_chart_data[expense.category.name] += float (expense.amount)
    category_chart_data = json.loads(json.dumps(category_chart_data))

    context = {
        'expenses': expenses,
        'balance': balance,
        'general_chart_data': general_chart_data,
        'category_chart_data': category_chart_data,
        'expense_categories': expense_categories
    }
    return render(request, 'home_budget_planning/expenses.html', context)

@login_required
def add_receipt(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST, request.FILES)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.user = request.user
            receipt.save()
            return redirect('receipts')
    else:
        form = ReceiptForm()
    return render(request, 'home_budget_planning/add_receipt.html', {'form': form})

@login_required
def receipts(request):
    now = datetime.datetime.now()
    current_month_receipts = Receipt.objects.filter(user=request.user, date__month=now.month, date__year=now.year)
    balance = get_monthly_balance(Receipt.objects.filter(user=request.user), Expense.objects.filter(user=request.user))
    return render(request, 'home_budget_planning/receipts.html', {'receipts': current_month_receipts, 'balance': balance})


@login_required
def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id, user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expenses')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'home_budget_planning/edit_expense.html', {'form': form})

@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id, user=request.user)
    expense.delete()
    return redirect('expenses')

@login_required
def edit_receipt(request, receipt_id):
    receipt = get_object_or_404(Receipt, pk=receipt_id, user=request.user)
    if request.method == 'POST':
        form = ReceiptForm(request.POST, request.FILES, instance=receipt)
        if form.is_valid():
            form.save()
            return redirect('receipts')
    else:
        form = ReceiptForm(instance=receipt)
    return render(request, 'home_budget_planning/edit_receipt.html', {'form': form})

@login_required
def delete_receipt(request, receipt_id):
    receipt = get_object_or_404(Receipt, pk=receipt_id, user=request.user)
    receipt.delete()
    return redirect('receipts')

@administrator_required
def receipt_categories(request):
    categories = ReceiptCategory.objects.all()
    return render(request, 'home_budget_planning/receipt_categories.html', {'categories': categories})

@administrator_required
def add_receipt_category(request):
    if request.method == 'POST':
        form = ReceiptCategoryForm(request.POST)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.user = request.user
            receipt.save()
            return redirect('receipt_categories')
    else:
        form = ReceiptCategoryForm()
    return render(request, 'home_budget_planning/add_receipt_category.html', {'form': form})

@administrator_required
def edit_receipt_category(request, category_id):
    category = get_object_or_404(ReceiptCategory, pk=category_id)
    if request.method == 'POST':
        form = ReceiptCategoryForm(request.POST, instance=category)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.user = request.user
            receipt.save()
            return redirect('receipt_categories')
    else:
        form = ReceiptCategoryForm(instance=category)
    return render(request, 'home_budget_planning/edit_receipt_category.html', {'form': form})

@administrator_required
def delete_receipt_category(request, category_id):
    category = get_object_or_404(ReceiptCategory, pk=category_id)
    category.delete()
    return redirect('receipt_categories')

# Expense Categories Views
@administrator_required
def expense_categories(request):
    categories = ExpenseCategory.objects.all()
    return render(request, 'home_budget_planning/expense_categories.html', {'categories': categories})

@administrator_required
def add_expense_category(request):
    if request.method == 'POST':
        form = ExpenseCategoryForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_categories')
    else:
        form = ExpenseCategoryForm()
    return render(request, 'home_budget_planning/add_expense_category.html', {'form': form})

@administrator_required
def edit_expense_category(request, category_id):
    category = get_object_or_404(ExpenseCategory, pk=category_id)
    if request.method == 'POST':
        form = ExpenseCategoryForm(request.POST, instance=category)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_categories')
    else:
        form = ExpenseCategoryForm(instance=category)
    return render(request, 'home_budget_planning/edit_expense_category.html', {'form': form})

@administrator_required
def delete_expense_category(request, category_id):
    category = get_object_or_404(ExpenseCategory, pk=category_id)
    category.delete()
    return redirect('expense_categories')


