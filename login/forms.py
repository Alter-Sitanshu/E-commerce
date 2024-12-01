from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Username",
        required=True,
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Your Username",
        })
    )
    email = forms.EmailField(
        max_length=120,
        required=True,
        label="Email-Address",
        widget=forms.EmailInput(attrs={
            "class":"form-control",
            "placeholder":"example@gmail.com"
        })
    )
    password = forms.CharField(
        min_length=8,
        label="Password",
        required=True,
        widget=forms.PasswordInput(attrs={
            "class":"form-control"
        })
    )
    again_password = forms.CharField(
        min_length=8,
        label="Confirm password",
        required=True,
        widget=forms.PasswordInput(attrs={
            "class":"form-control"
        })
    )
    type = forms.ChoiceField(
        required=True,
        choices=[
            ("business","Business"),
            ("normal","Normal")
        ],
        label="Account type"
    )

class LoginForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Username",
        required=True,
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Your Username",
        })
    )
    password = forms.CharField(
        min_length=8,
        label="Password",
        required=True,
        widget=forms.PasswordInput(attrs={
            "class":"form-control"
        })
    )