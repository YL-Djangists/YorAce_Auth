import django.conf
import django.conf.urls
import django.conf.urls.static
import django.contrib
import django.urls


urlpatterns = [
    django.urls.path('admin/', django.contrib.admin.site.urls),
    django.urls.path(
        'users/',
        django.urls.include('users.urls'),
    ),
    django.urls.path(
        'auth/',
        django.urls.include('django.contrib.auth.urls'),
    ),
]


if django.conf.settings.DEBUG:
    import debug_toolbar.toolbar

    urlpatterns += debug_toolbar.toolbar.debug_toolbar_urls()

    urlpatterns += django.conf.urls.static.static(
        django.conf.settings.MEDIA_URL,
        document_root=django.conf.settings.MEDIA_ROOT,
    )

    urlpatterns += django.conf.urls.static.static(
        django.conf.settings.STATIC_URL,
        document_root=django.conf.settings.STATIC_ROOT,
    )
