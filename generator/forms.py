from django import forms
from .models import MemeImage
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class MemeForm(forms.ModelForm):
    class Meta:
        model = MemeImage
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Check the file extension
            valid_extensions = ['jpg', 'jpeg', 'png', 'gif']
            print(image.name.split('.')[-1].lower())
            extension = image.name.split('.')[-1].lower()
            if extension not in valid_extensions:
                raise ValidationError(_('Invalid file format. Only JPG, JPEG, PNG, and GIF images are allowed.'))
        return image