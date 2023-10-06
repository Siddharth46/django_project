from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Greet the admin"

    def handle(self, *args, **kwargs):
        self.stdout.write("HI there")