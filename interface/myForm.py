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
from interface.models import Case
from interface.models import interface

# class IndexForm(forms.Form):
#     index_field = forms.ModelChoiceField(queryset=interface.objects.all())

class CaseForm(forms.Form):

    base_url = forms.CharField(label= "BaseURL",
                               widget=forms.TextInput(attrs={"class":"form-control"}))
    header = forms.CharField(label= "header",
                               widget=forms.TextInput(attrs={"class":"form-control"}))
    name = forms.CharField(label= "case_name",
                               widget=forms.TextInput(attrs={"class":"form-control"}))
    url = forms.CharField(label= "url",
                               widget=forms.TextInput(attrs={"class":"form-control"}))
    method = forms.ChoiceField(choices=[(1, "get"), (2, "post")],
                               widget=forms.Select(attrs={"class":"form-control"}))
    args_json = forms.CharField(label= "args",required=False,
                               widget=forms.Textarea(attrs={"class":"form-control"}))
    assertion = forms.CharField(label= "assertion",
                               widget=forms.Textarea(attrs={"class":"form-control"}))
    # 外键使用ModelChoiceField
    interf = forms.ModelChoiceField(queryset=interface.objects.all(),
                                    widget=forms.HiddenInput)

class InterfaceModelForm(forms.ModelForm):

    class Meta:
        model = interface
        fields = ["base_url", "header", "url", "method"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 找到所有字段，
        for name, item in self.fields.items():
            item.widget.attrs = {"class":"form-control","readonly":"readonly"}

class CaseModelForm(forms.ModelForm):
    # interf = forms.ModelChoiceField(queryset=models.interface.objects.all(),
    #                                 widget={'interf':forms.HiddenInput()})
    class Meta:
        model = Case

        fields = ["case_name", "args_json", "assertion", "interf"]
        widgets = {
            "case_name": forms.TextInput(attrs={"class":"form-control"}),
            "args_json": forms.Textarea(attrs={"class":"form-control"}),
            "assertion": forms.Textarea(attrs={"class":"form-control"}),
            "interf":forms.HiddenInput()

        }




