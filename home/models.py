from django.db import models
from django.db.models import ImageField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.blocks import RichTextBlock, PageChooserBlock
from wagtail.core.models import Page
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    pass


class ExamplePage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = RichTextField()
    docs = StreamField([
        ('doc', DocumentChooserBlock()),
        ('page', PageChooserBlock()),
    ])
    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        FieldPanel('body'),
        StreamFieldPanel('docs'),
    ]
