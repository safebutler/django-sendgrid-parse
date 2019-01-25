from django.db import models

from jsonfield import JSONField
import os

from . import _ugl


def attachments_file_upload(instance, filename):
    fn, ext = os.path.splitext(filename)
    return 'emails/{to}/{id}/{fn}{ext}'.format(
        to=instance.email.to_mailbox,
        id=instance.email.id,
        fn=fn[:25],
        ext=ext
    )


class Email(models.Model):
    headers = models.TextField(
        blank=True,
        null=True,
        verbose_name=_ugl('Headers')
    )
    text = models.TextField(
        blank=True,
        null=True,
        verbose_name=_ugl('Text')
    )
    html = models.TextField(
        blank=True,
        null=True,
        verbose_name=_ugl('HTML')
    )
    to_mailbox = models.TextField(
        blank=False,
        null=False,
        verbose_name=_ugl('To')
    )
    from_mailbox = models.TextField(
        blank=False,
        null=False,
        verbose_name=_ugl('From')
    )
    cc = models.TextField(
        blank=True,
        null=True,
        verbose_name=_ugl('Carbon Copy')
    )
    subject = models.TextField(
        blank=True,
        null=True,
        verbose_name=_ugl('Subject')
    )
    # Changed because sendgrid doesn't respect REST and JSON standards ¬¬
    dkim = models.TextField(
        blank=True,
        null=True,
        verbose_name=_ugl('DomainKeys Identified Mail')
    )
    # Changed because sendgrid doesn't respect REST and JSON standards ¬¬
    SPF = models.TextField(
        blank=True,
        null=True,
        verbose_name=_ugl('Sender Policy Framework')
    )
    envelope = JSONField(
        default={'to': None, 'from': None},
        blank=True,
        null=True,
        verbose_name=_ugl('Envelope')
    )
    charsets = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_ugl('Charsets')
    )
    spam_score = models.FloatField(
        blank=True,
        null=True,
        verbose_name=_ugl('Spam score')
    )
    spam_report = models.TextField(
        blank=True,
        null=True,
        verbose_name=_ugl('Spam report')
    )
    creation_date = models.DateTimeField(
       auto_now_add=True,
       verbose_name=_ugl('Creation date')
    )
    # TODO: sender_ip
    # TODO: attachment-info
    # TODO: content-ids


class Attachment(models.Model):
    number = models.IntegerField(
        default=1,
        blank=False,
        null=False,
        verbose_name=_ugl("Email's Attachment Number")
    )
    file = models.FileField(
        upload_to=attachments_file_upload,
        blank=False,
        null=False,
        verbose_name=_ugl('Attached File'),
        max_length=1000,
    )
    email = models.ForeignKey(
        Email,
        blank=False,
        null=False,
        related_name='attachments',
        verbose_name=_ugl("Email Attached To",),
        on_delete=models.CASCADE,
    )

    @property
    def filename(self):
        return os.path.basename(self.file.name)
