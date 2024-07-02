from django.contrib import admin
from .models import Doctor, Patient, Appointment, PatientDischargeDetails, Location, Resource, Department


# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)

class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)


class LocationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Location, LocationAdmin)



class ResourceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Resource, ResourceAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Department, DepartmentAdmin)
