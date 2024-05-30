from rest_framework import serializers
from .models import Expense, Income
class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__"

class IncomeSerializer(serializers.ModelSerializer):
    total_month_expenses = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    class Meta:
        model = Income
        fields = ["income","month","total_month_expenses"]
        # fields = "__all__"
