from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ImageForm,UserForm
# Create your views here.
def home(request):
    return render(request, 'users/index.html')
    
def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request,'users/index.html',{'form':form,'img_obj':img_obj})
    else:
        form = ImageForm()
    return render(request,'users/index.html',{'form':form})


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your account has been created successfully')
            return redirect('login')
    else:
        form = UserForm()
    context = {'form': form}
    return render(request,'users/register.html',context)


