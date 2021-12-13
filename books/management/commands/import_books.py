from django.core.management.base import BaseCommand
from books.models import Book
import json


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(r'fixtures\books.json', 'r', encoding="utf-8") as file:
            books = json.load(file)
            books = [book['fields'] for book in books]
            for row in books:
                book = Book(
                    name=row['name'],
                    author=row['author'],
                    pub_date=row['pub_date']
                )
                book.save()
