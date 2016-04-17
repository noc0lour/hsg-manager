from django.db import models
from django.core.exceptions import ValidationError


class Group(models.Model):
    name = models.CharField(max_length=100)
    abbrev = models.CharField(max_length=50)
    homepage = models.URLField(blank=True)
    postbox = models.CharField(max_length=3, blank=True)
    logo = models.FileField(upload_to='Logos/', blank=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.abbrev)


class RegInfo(models.Model):

    class Meta:
        ordering = ['-date', 'group']
        verbose_name = "Registration"
        verbose_name_plural = "Registrations"
    group = models.ForeignKey('Group', related_name='registration')
    date = models.DateField()
    documents = models.BooleanField(default=False)
    constitution = models.BooleanField(default=False)
    comment = models.CharField(max_length=160, blank=True)
    duedate = models.DateField(blank=True, null=True)
    members = models.SmallIntegerField()
    FULL = 'FULL'
    PRELIMINARY = 'PREL'
    NONE = 'NONE'
    FORMS_CHOICES = (
        (FULL, 'Full'),
        (PRELIMINARY, 'Preliminary'),
        (NONE, 'None'),
    )
    form = models.CharField(max_length=4,
                            choices=FORMS_CHOICES,
                            default=NONE)

    def __str__(self):
        return("{} ".format(self.group)+ str(self.get_form_display()))

    def clean(self):
        if (self.form == self.PRELIMINARY) and (not self.duedate):
            raise ValidationError(
                'Set duedate for preliminary registration',
                code='invalid'
            )
        if (Group.objects.filter(id=self.group.id, registration__date__year=self.date.year).exclude(registration__id=self.id)):
            raise ValidationError(
                'This group has already a Registration for the year {}'.format(
                    self.date.year),
                code='invalid')


class RegProcess(models.Model):
    group = models.ForeignKey('Group', related_name='status')
    mailinglist = models.BooleanField(default=0)
    homepage = models.BooleanField(default=0)
    logowall = models.BooleanField(default=0)


class GroupEmail(models.Model):
    group = models.ForeignKey('Group', related_name='listemail')
    email = models.EmailField()


class GroupContact(models.Model):
    registration = models.ForeignKey('RegInfo', related_name='contact')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return "{} ({})".format(self.name, self.registration)

class PostAddress(models.Model):
    group = models.ForeignKey('Group', related_name='address', null=True)
    person = models.ForeignKey('GroupContact',
                               related_name='address', null=True)
    street = models.CharField(max_length=50)
    housenumber = models.CharField(max_length=10)
    location = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)

    def __str__(obj):
        return("{} {}, {} {}".format(obj.street, obj.housenumber, obj.location,
                                     obj.zipcode))
