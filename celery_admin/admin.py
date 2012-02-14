from celery.execute import send_task
from django.contrib import admin
from djcelery.admin import PeriodicTaskAdmin
from djcelery.models import PeriodicTask

class ExtendedPeriodicTaskAdmin(PeriodicTaskAdmin):
    actions = PeriodicTaskAdmin.actions + ['run_task']

    def run_task(self, request, queryset):
        if request.user.is_superuser:
            for task in queryset.all():
                send_task(task.task)
            self.message = 'Tasks are running'
        else:
            self.message = 'You must be a superuser to perform this action.'
    run_task.short_description = 'Run Task'

admin.site.unregister(PeriodicTask)
admin.site.register(PeriodicTask, ExtendedPeriodicTaskAdmin)

