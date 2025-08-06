from django.contrib import admin


# Register your models here
class ConversationAdmin(admin.ModelAdmin):
    pass
    # list_display = ('message', 'created_at')
    # list_filter = ('created_at',)
    # search_fields = ('message',)
    # ordering = ('-created_at',)
    # readonly_fields = ('created_at',)
    # fieldsets = (
    #     (None, {'fields': ('message',)}),
    # )
