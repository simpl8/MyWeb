from django import forms
from captcha.fields import CaptchaField
from iyb import iybviews
# 用户登录表单


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder':'username', 'autofocus': ''
    }))
    password = forms.CharField(label="密  码", max_length=256, widget=forms.PasswordInput(attrs={
        'class': 'form-control','placeholder': "password"
    }))
    captcha = CaptchaField(label='验证码')
    
    
# 用户注册表单
class RegisterForm(forms.Form):
    gender = (
        ('male',"男"),
        ('female',"女"),
    )
    username = forms.CharField(label="用户名",max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码",max_length=256, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='验证码')


#版本信息创建表单
class VersionForm(forms.Form):
    plat = (
        ('ios','IOS'),
        ('android','Android'),
        ('PC','PC'),
    )
    drate = (
        ('需求分析','需求分析'),
        ('开发中','开发中'),
        ('开发完成','开发完成'),
    )
    trate = (
        ('需求分析','需求分析'),
        ('测试中','测试中'),
        ('测试完成','测试完成'),
    )
    #版本信息
    version_no = forms.CharField(label="版本号", max_length=64, widget=forms.TextInput(attrs={'class': 'form-control'})) 
    version_er = forms.CharField(label="负责人", max_length=64, widget=forms.TextInput(attrs={'class': 'form-control'})) 
    #功能信息
    fun_name = forms.CharField(label="功能名称", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'})) 
    dev_name = forms.CharField(label="开发人员", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'})) 
    test_name = forms.CharField(label="测试人员", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'})) 
    platform = forms.ChoiceField(label="涉及平台", choices=plat) 
    dev_rate = forms.ChoiceField(label="开发进度", choices=drate) 
    test_rate = forms.ChoiceField(label="测试进度", choices=trate) 
    remark = forms.CharField(label="问题备注", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))

#纯版本信息
class Vforms(forms.Form):
    status=(
        ('yes','是'),
        ('no','否')
    )
    v_code = forms.CharField(label='版本号', max_length=64, widget=forms.TextInput(attrs={'class': 'form-control'}))
    v_name = forms.CharField(label='负责人', max_length=64, widget=forms.TextInput(attrs={'class': 'form-control'}))
    status_info = forms.ChoiceField(label='完成状态',choices=status)

#纯功能信息
class FunctionForm(forms.Form):
    dev_status=(
        ('需求分析','需求分析'),
        ('开发中','开发中'),
        ('开发完成','开发完成')
    )
    test_status=(
        ('需求分析','需求分析'),
        ('测试中','测试中'),
        ('测试完成','测试完成')
    )
    #version = forms.CharField(label='功能名称',max_length=)
    #version_code = forms.ChoiceField(label="版本号",choices=version_code)
    function_name = forms.CharField(label='功能名称', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    function_dev = forms.CharField(label='开发', max_length=64, widget=forms.TextInput(attrs={'class': 'form-control'}))
    function_test = forms.CharField(label='测试', max_length=64, widget=forms.TextInput(attrs={'class': 'form-control'}))
    function_plat = forms.CharField(label='平台', max_length=64, widget=forms.TextInput(attrs={'class': 'form-control'}))
    dev_status = forms.ChoiceField(label='开发进度', choices=dev_status)
    test_status = forms.ChoiceField(label='测试进度', choices=test_status)
    question_remark = forms.CharField(label='问题记录', max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))