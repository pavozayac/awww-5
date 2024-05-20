from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from cms.models import Picture, Rectangle
from django.contrib.auth.models import User 
from random import randint, choice


class Command(BaseCommand):
    help = "Generates random pictures"

    def add_arguments(self, parser):
        parser.add_argument("picture_count", nargs=1, type=int)

    def handle(self, *args, **options):
        joe = User.objects.get(username='joe')

        for _ in range(options['picture_count'][0]):
            picture = Picture(
                name=f'Random picture {randint(1000000, 9999999)}',
                description=f'Random description {randint(1000000, 9999999)}',
                height=randint(100, 1000),
                width=randint(100, 1000),
                date_added=datetime.now(),
                tags=' '.join([str(i) for i in [randint(0, 10) for _ in range(randint(0, 10))]]),
                # editors=joe
            )

            picture.save()

            picture.editors.aadd(joe)

            pic_id = picture.id

            for _ in range(randint(1, 10)):
                rect = Rectangle(
                    x=randint(0, picture.width),
                    y=randint(0, picture.height),
                    height=randint(0, 100),
                    width=randint(0, 100),
                    fill=choice(('green', 'red', 'blue', 'yellow', 'orange', 'black')),
                    picture_id=pic_id,
                ) 
                
                rect.save()
