from django.core.management import BaseCommand
import csv
import os
from pathlib import Path
from django.conf import settings
from recommender.models import Processor, RamMemory, StorageMemory, Display, Graphics, OperationSystem, Laptop

class Command(BaseCommand):
    help = "Import laptop data from csv into database"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to csv file with laptops')

    def handle(self, *args, **kwargs):
        file_path = kwargs['csv_file']

        # Resolve the path: accept absolute paths, project-relative paths,
        # or files inside the project's `data/` folder.
        given = Path(file_path)
        candidates = [given]
        base = Path(settings.BASE_DIR)
        if not given.is_absolute():
            candidates.append(base / given)
            candidates.append(base / 'data' / given)

        csv_path = None
        for p in candidates:
            if p.exists():
                csv_path = p
                break

        if csv_path is None:
            tried = ', '.join(str(p) for p in candidates)
            raise FileNotFoundError(f"CSV file not found. Tried: {tried}")

        with open(csv_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            counter = 0

            for row in reader:
                counter += 1

                processor_obj, _ = Processor.objects.get_or_create(
                    generation=row['Generation'],
                    core=row['Core'])
                ram_obj, _ = RamMemory.objects.get_or_create(capacity=row['Ram'])
                ssd_obj, _ = StorageMemory.objects.get_or_create(capacity=row['SSD'])
                display_obj, _ = Display.objects.get_or_create(parameter=row['Display'])
                os_obj, _ = OperationSystem.objects.get_or_create(name=row['OS'])

                rating_val = float(row['Rating']) if row['Rating'] else None
                if row['Graphics']:
                    graphics_obj, _ = Graphics.objects.get_or_create(name=row['Graphics'])
                else:
                    graphics_obj = None
                
                Laptop.objects.create(
                    name=row['Model'],
                    price=row['Price (₹)'],
                    rating = rating_val,
                    processor = processor_obj,
                    ram = ram_obj,
                    storage = ssd_obj,
                    display=display_obj,
                    graphics=graphics_obj,
                    os=os_obj,
                    warranty=row['Warranty'])

            self.stdout.write(self.style.SUCCESS(f'Downloaded {counter} laptops'))
                


