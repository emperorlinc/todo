from django import forms
from .models import Todo

# Create your forms here
class TodoForm(forms.ModelForm):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "id": "title-form",
        "placeholder": "Enter title"
    }))
    class Meta:
        model = Todo
        fields = "__all__"
        exclude = ["host"]
