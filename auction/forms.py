# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from auction.models import User, Brand, Category, Motorcycle, Comment, Feature
from django.utils import timezone
from datetime import timedelta


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput())


class CreateListingForm(forms.Form):
    name = forms.CharField(max_length=255)
    start_price = forms.IntegerField()
    brand = forms.ModelChoiceField(queryset=Brand.objects.all())
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    engine_capacity = forms.DecimalField()
    cylinders = forms.IntegerField()
    power = forms.DecimalField()
    torque = forms.DecimalField()
    mileage = forms.FloatField()
    top_speed = forms.IntegerField()
    fuel_capacity = forms.IntegerField()
    color = forms.ChoiceField(choices=Motorcycle.COLOR_CHOICES)
    condition = forms.ChoiceField(choices=Motorcycle.CONDITION_CHOICES)
    image_url = forms.URLField()
    summary = forms.CharField(widget=forms.Textarea)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "firstName",
            "lastName",
            "username",
            "dob",
            "mobileNo",
            "profile_picture",
            "address",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["message"]
