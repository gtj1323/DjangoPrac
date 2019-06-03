from django.shortcuts import render
import random

# Create your views here.
def index(request): # request는 필수인자.
    return render(request, 'index.html') # 반드시 templates 라는 폴더 안에 있어야함.

def dinner(request):
    menus = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menus)
    context = {'pick':pick}
    return render(request, 'dinner.html', context)

def hello(request, name):
    context={
        'name':name,
    }
    return render(request, 'hello.html', context)

# 자기소기 / 이름, 나이를 url로 받아서 출력.
def introduce(request, name, age):
    context={
        'name': name,
        'age': age,
    }
    return render(request, 'introduce.html', context)

# 숫자 2개를 avriable reouting 으로 받아 곱셈 결과 출력.
def times(request, num1, num2):
    res = num1 * num2
    context = {
        'num1': num1,
        'num2': num2,
        'res': res,
    }
    return render(request, 'times.html', context)

# 원의 반지름 값을 variable routing 으로 받아 원의 넓이를 출력.
def area(request, radius):
    area = radius**2 * 3.141592653589793
    context = {
        'area': area,
    }
    return render(request, 'area.html', context)
