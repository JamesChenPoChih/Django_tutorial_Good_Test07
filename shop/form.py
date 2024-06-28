from django.forms import ModelForm
#from django.contrib.auth.models import User
from .models import User
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm

# from django.utils.translation import ugettext_lazy as _            # 版本humble
from django.utils.translation import gettext_lazy as _




class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Password"  # 密碼
        self.fields['password2'].label = "Confirm Password"  #確認密碼
    class Meta:
        model = User
        fields = ('username','password1','password2','name','sex','phone')
        labels = {
            "username": "帳號",  # 帳號 Account
            "name":"姓名",       # 姓名 Name
            "sex":"性別",        # 性別 Gender
            "phone":"手機",      # 手機 phone 
        }

class EditForm(ModelForm):
    class Meta:
        model = User
        fields = ('name','sex','email','phone')
        labels = {
            "name":_("Name"),
            "sex":"Gender",
            "email":"E-mail",
            "phone":"Phone",
        }

    