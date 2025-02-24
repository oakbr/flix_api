import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from actors.models import Actor


class Command(BaseCommand):


    def add_arguments(self, parser):
        
        parser.add_argument('file_name', 
                             type=str, 
                             help='Arquivo CSV com os nomes de atores.')
    
        # parser.add_argument('file_name2', 
        #                      type=str, 
        #                      help='Arquivo com os nomes de atores.')

    def handle(self, *args, **options):

        file_name = options['file_name']
        # file_name2 = options['file_name2']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                name = row['name']
                birthday = datetime.strptime(row['birthday'], '%d/%m/%Y').date()
                nationality = row['nationality']

                self.stdout.write(self.style.NOTICE(name))

                Actor.objects.create(name=name, birthday=birthday, nationality=nationality)

        self.stdout.write(self.style.SUCCESS('Atores importados com sucesso!!!'))
