from django import forms

from videokit.forms import VideoField

class MediaItemCreateForm(forms.Form):
    video = VideoField()
