from django.conf import settings


def global_vars(request):
    global_vars = dict(
        SITE_NAME=settings.SITE_NAME,
        REFRESH_TIME=settings.REFRESH_TIME,
    )
    return global_vars
