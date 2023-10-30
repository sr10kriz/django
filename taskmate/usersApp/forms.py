from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField() # by default, this EmailField() method comes with attribute required to true, if we dont want to make email field as mandatory, need to pass required = False attribute to EmailField(required=False) method
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    class Meta: 
        # why we use meta class here: its for configure the form fields, with which data to be saved t which database via which model.
        # Meta class is simply to provide metadata to the ModelForm or the Model class.
        # A model form has to have a model to work from, and the Meta object configures this.
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
        # this is the sequence the form should looks like
        # after creating this custom form that is inherited from the default Django UserCreationForm, we need use the CustomRegisterForm instead of UserCreationForm
        