from django.apps import AppConfig


class MyappConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        # print("MyappConfig ready method called")
        import myapp.signals
