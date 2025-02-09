# -*- coding:utf-8 -*-

import re

from django import forms
from django.core.validators import RegexValidator

# Form for searching
class EventForm(forms.Form):
    course = forms.CharField(
        min_length=4, 
        max_length=7
    )
    location = forms.CharField(
        min_length=1,
        max_length=10
    )
    
class CourseForm(forms.Form):
    course = forms.CharField(
        min_length=6,
        max_length=6,
           validators=[
            RegexValidator(
                regex=re.compile(r'(^\d\w{2}\d{2}.$)', flags=re.U),
                message='Search term must be a course code!',
                code='invalid_search'
            ),
        ]
    )

class CourseCodeForm(forms.Form):
    code = forms.CharField(
        min_length=4,
        max_length=7
    )
