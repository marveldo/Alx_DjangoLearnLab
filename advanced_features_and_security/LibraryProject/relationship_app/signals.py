from django.db.models.signals import post_save
from .models import UserProfile
from django.contrib.auth.models import User
def create_profile(sender, instance ,created , **kwargs) :
    user = instance
    if created :
       UserProfile.objects.create(
        user = user,
        role = 'Member'
        )

post_save.connect(create_profile , User)
   