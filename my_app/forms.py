from django.db  import models
from django     import forms
from .models    import RiceviRequest



class SendRequest(forms.ModelForm):
    class Meta:
        model = RiceviRequest
        fields = "__all__"
