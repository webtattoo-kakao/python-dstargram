from django.forms import fields
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django import forms


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    re_password = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


    def clean_re_password(self):        
        if self.cleaned_data['password'] != self.cleaned_data['re_password']:
            raise forms.ValidationError(' 비밀번호 값이 일치하지 않습니다. ')

        return self.cleaned_data['re_password']
        


#GET, POST
def register(request):
    
    if (request.method == 'POST'):
        #DB에 저장
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {
                'new_user': new_user
            })
            
    else:
        user_form = RegisterForm()

    return render(request, 'registration/register.html', {
        'form': user_form
    })