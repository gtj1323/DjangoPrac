from django.urls import path, include
from . import views

urlpatterns = [ # 아래로 내려가면서 작성함.
    path('', views.index),
    # 끝에 urls 에 항상 '/'를 써야함.
    path('dinner/', views.dinner),
    path('hello/<name>/', views.hello),
    path('introduce/<name>/<age>/', views.introduce),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('area/<int:radius>/', views.area),
]
