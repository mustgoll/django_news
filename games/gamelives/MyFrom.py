from django import forms
from  django.forms import fields
from django.forms import widgets
from django.core.validators import RegexValidator
class FM(forms.Form):
    user=fields.CharField(max_length=10,
                         min_length=5,
                         error_messages={'required':'用户名不能为空',
                                         'min_length':'用户名长度不能小于5',
                                         'max_length':'用户名长度不能大于10',},
                         validators=[RegexValidator('[a-zA-Z]+','请输入英文')],
                          widget=widgets.TextInput(attrs={'class':'form-control','placeholder':'请输入用户名'})
                         )
    pwd=fields.CharField(max_length=12,
                         min_length=6,
                         error_messages={'required':'密码不能为空',
                                         'min_length':'用户名长度不能小于6',
                                         'max_length':'用户名长度不能大于12',},
                         validators=[RegexValidator('[0-9]+','请输入数字')],
                          widget=widgets.PasswordInput(attrs={'class':'form-control','placeholder':'请输入密码'}))
    yzm=fields.CharField(max_length=4,
                         min_length=4,
                         error_messages={'required':'验证码不能为空',
                                         'min_length':'用户名长度不能小于4',
                                         'max_length':'用户名长度不能大于4',},
                         validators=[RegexValidator('[a-zA-Z0-9]+','请输入正确验证码')],
                          widget=widgets.TextInput(attrs={'class':'form-control','placeholder':'请输入验证码'}))

class register(forms.Form):
    user=fields.CharField(max_length=10,
                         min_length=5,
                         error_messages={'required':'用户名不能为空',
                                         'min_length':'用户名长度不能小于5',
                                         'max_length':'用户名长度不能大于10',},
                         validators=[RegexValidator('[a-zA-Z]+','请输入英文')],
                          widget=widgets.TextInput(attrs={'class':'form-control','placeholder':'请输入5-10位英文'})
                         )
    pwd=fields.CharField(max_length=12,
                         min_length=6,
                         error_messages={'required':'密码不能为空',
                                         'min_length':'用户名长度不能小于6',
                                         'max_length':'用户名长度不能大于12',},
                         validators=[RegexValidator('[0-9]+','请输入数字')],
                          widget=widgets.PasswordInput(attrs={'class':'form-control','placeholder':'请输入6-12位数字'}))
