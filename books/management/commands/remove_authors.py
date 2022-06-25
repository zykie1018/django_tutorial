from django.core.management.base import BaseCommand, CommandError
from books.models import Author


class Command(BaseCommand):
    help = "Removes the author from the given ids"

    def add_arguments(self, parser):
        parser.add_argument("author_ids", nargs="+", type=int)

    def handle(self, *args, **options):

        for author_id in options["author_ids"]:
            try:
                author = Author.objects.get(pk=author_id)
            except Author.DoesNotExist:
                raise CommandError(f"Author ID #{author_id} does not exist.")

            # author.active = False
            print(author)
            author.save()

            self.stdout.write(
                self.style.SUCCESS(f"Successfully deleted author ID #{author_id}.")
            )
