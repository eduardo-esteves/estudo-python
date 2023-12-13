from django.contrib import admin

# Register your models here.
from fusion.models import Position, Services, Team_Members


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'is_active', 'update_at')


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service', 'description', 'icone', 'is_active', 'update_at')


@admin.register(Team_Members)
class Team_MembersAdmin(admin.ModelAdmin):
    list_display = ('professional', 'job_title', 'bio', 'is_active', 'update_at')
