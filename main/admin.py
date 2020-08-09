from django.contrib import admin
from main.models import Service,Record
# Register your models here.


def test(modeladmin,request,queryset):
    modeladmin.message_user(request,"it works")

test.short_description = "TEST"


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name","description","price",)
    actions = (test,)

