
from .models import Idc

from django.contrib import admin

# Register your models here.

@admin.register(Idc)
class IdcAdmin(admin.ModelAdmin):

    # listdisplay 设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'name', 'email', 'phone', 'letter')

    # list_per_page 设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-id',)