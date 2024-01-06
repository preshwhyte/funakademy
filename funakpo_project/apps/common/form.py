from django import forms
from .models import Slider,Gallery, News, Staff


class SlideForm(forms.ModelForm):
    class Meta:
        model=Slider
        fields='__all__'

class GalleryForm(forms.ModelForm):
    class Meta:
        model=Gallery
        fields='__all__'


class NewsForm(forms.ModelForm):
    class Meta:
        model=News
        fields='__all__'

class StaffForm(forms.ModelForm):
    class Meta:
        model=Staff
        fields='__all__'