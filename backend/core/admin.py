from django.contrib import admin
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import Group


admin.site.site_title = gettext_lazy('ICRT')
admin.site.site_header = gettext_lazy('ICRT Radio Almacén')
admin.site.index_title = gettext_lazy("Administración")
admin.AdminSite.enable_nav_sidebar = False


# admin.site.unregister(Group)