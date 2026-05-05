from django.contrib import admin
from .models import Processor, RamMemory, StorageMemory, Display, Graphics, OperationSystem, Laptop

admin.site.register(Processor)
admin.site.register(RamMemory)
admin.site.register(StorageMemory)
admin.site.register(Display)
admin.site.register(Graphics)
admin.site.register(OperationSystem)
admin.site.register(Laptop)
