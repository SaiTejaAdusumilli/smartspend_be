from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Expense, Income
from .serializers import ExpenseSerializer, IncomeSerializer
from datetime import datetime
from django.db.models import Sum
from django.db.models import DecimalField, Value


# Income Serializer APIs

@api_view(['GET'])

def getCurrentIncome(request):
    current_date = datetime.now().strftime('%m-%Y')
    month, year = current_date.split('-')
    total_month_expenses = Expense.objects.filter(date__year=int(year), date__month=int(month)).aggregate(Sum("amount"))["amount__sum"]
    income = Income.objects.annotate(total_month_expenses=Value(total_month_expenses, output_field=DecimalField()))
    income, created = income.get_or_create(month = str(current_date))
    serializer = IncomeSerializer(income)
    return Response(serializer.data)

@api_view(['GET'])

def getSpecificIncome(request,month):
    month_inp = month
    month, year = month.split('-')
    total_month_expenses = Expense.objects.filter(date__year=int(year), date__month=int(month)).aggregate(Sum("amount"))["amount__sum"]
    income = Income.objects.annotate(total_month_expenses=Value(total_month_expenses, output_field=DecimalField()))
    income = income.get(month = month_inp)
    serializer = IncomeSerializer(income)
    return Response(serializer.data)

@api_view(['POST'])
def updateIncome(request, month):
    income = Income.objects.get(month = month)
    data = IncomeSerializer(instance=income, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response({"msg":"Error in fetching data from id"})


# Expense serializer APIs


@api_view(['GET'])

def getExpenses(request):
    expenses = Expense.objects.all()
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)

@api_view(['POST'])

def postItem(request):
    serializer = ExpenseSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateItem(request, id):
    expense = Expense.objects.get(id=id)
    data = ExpenseSerializer(instance=expense, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response({"msg":"Error in fetching data from id"})

@api_view(['DELETE'])
def deleteItem(request, id):
    item = Expense.objects.get(id=id)
    try:
        item.delete()
        return Response({"msg":"Item deleted sucessfully"})
    except Exception as  e:
        return ("Error",e)