import django.conf
import django.db
import django.http
import django.utils

import users.models

__all__ = []

SESSION = 300


class UserStatus(django.db.models.Model):
    user = django.db.models.OneToOneField(
        django.conf.settings.AUTH_USER_MODEL,
        on_delete=django.db.models.CASCADE,
        related_name='status',
    )
    last_activity = django.db.models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ['-last_activity']

    def __str__(self):
        return f'Status of user: {self.user.username}'

    @staticmethod
    def update_user_activity(user):
        UserStatus.objects.update_or_create(
            user=user,
            defaults={'last_activity': django.utils.timezone.now()},
        )

    @staticmethod
    def is_user_online(user):
        if not isinstance(user, users.models.User):
            try:
                user = users.models.User.objects.get(username=user)
            except users.models.User.DoesNotExist:
                return False

        try:
            user_status = UserStatus.objects.get(user=user)
            online = django.utils.timezone.now() - user_status.last_activity
            return online.total_seconds() < SESSION
        except UserStatus.DoesNotExist:
            return False

    @staticmethod
    def last_seen(user):
        if not isinstance(user, users.models.User):
            try:
                user = users.models.User.objects.get(username=user)
            except users.models.User.DoesNotExist:
                return django.utils.timezone.now()

        try:
            return UserStatus.objects.get(user=user).last_activity
        except UserStatus.DoesNotExist:
            return django.utils.timezone.now()
