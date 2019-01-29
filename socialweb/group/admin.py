from django.contrib import admin
from . import models

# Register your models here.

class GroupMembersInline(admin.TabularInline):
    model = models.GroupMember


admin.register(models.Group)