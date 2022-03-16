from django import forms



class UserSignUpForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    re_password = forms.CharField()

    # def __init__(self, *args, **kwargs):
    #
    #
    # def save(self):
    #     pass
    #