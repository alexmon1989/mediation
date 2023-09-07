import reversion.signals
from django.dispatch import receiver


@receiver(reversion.signals.pre_revision_commit, sender=reversion.create_revision)
def pre_revision_commit_handler(sender, **kwargs):
    kwargs['revision'].comment = kwargs['revision'].comment.replace('Причина змін та ', '')


@receiver(reversion.signals.post_revision_commit, sender=reversion.create_revision)
def post_revision_commit_handler(sender, **kwargs):
    if kwargs['revision'].comment == 'Змінені Причина змін.':
        kwargs['revision'].delete()
