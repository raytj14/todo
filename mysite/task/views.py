from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

class CBView(View):
    def get(self,request):
        params = {"message":"View function:Get process"}
        return render(request,"task/index.html",params)

    def post(self,request):
        params = {"message":"View function:Post process"}
        return render(request,"task/index.html",params)       
