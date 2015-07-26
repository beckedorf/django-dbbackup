from optparse import make_option
from django.core.management.base import BaseCommand, LabelCommand


class BaseDbBackupCommand(LabelCommand):
    option_list = BaseCommand.option_list + (
        make_option("--noinput", action='store_false', dest='interactive', default=True,
                    help='Tells Django to NOT prompt the user for input of any kind.'),
        make_option('-q', "--quiet", action='store_true', default=False,
                    help='Tells Django to NOT output other text than errors.')
    )

    verbosity = 1
    quiet = False

    def log(self, msg, level):
        if not self.quiet and self.verbosity >= level:
            self.stdout.write(msg)
