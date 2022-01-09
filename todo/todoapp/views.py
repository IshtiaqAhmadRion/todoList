from django.shortcuts import render
from.models import Todo,Todoform

# Create your views here.

def HomePage(request):
    tododatas = Todo.objects.all().order_by("-id")
    content = {
        "todo": tododatas,
        "form": Todoform,
    }

    return render(request,"todoapps/index.html",{"data":content})