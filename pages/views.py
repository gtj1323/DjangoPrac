from django.shortcuts import render
from datetime import datetime
import requests
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

def dtl_example(requset):
    menus=['짜장명', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, You need python'
    messages = ['apple', 'banana', 'cucumbr', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }
    return render(requset, 'dtl_example.html', context)

# Throw Catch (variable louting을 하지 않음.)
def throw(requset):
    return render(requset, 'throw.html')

def catch(requset):
    print(requset.GET)
    message = requset.GET.get('message')
    context={'message': message}
    return render(requset, 'catch.html', context)

# requsets, random 필요.
#ASCII ART
def artii(requset):
    return render(requset, 'artii.html')
def result(requset):
    # 1. form에서 날아온 데이터를 받느다.
    message = requset.GET.get('message')
    print(f'message={message}')
    # 2. http://artii.herokuapp.com/fonts_list로 요청을 보내 응답을 결과로 .text로 변환후 저장한다.
    req = requests.get('http://artii.herokuapp.com/fonts_list').text
    # 3. 저장한 데이터를 list 로 바꾼다.
    fonts = req.split('\n')
    # 4. List 안에 들어있는 요소(font) 하나를 선택해서 저장한다.
    font = random.choice(fonts)
    # 5. 우리가 전달한 데이터와 저장한 font를 가지고 다시 요청을 보내 해당 응답 결과를 저장한다. (.text)
    url = f'http://artii.herokuapp.com/make?text={message}&font={font}'
    artii_res = requests.get(url).text
    # 5. 최종적으로 지정한 데이터를 template로 넘겨준다.
    context = {
        'artii': artii_res,
        'url': url
    }
    return render(requset, 'result.html', context)

# POST 방식
def user_new(request):
    return render(request, 'user_new.html')
def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {
        'name': name,
        'pwd': pwd,
    }
    return render(request, 'user_create.html', context)

def static_example(request):
    return render(request, 'static_example.html')
