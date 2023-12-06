from django.conf import settings

def base_dir(request):
    return {'base_dir': settings.BASE_DIR}