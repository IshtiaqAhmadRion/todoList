from django.shortcuts import render, redirect
from.models import Todo,Todoform

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