from django.db.models import CharField, DateTimeField
from django.db.models import Model, SlugField
from django.utils.text import slugify


class BaseSlugModel(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            original_slug = self.slug
            counter = 1
            while self.__class__.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
