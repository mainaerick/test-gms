from django.contrib import admin
from django_object_actions import DjangoObjectActions


from .models import Regions, Tenants, NameSpaces

admin.site.register(Regions)
admin.site.register(Tenants)
admin.site.register(NameSpaces)

class ConnectToHCP(DjangoObjectActions, admin.ModelAdmin):
    def connect_To_Hcp(self, request, obj):
        #connect_To_obj(obj):
        print("Import button pushed")

    changelist_actions = ('connect_To_Hcp',)