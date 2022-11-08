from django.shortcuts import render, redirect
from .models import Books
from . forms import BookForm

# Create your views here.
def index(request):
    book=Books.objects.all()
    context={
        'booklist' : book
    }
    return render(request,'home.html',context)

def detail(request,bookid):
    book=Books.objects.get(id=bookid)
    return render(request,'detail.html',{'book': book})

def add_book(request):

    if request.method=="POST":
        name=request.POST.get('name',)
        description=request.POST.get('description',)
        author=request.POST.get('author',)
        img=request.FILES['img']
        book=Books(name=name,description=description,author=author,img=img)
        book.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    abc=Books.objects.get(id=id)
    form=BookForm(request.POST or None ,request.FILES,instance=abc)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'abc':abc})


def delete(request,id):

    if request.method=='POST':
        book=Books.objects.get(id=id)
        book.delete()
        return redirect('/')
    return render(request,'delete.html',)