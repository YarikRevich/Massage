from django.contrib import admin
from social_django.models import UserSocialAuth
from main.models import Service, Record, VisitImage, Review, SocialLoginSettings
# Register your models here.


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Registrates Service model to Admin panel"""

    list_display = (
        "name",
        "name_de",
        "description",
        "description_de",
        "category",
        "photo",
        "price",
        "currency",
        "made_time"
    )
    list_per_page = 10

    
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    """Registrates records model to Admin panel"""

    list_display = (
        "author",
        "name",
        "description",
        "phone",
        "time",
        "status",
        "seen"
    )
    list_per_page = 10


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Registrates review model to Admin panel"""

    list_display = (
        "author",
        "review",
        "mark",
        "time"
    )
    list_per_page = 10


@admin.register(VisitImage)
class VisitImageAdmin(admin.ModelAdmin):
    """Registrates VisitImage model to Admin panel"""

    list_display = ("visit_image", )
    list_per_page = 10


@admin.register(SocialLoginSettings)
class SocialLoginAdmin(admin.ModelAdmin):
    """Registrates SocialAuth services"""

    list_display = ("service", "status")
    list_per_page = 10
