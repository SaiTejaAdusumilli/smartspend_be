from django.urls import path
from .views import getExpenses, postItem, updateItem,deleteItem,getCurrentIncome,getSpecificIncome,updateIncome

urlpatterns=[
    path("get/", getExpenses),
    path("add/",postItem),
    path("update/<int:id>/",updateItem),
    path("delete/<int:id>/",deleteItem),
    path("income/get/",getCurrentIncome),
    path("income/get/<str:month>/",getSpecificIncome),
    path("income/update/<str:month>/",updateIncome),
]