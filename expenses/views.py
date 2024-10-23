from django.shortcuts import render, redirect
from .forms import ExpenseForm, SplitForm
from .models import Expense, Split

def home(request):
    return render(request, 'home.html')  # Rendering a homepage template

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.payer = request.user
            expense.save()
            return redirect('split_expense', expense_id=expense.id)
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

def split_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    if request.method == 'POST':
        form = SplitForm(request.POST)
        if form.is_valid():
            method = form.cleaned_data['method']
            amounts = form.cleaned_data['amounts']
            # Process split logic here
            return redirect('view_balance_sheet')
    else:
        form = SplitForm()
    return render(request, 'split_expense.html', {'form': form, 'expense': expense})

def view_balance_sheet(request):
    '''
    user_expenses = Expense.objects.filter(payer=request.user)
    user_splits = Split.objects.filter(user=request.user)
    
    total_owed = sum(split.split_amount for split in user_splits)
    total_paid = sum(expense.total_amount for expense in user_expenses)
    
    context = {
        'total_owed': total_owed,
        'total_paid': total_paid,
        'user_expenses': user_expenses,
        'user_splits': user_splits,
    }
    return render(request, 'balance_sheet.html', context)

    '''
    return render(request, 'balance_sheet.html')
    