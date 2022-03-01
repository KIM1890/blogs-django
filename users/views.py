from django.shortcuts import render,redirect
from .forms import ImageForm
# Create your views here.

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
def site(request):
    response = redirect('users')
    return response
