from django import forms
from .models import UploadImg


class ImageForm(forms.ModelForm):
    class Meta:
        model = UploadImg
        fields =('captions','image')