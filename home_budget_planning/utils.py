import datetime
from .models import Expense

def add_recurring_expenses():
    today = datetime.date.today()
    first_day_of_current_month = today.replace(day=1)

    recurring_expenses = Expense.objects.filter(recurring=True)

    for expense in recurring_expenses:
        if expense.last_added < first_day_of_current_month:
            new_expense = Expense(
                user=expense.user,
                description=expense.description,
                amount=expense.amount,
                date=today,
                category=expense.category,
                recurring=True,
                last_added=today,
            )
            new_expense.save()
            expense.last_added = today
            expense.save()

