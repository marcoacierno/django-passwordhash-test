from django.contrib.auth import get_user_model
from django.db import models
from django.dispatch import receiver

User = get_user_model()

@receiver(models.signals.pre_save, sender=User)
def personal_pre_save(*args, **kwargs):
    user = kwargs['instance']
    user.prev_password = User.objects.get(id=user.id).password
    print('pre-save: raw pass', user._password, 'user.password', user.password)


@receiver(models.signals.post_save, sender=User)
def personal_post_save(*args, **kwargs):
    user = kwargs['instance']
    print('post-save:',
          'raw password', user._password,
          'are hashes equal?', user.prev_password == user.password,
          'user.prev_password is: ', user.prev_password,
          'user.password is:', user.password
    )
