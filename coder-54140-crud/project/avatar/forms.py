from django import forms

from . import models


class AvatarForm(forms.ModelForm):
    class Meta:
        model = models.Avatar
        fields = ["user", "imagen"]





