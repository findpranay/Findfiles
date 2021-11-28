from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from .models import Image,Video,Pdf
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm , ImageForm, VideoForm, PdfForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('image')
    else:
        form = UserCreationForm

    return render(request,'html/register.html',{'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            
            return redirect('index')

    else:
        form = AuthenticationForm
    return render(request,'html/login.html',{'form':form})


@login_required(login_url="login/")   
def index(request):
    return render(request,'html/index.html')
   

@login_required(login_url="login/")
def image(request):
    task_list = Image.objects.filter(author=request.user)
    if request.method == 'POST':
        title = request.POST['title'],
        image = request.FILES['image']
        task = Image(title=title,image=image,author=request.user)
        task.save()
        return redirect('image')
    
    return render(request,'html/main.html',{'task_list':task_list})
   

@login_required(login_url="login/")
def video(request):
    task_list = Video.objects.filter(author=request.user)
    if request.method == 'POST':
        title = request.POST['title'],
        video = request.FILES['video']
        task = Video(title=title,video=video,author=request.user)
        task.save()
        return redirect('video')
    
    return render(request,'html/video.html',{'task_list':task_list})
    

@login_required(login_url="login/")
def pdf(request):
    task_list = Pdf.objects.filter(author=request.user)
    if request.method == 'POST':
        title = request.POST['title'],
        pdf = request.FILES['pdf']
        task = Pdf(title=title,pdf=pdf,author=request.user)
        task.save()
        return redirect('pdf')
    
    return render(request,'html/pdf.html',{'task_list':task_list})
    
    
@login_required(login_url="login/")
def update(request):
    form = UserUpdateForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('login')

    return render(request,'html/update.html',{'form':form})
 

@login_required(login_url="login/")
def deleteimage(request, taskid):
    task = Image.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return redirect('image')

    return render(request,'html/delete.html',{'item':task})

def deletevideo(request, taskid):
    task = Video.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return redirect('video')

    return render(request,'html/delete.html')

def deletepdf(request, taskid):
    task = Pdf.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return redirect('pdf')

    return render(request,'html/delete.html')

def updateimage(request,id):
    task = Image.objects.get(id=id)
    form = ImageForm(request.POST or None, request.FILES ,instance=task)
    if form.is_valid():
        form.save()
        return redirect('image')

    return render(request,'html/update.html',{'form':form,'task':task})


def updatevideo(request,id):
    task = Video.objects.get(id=id)
    form = VideoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('video')

    return render(request,'html/update.html',{'form':form,'task':task})


def updatepdf(request,id):
    task = Pdf.objects.get(id=id)
    form = PdfForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('pdf')

    return render(request,'html/update.html',{'form':form,'task':task})





def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')


