from django.contrib import admin
from .models import *
# class adminone(admin.AdminSite): #another admin
#     site_header='admin one site header'
# class moviesadmin(admin.ModelAdmin):
#     fields = '__all__'
#
# adm1=adminone(name='admone')
admin.site.register([movies_table,collections_table])