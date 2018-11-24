from django.db import models


class Article(models.Model):
    abstract = models.TextField()
    journal = models.TextField()
    title = models.TextField()


class Author(models.Model):
    affiliation = models.TextField()
    email = models.EmailField()
    name = models.TextField()


class Domain(models.Model):
    name = models.TextField()


class Entity(models.Model):
    concept_code = models.IntegerField()
    name = models.TextField()
    omop_id = models.TextField()
    vocabulary_id = models.TextField()


class Tag(models.Model):
    description = models.TextField()
    name = models.TextField()
