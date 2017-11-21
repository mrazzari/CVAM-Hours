from django.contrib.admin import SimpleListFilter

from log.models import Client


class FilterEntriesByClient(SimpleListFilter):

    def lookups(self, request, model_admin):
        all_entries = Client.objects.all().distinct()
        if not request.user.is_superuser:
            all_entries = all_entries.filter(project__employee__user=request.user)

        response = [(entry.id, entry.name) for entry in all_entries]

        return response

    title = u'Client'

    parameter_name = 'client'

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(project__client=self.value())
        return queryset