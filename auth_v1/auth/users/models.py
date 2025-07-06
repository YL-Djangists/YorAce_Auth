import django.conf
import django.contrib.auth.models
import django.core.validators
import django.db.models
import django.utils.timezone


__all__ = []


class User(django.contrib.auth.models.AbstractUser):
    email = django.db.models.EmailField(unique=True)


def pfp_upload_to(self, filename):
    return f'users/{self.user.username}/pfp/{filename}'


class UserProfile(django.db.models.Model):
    user = django.db.models.OneToOneField(
        django.conf.settings.AUTH_USER_MODEL,
        on_delete=django.db.models.CASCADE,
        related_name='profile',
    )

    profile_picture = django.db.models.ImageField(
        upload_to=pfp_upload_to,
        blank=True,
        validators=[
            django.core.validators.FileExtensionValidator(
                ['png', 'jpg', 'jpeg'],
            ),
        ],
    )

    last_activity = django.db.models.DateTimeField(
        default=django.utils.timezone.now,
    )
