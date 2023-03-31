from django.db import models

# OUR TEAM MODEL -> TEAM MEMBERS MODEL
# profile picture
# firstname
# lastname
# designation
# facebooklink
# twitterlink
# googleplusLink
# created_date


class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='photos/%y/%m/%d')
    facebook_link = models.URLField(max_length=200)
    twitter_link = models.URLField(max_length=200)
    googleplus_link = models.URLField(max_length=200)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
