from django.core.management.base import BaseCommand, CommandError
from demoapp.models import Item, TimeCapsule
from django.utils import timezone
from django.db.utils import IntegrityError

import random


class Command(BaseCommand):
    help = 'Add import data for our test data'

    def handle(self, *args, **options):
        # Example names
        FIRST_NAMES = ('John', 'Bruna', 'Jonhnatha', 'Mary', 'Alfred', 'Theresa', 'Ralph', 'Christopher', 'Laura')
        LAST_NAMES = ('McFly', 'Trigueiro', 'Pontes', 'Kasinsky', 'Santos', 'Random', 'Lauren', 'Dilling', 'Sputinik', 'Newton', 'Galilei')
        ITEM_NAMES = ('photo', 'video', 'spreadsheet', 'document', 'application', 'gif', 'drawing', 'corel file', 'iso', '3d model')
       
        deleted_summary = TimeCapsule.objects.all().delete()
        
        self.stdout.write(f'Deleting existing items: {deleted_summary}')
         
        self.stdout.write(self.style.SUCCESS('Creating Time Capsules'))
       
        item_count = 0
        
        for i in range(1, 111):
            t = TimeCapsule()
            t.name = f'{random.choices(FIRST_NAMES)[0]} {random.choices(LAST_NAMES)[0]} {i}'
            t.description = f'A short description for TimeCapsule of {t.name}'
            t.age = 1_900 + i
            t.current_date = timezone.now()
            t.save()
            
            item_count += 1
            
            for j in range(1, 31):
                item = Item()
                item.time_capsule = t
                item.name = f'{random.choices(FIRST_NAMES)[0]}\'s {random.choices(ITEM_NAMES)[0]}'
                item.item_no = random.randint(1_000_000, 2_000_000)

                try:
                    item.save()
                    item_count += 1
                except IntegrityError as e:
                    pass
            
        self.stdout.write(self.style.SUCCESS(f'Done; items created: {item_count}'))