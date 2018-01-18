from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render
from ulyne import models

# user_list = [
#     {"user": "jack", "pwd": "abc"},
#     {"user": "tom", "pwd": "ABC"},
# ]

def index(request):
    #return HttpResponse("hello python ")
    if request.method == 'POST':
        username = request.POST.get("userName", None)
        password = request.POST.get("password", None)
        #temp = {"user": username, "pwd": password}
        #user_list.append(temp)
        #添加到数据库
        models.UserInfo.objects.create(user= username, pwd= password)
        #print(username, password)
    #从数据库中读取数据
    userList = models.UserInfo.objects.all()

    return render(request, "index.html", {"data": userList})