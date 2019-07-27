from django.contrib import admin

from .models import History, Faq, Stuff, ClinicTeamMember


admin.site.register(History)
admin.site.register(Faq)
admin.site.register(Stuff)
admin.site.register(ClinicTeamMember)
