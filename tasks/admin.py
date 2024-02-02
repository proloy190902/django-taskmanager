from django.contrib import admin

# Register your models here.
from .models import Task
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'dueDate', 'isComplete', 'createdAt', 'updatedAt', 'priority')  # Specify which fields to display in the list view
    list_filter = ('isComplete', 'priority')  # Add filters for isComplete and priority fields
    search_fields = ('title', 'description')  # Add search functionality based on title and description
    readonly_fields = ('createdAt', 'updatedAt')  # Specify fields as read-only in admin interface

admin.site.register(Task)

