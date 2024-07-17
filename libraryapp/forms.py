from django import forms
from .models import *
from django.contrib.auth.models import User
class studregform(forms.ModelForm):
    password=forms.CharField(label='Password',widget=forms.PasswordInput)
    cpassword=forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    phone=forms.IntegerField(label='Phone No',widget=forms.TextInput)
    roll_no=forms.IntegerField(label='Roll No',widget=forms.TextInput)
    register_id=forms.CharField(label='Register Id',max_length=10)
    college_name=forms.CharField(label='College Name',max_length=20)

    my_choice=(
        ('cse','CSE'),   # value to be save,Value to display in form
        ('eee','EEE'),
        ('mech','Mechanical'),
        ('civil','Civil')
    )
    department = forms.ChoiceField(label='Department', choices=my_choice)

    class Meta:
        model=User
        fields=['username','first_name','last_name','phone','email','password','cpassword','department','roll_no','register_id','college_name']

class libbookform(forms.ModelForm):
    class Meta:
        model=LibraryBookDetail
        fields=['book_name','book_img','auther','book_id','description','available_copies']


class EditProfileForm(forms.ModelForm):
    phone = forms.IntegerField(label='Phone No', widget=forms.TextInput)
    roll_no = forms.IntegerField(label='Roll No', widget=forms.TextInput)
    register_id = forms.CharField(label='Register Id', max_length=10)
    college_name = forms.CharField(label='College Name', max_length=20)

    my_choice=(('cse','CSE'),
            ('eee', 'EEE'),
            ('mech', 'Mechanical'),
            ('civil', 'Civil')
     )
    department = forms.ChoiceField(label='Department', choices=my_choice)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'email', 'department',
                  'roll_no', 'register_id', 'college_name']








class RegisterForm(forms.ModelForm):
    password=forms.CharField(label='Password',widget=forms.PasswordInput)
    cpassword=forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    phone = forms.IntegerField(label='Phone No', widget=forms.TextInput)
    age= forms.IntegerField(label='Age', widget=forms.TextInput)
    job = forms.CharField(label='Job', max_length=30)

    my_choice = (
        ('btech', 'BTECH'),  # value to be save,Value to display in form
        ('bca', 'BCA'),
        ('msc', 'MSC'),
        ('diploma', 'DIPLOMA')
    )
    higher_qualification = forms.ChoiceField(label='Higher Qualification', choices=my_choice)

    class Meta:
        model=User
        fields=['username','first_name','last_name','phone','age','password','cpassword','job','higher_qualification']


class EdituserForm(forms.ModelForm):
    phone = forms.IntegerField(label='Phone No', widget=forms.TextInput)
    age = forms.IntegerField(label='Age', widget=forms.TextInput)
    job= forms.CharField(label='Job', max_length=10)

    my_choice=(
        ('btech', 'BTECH'),  # value to be save,Value to display in form
        ('bca', 'BCA'),
        ('msc', 'MSC'),
        ('diploma', 'DIPLOMA')
    )
    higher_qualification= forms.ChoiceField(label='Higher Qualification', choices=my_choice)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'age', 'job',
                  'higher_qualification']