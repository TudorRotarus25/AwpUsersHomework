from django.contrib.auth.models import User
from django.db import models


class UserPost(models.Model):
    text = models.TextField(max_length=500)
    date_added = models.DateTimeField(
        auto_now_add=True)
    author = models.ForeignKey(User)

    class Meta:
        ordering = ['-date_added']

    def __unicode__(self):
        return u'{} @ {}'.format(self.author, self.date_added)


class UserPostComment(models.Model):
    text = models.TextField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    post = models.ForeignKey(UserPost, related_name='comments')

    class Meta:
        ordering = ['date_added']

    def __unicode__(self):
        return u'{} @ {}'.format(self.author, self.date_added)


class UserProfile(models.Model):
    sex_choices = (('M', 'Masculin'), ('F', 'Feminin'))
    prenume = models.TextField(max_length=100)
    nume = models.TextField(max_length=100)
    data_nasterii = models.DateField()
    sex = models.CharField(max_length=1, choices=sex_choices)
    avatar = models.ImageField(upload_to='images', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    def __unicode__(self):
        return u'{} @ {} @ {} @ {}'.format(self.prenume, self.nume, self.data_nasterii, self.sex)
