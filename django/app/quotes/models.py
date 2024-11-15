# Create your models here.
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Q

from pgvector.django import VectorField


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Language(BaseModel):
    code = models.CharField(max_length=2, unique=True, default="xx")
    name = models.CharField(max_length=100, unique=True)

    class Meta:  # type: ignore
        constraints = [
            models.CheckConstraint(
                name="language_supported_only_en_or_es",
                check=Q(code="en") | Q(code="es"),
            )
        ]

    def __str__(self):
        return str(self.name)


class Author(BaseModel):
    name = models.CharField(max_length=200, unique=True)
    authorized = models.BooleanField(default=False)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    image_sm = models.ImageField(upload_to="images", null=True, blank=True)
    image_md = models.ImageField(upload_to="images", null=True, blank=True)
    image_lg = models.ImageField(upload_to="images", null=True, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.name

    @property
    def full_name(self):
        return f"{self.name}"

    @property
    def text(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author-detail", kwargs={"pk": self.pk})


# Create your models here.
class Quote(BaseModel):
    quote = models.TextField()
    authorized = models.BooleanField(default=False)
    is_private = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    embedding = VectorField(dimensions=1536)

    def __str__(self):
        return str(self.quote)

    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="quotes"
    )

    favorite = models.ForeignKey(
        "Favorite",
        on_delete=models.SET_NULL,
        null=True,
        related_name="quotes",
    )

    language = models.ForeignKey(
        Language, on_delete=models.SET_NULL, null=True, related_name="quotes"
    )


class Favorite(BaseModel):
    quote = models.ForeignKey(
        Quote,
        on_delete=models.SET_NULL,
        null=True,
        related_name="favorites",
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )
