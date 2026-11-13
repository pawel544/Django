from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import get_user_model



User = get_user_model()
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(min_length=5, max_length=50, required=True,
                             help_text='Required. Inform a valid email address.',
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(min_length=5, max_length=30, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(min_length=5, max_length=30, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(min_length=5, max_length=50, required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(min_length=5, max_length=45, required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    #role=forms.ChoiceField(min_length=5, max_length=50, required=True,
                     #    choices=User.ROLE_CHOICES, widget=forms.Select())
    class Meta:
        model = User
        fields = ( 'email', 'first_name', 'last_name', 'password1', 'password2', 'role')


class ChangePasswordForm(UserChangeForm):
    password1 = forms.CharField(min_length=5, max_length=50, required=True,)
    password2 = forms.CharField(min_length=5, max_length=45, required=True,)
    class Meta:
        model = User
        fields = ('password1', 'password2')



class LoginForm(AuthenticationForm):
    username =  forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )