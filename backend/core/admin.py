from django.contrib import admin

from .models import *

class UserRoomAdmin(admin.ModelAdmin):
    readonly_fields = ('move_in_date',)
    fields = ('user', 'move_in_date', 'move_out_date')


admin.site.register(User)
admin.site.register(Medlink)
admin.site.register(Administrator)
admin.site.register(Officer)
admin.site.register(Room)
admin.site.register(UserRoom, UserRoomAdmin)
admin.site.register(Section)
admin.site.register(SectionGRA)