from django.shortcuts import render,redirect

# Create your views here.
from BlogApp.forms import FormBlogs
from BlogApp.models import Blogs



def blogs(request):
    obj1=Blogs.objects.all()
    if request.method=='POST':
        title=request.POST.get('title')
        desc = request.POST.get('desc')

        date = request.POST.get('date')

        obj=Blogs(title=title,desc=desc,date=date)
        obj.save()
    return render(request,'blogs.html',{'obj1':obj1})
def delete(request,blogid):
    obj=Blogs.objects.get(id=blogid)
    if request.method=="POST":
        obj.delete()
        return redirect('/')
    return render(request,'delete.html',{'obj':obj})
def update(request,id):
    obj1=Blogs.objects.get(id=id)
    form=FormBlogs(request.POST or None,instance=obj1)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'obj1':obj1,'form':form})