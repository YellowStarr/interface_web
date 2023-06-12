#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
@Project : Interface_web
@File :myForm.py
@Author: Azure Qiu
@Date: 2023/6/12 11:53
@Desc: 自定义组件
'''

from django import forms
from django.db import models

class CaseForm(forms.Form):

    base_url = forms.CharField(label= "BaseURL",
                               widget=forms.TextInput(attrs={"class":"form-control"}))
    case_name = forms.CharField(label= "case_name",
                               widget=forms.TextInput(attrs={"class":"form-control"}))
    url = forms.CharField(label= "url",
                               widget=forms.TextInput(attrs={"class":"form-control"}))
    method = forms.ChoiceField(choices=[(1, "get"), (2, "post")],
                               widget=forms.Select(attrs={"class":"form-control"}))
    args_json = forms.CharField(label= "args",
                               widget=forms.Textarea(attrs={"class":"form-control"}))

    '''
    class Meta:
        model = models.Case
        fields = ["case_name","base_url", "url", "method", "args_json"]
        widgets = {
            "case_name": forms.TextInput(attrs={"class":"form-control"}),
            "base_url": forms.TextInput(attrs={"class":"form-control"}),
            "url": forms.TextInput(attrs={"class":"form-control"}),
            "method": forms.Select(attrs={"class":"form-control"}),
            "args_json": forms.Textarea(attrs={"class":"form-control"})
        }
    '''