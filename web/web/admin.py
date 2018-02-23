from django.contrib import admin
from .models import GeneralSetting, TopicSetting
from .forms import GeneralSettingAdminForm


class GeneralSettingAdmin(admin.ModelAdmin):
    form = GeneralSettingAdminForm
    list_display = [
        'address',
        'keepalive',
        'title',
        'refresh',
        'user',
        'password',
        'client_id',
        'client_id_sub',
    ]


class TopicSettingAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'topic',
        'subscribe',
    ]
    list_display_links = ('topic',)
    ordering = ['pk']


admin.site.register(GeneralSetting, GeneralSettingAdmin)
admin.site.register(TopicSetting, TopicSettingAdmin)
