from django.db.models.signals import post_save
from .models import Profile
from django.contrib.auth.models import User
def create_profile(sender, instance ,created , **kwargs) :
    user = instance
    if created :
       Profile.objects.create(
        user = user,
        role = 'Member'
        )

post_save.connect(create_profile , User)
   