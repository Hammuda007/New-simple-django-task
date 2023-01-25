
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from.models import Cours
# Register your models here.
class CoursAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register (Cours,CoursAdmin)
