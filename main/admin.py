from django.contrib import admin
from main.models import Service, Record, VisitImage
# Register your models here.


def test(modeladmin,request,queryset):
    modeladmin.message_user(request,"it works")

test.short_description = "TEST"


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Registrates Service model to Admin panel"""

    list_display = ("name","photo","description","price",)
    actions = (test,)


@admin.register(VisitImage)
class VisitImageAdmin(admin.ModelAdmin):
    """Registrates VisitImage model to Admin panel"""

    list_display = ("visit_image", )
