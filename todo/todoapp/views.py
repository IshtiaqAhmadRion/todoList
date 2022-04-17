from django.shortcuts import render, redirect
from.models import Todo,Todoform
from django.http import HttpResponse

# Create your views here.

def HomePage(request):
    tododatas = Todo.objects.all().order_by("-id")
    content = {
        "todo": tododatas,
        "form": Todoform,
    }

    if request.method == "POST":
        data = request.POST
        form = Todoform(data)
        if form.is_valid():
            form.save()
            return redirect('/')
      
        return render(request,"todoapps/index.html")

    return render(request,"todoapps/index.html",{"data":content})

def Edittodo(request,id):
    try:
        tdata = Todo.objects.get(id=id)
        tdata.delete()
        return HttpResponse(f"<h1>Todo is Deleted</h1>")
    except: 
        return redirect ("/")
    return HttpResponse(f"<h1>{id}</h1>")

def Updatetodo (request,id):
    try:
        tdata = Todo.objects.get(id = id)
        return HttpResponse(f"{id}")
    except:
        return redirect("/")
    