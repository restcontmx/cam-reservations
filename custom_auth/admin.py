from django.contrib import admin
from .models import Rol, CustomSystemUser

# Register your models here.


class RolAdmin( admin.ModelAdmin ) :
    pass

class CustomSystemUserAdmin( admin.ModelAdmin ) :
    pass


admin.site.register( Rol, RolAdmin )
admin.site.register( CustomSystemUser, CustomSystemUserAdmin )