from django import forms  # นำเข้าโมดูล forms จาก Django
from .models import Employee, Position, Project  # นำเข้าโมเดล Employee และ Position จาก models ของเรา
from datetime import date  # นำเข้าโมดูล date สำหรับตรวจสอบวันที่ปัจจุบัน
from django.forms import ModelForm, SplitDateTimeField
from django.forms.widgets import Textarea, TextInput, SplitDateTimeWidget
from django.core.exceptions import ValidationError

class EmployeeForm(ModelForm):  # ใช้ ModelForm ซึ่งเป็นฟอร์มที่เชื่อมต่อกับโมเดลใน Django
    class Meta:  # Meta เป็นคลาสภายในที่ใช้กำหนดข้อมูลของฟอร์ม
        model = Employee  # กำหนดโมเดลที่ใช้ในฟอร์มนี้ คือโมเดล Employee
        fields = ['first_name', 'last_name', 'gender', 'birth_date', 'hire_date', 'salary', 'position']
        # ระบุฟิลด์ที่จะถูกแสดงในฟอร์มจากโมเดล Employee
        widgets = {
            "birth_date" : TextInput(attrs={"type": "date"}),
            "hire_date" : TextInput(attrs={"type": "date"}),
            
        }
    gender_choices = (
        ("M", 'Male'),  
        ("F", 'Female'),  
        ("LGBT", 'LGBT'),  
    )
    
   
    gender = forms.ChoiceField(
        choices=gender_choices  
    )
    
    def clean(self):
        cleaned_data = super().clean()
        hire_date = cleaned_data.get('hire_date')  # ดึงค่าของ hire_date จากข้อมูลที่ถูกทำความสะอาดแล้ว
        if hire_date > date.today():  # ถ้า hire_date เป็นวันที่อยู่ในอนาคต
            raise forms.ValidationError("The hire date cannot be in the future.")  # ส่ง error ว่าวันที่ไม่สามารถเป็นวันในอนาคตได้
        return cleaned_data  # ถ้าวันที่ถูกต้อง ส่งคืนค่า hire_date
    
    
    # birth_date = forms.DateField(label="Birthdate", widget=forms.TextInput(attrs={"type": "date"}))
    
    
    # hire_date = forms.DateField(label="Hiredate", widget=forms.TextInput(attrs={"type": "date"}))
    
    
    # salary = forms.IntegerField(label="Salary", initial=0)
    
    
    
    
    
class ProjectForm(ModelForm):  # ใช้ ModelForm ซึ่งเป็นฟอร์มที่เชื่อมต่อกับโมเดลใน Django
    class Meta:  # Meta เป็นคลาสภายในที่ใช้กำหนดข้อมูลของฟอร์ม
        model = Project  # กำหนดโมเดลที่ใช้ในฟอร์มนี้ คือโมเดล Employee
        fields = ['name', 'manager',  'due_date', 'start_date', 'description']
        # ระบุฟิลด์ที่จะถูกแสดงในฟอร์มจากโมเดล Employee
        widgets = {
            "due_date" : TextInput(attrs={"type": "date"}),
            "start_date" : TextInput(attrs={"type": "date"}),
            "description" : Textarea(attrs={"col": 4, "row" : 4})
        }
        
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')  # ดึงค่าของ hire_date จากข้อมูลที่ถูกทำความสะอาดแล้ว
        due_date = cleaned_data.get('due_date') 
        if due_date <= start_date:  
            raise forms.ValidationError("Error ไม่ได้")  # ส่ง error ว่าวันที่ไม่สามารถเป็นวันในอนาคตได้
        return cleaned_data  # ถ้าวันที่ถูกต้อง ส่งคืนค่า hire_date

    # ฟังก์ชันนี้ใช้ตรวจสอบ hire_date ว่าจะต้องไม่เป็นวันในอนาคต
    
class ProjectDetailForm(ModelForm):  # ใช้ ModelForm ซึ่งเป็นฟอร์มที่เชื่อมต่อกับโมเดลใน Django
    class Meta:  # Meta เป็นคลาสภายในที่ใช้กำหนดข้อมูลของฟอร์ม
        model = Project  # กำหนดโมเดลที่ใช้ในฟอร์มนี้ คือโมเดล Employee
        fields = ['name', 'manager',  'due_date', 'start_date', 'description', 'staff']
        # ระบุฟิลด์ที่จะถูกแสดงในฟอร์มจากโมเดล Employee
        widgets = {
            "due_date" : TextInput(attrs={"type": "date"}),
            "start_date" : TextInput(attrs={"type": "date"}),
            "description" : Textarea(attrs={"col": 4, "row" : 4})
        }
        
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')  # ดึงค่าของ hire_date จากข้อมูลที่ถูกทำความสะอาดแล้ว
        due_date = cleaned_data.get('due_date') 
        if due_date <= start_date:  
            raise forms.ValidationError("Error ไม่ได้")  # ส่ง error ว่าวันที่ไม่สามารถเป็นวันในอนาคตได้
        return cleaned_data  # ถ้าวันที่ถูกต้อง ส่งคืนค่า hire_date