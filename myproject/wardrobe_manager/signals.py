from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Bases, Coats, Combinations, Hats, Overtops, Pants, Shoes
import subprocess

# Funkcja odbiorcy sygnału
@receiver(post_save, sender=Bases)
@receiver(post_save, sender=Coats)
@receiver(post_save, sender=Hats)
@receiver(post_save, sender=Overtops)
@receiver(post_save, sender=Pants)
@receiver(post_save, sender=Shoes)
def item_added(sender, instance, created, **kwargs):
    print('dziala')
    if created:
        print(f'Item {sender} has been added to database.')
        print(f'{sender} properties: {instance.properties()}')
        
        list_of_ids = {}
        
        if sender == Bases:
            list_of_ids['bases'] = [instance.id]
        else:
            list_of_ids['bases'] = Bases.objects.values_list('id', flat=True)
        
        if sender == Coats:
            list_of_ids['coats'] = [instance.id]
        else:
            list_of_ids['coats'] = Coats.objects.values_list('id', flat=True)
        
        if sender == Hats:
            list_of_ids['hats'] = [instance.id]
        else:
            list_of_ids['hats'] = Hats.objects.values_list('id', flat=True)
        
        if sender == Overtops:
            list_of_ids['overtops'] = [instance.id]
        else:
            list_of_ids['overtops'] = Overtops.objects.values_list('id', flat=True)
        
        if sender == Pants:
            list_of_ids['pants'] = [instance.id]
        else:
            list_of_ids['pants'] = Pants.objects.values_list('id', flat=True)
        
        if sender == Shoes:
            list_of_ids['shoes'] = [instance.id]
        else:
            list_of_ids['shoes'] = Shoes.objects.values_list('id', flat=True)
            
        for shoes in list_of_ids['shoes']:
            for pants in list_of_ids['pants']:
                for base in list_of_ids['bases']:
                    for overtop in list_of_ids['overtops']:
                        for coat in list_of_ids['coats']:
                            for hat in list_of_ids['hats']:
                                Combinations.objects.create(
                                    shoes_id=shoes,
                                    pants_id=pants,
                                    base_id=base,
                                    overtop_id=overtop,
                                    coat_id=coat,
                                    hat_id=hat,
                                    reviewed=False,
                                    rate=None
                                    )