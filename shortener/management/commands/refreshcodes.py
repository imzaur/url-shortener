from django.core.management.base import BaseCommand, CommandError

from shortener.models import KirrURL

class Command(BaseCommand):
    help = 'Refreshes all KirrURL shortcodes'

    # def add_arguments(self, parser):
    #     parser.add_argument('number', nargs='+', type=int)

    def handle(self, *args, **options):
        return KirrURL.objects.refresh_shortcodes()
