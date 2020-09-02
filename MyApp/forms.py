from django import forms
from .models import *


class Add_Course_form(forms.ModelForm):
    class Meta:
        model = CourseDetails
        exclude=()
        widgets = {
            "title":forms.TextInput(attrs={"placeholder":"Title"}),
            "category":forms.TextInput(attrs={"placeholder":"Category"}),
            "duration":forms.TextInput(attrs={"placeholder":"Duration"}),
            "price":forms.TextInput(attrs={"placeholder":"Director"}),
            "overview":forms.TextInput(attrs={"placeholder":"Description"}),
            "rating":forms.TextInput(attrs={"placeholder":"rating"}),
            "lectures":forms.DateInput(attrs={"placeholder":"release date"}),
            "img":forms.FileInput(),
        }

class Add_Instructor_form(forms.ModelForm):
    class Meta:
        model = Instructor
        exclude=()
        widgets = {
            "title":forms.Select(attrs={"width":"250px"}),
            "name":forms.TextInput(attrs={"placeholder":"name"}),
            "photo":forms.FileInput(),
            "about":forms.TextInput(attrs={"placeholder":"role"}),
        }

class Add_Lecture_form(forms.ModelForm):
    class Meta:
        model = LecturesModel
        exclude=()
        widgets = {
            "course":forms.Select(attrs={"width":"250px"}),
            "lect":forms.TextInput(attrs={"placeholder":"lect"}),
            "lect_number":forms.TextInput(attrs={"placeholder":"lect_number"}),
            "time":forms.TextInput(attrs={"placeholder":"time"}),
            "type":forms.TextInput(attrs={"placeholder":"type"}),
            "description":forms.TextInput(attrs={"placeholder":"description"}),
        }