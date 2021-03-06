from django.contrib import admin
from .models import Membership


# Register your models here.

class MembershipAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
    )

admin.site.register(Membership, MembershipAdmin)