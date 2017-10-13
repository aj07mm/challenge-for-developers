from django.db import models


class RepositoryManager(models.Manager):

    def filter_by_tag(self, user, tag_name):
        return self.filter(user=user, tags__name__icontains=tag_name)

    def filter_by_user(self, user):
        return self.filter(user=user)

