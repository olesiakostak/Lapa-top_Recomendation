from django.db import models

class Processor(models.Model):
    generation = models.CharField(max_length=512, verbose_name='Generation of the processor')
    core = models.CharField(max_length=256, verbose_name='Processor')

    def __str__(self):
        return f"Processor generation: {self.generation} core: {self.core}"


class RamMemory(models.Model):
    capacity = models.CharField(max_length=256, verbose_name='RAM capacity')

    def __str__(self):
        return self.capacity


class StorageMemory(models.Model):
    capacity = models.CharField(max_length=256, verbose_name='Storage capacity')

    def __str__(self):
        return self.capacity
    

class Display(models.Model):
    parameter = models.CharField(max_length=512, verbose_name='Display parameter')

    def __str__(self):
        return f"Display with parameters: {self.parameter}"


class OperationSystem(models.Model):
    name = models.CharField(max_length=256, verbose_name='OS name')

    def __str__(self):
        return f"OS: {self.name}"


class Laptop(models.Model):
    name = models.CharField(max_length=1024, verbose_name='Model name')
    price = models.IntegerField(verbose_name='Price(₹)')
    rating = models.FloatField(null=True, blank=True, verbose_name='Rating')
    processor = models.ForeignKey(Processor, on_delete=models.CASCADE)
    ram = models.ForeignKey(RamMemory, on_delete=models.CASCADE)
    storage = models.ForeignKey(StorageMemory, on_delete=models.CASCADE)
    display = models.ForeignKey(Display, on_delete=models.CASCADE)
    os = models.ForeignKey(OperationSystem, null=True, blank=True, on_delete=models.SET_NULL)
    warranty = models.IntegerField(verbose_name='Warranty (In Years)')

    def __str__(self):
        return f"Laptop model: {self.name}"
