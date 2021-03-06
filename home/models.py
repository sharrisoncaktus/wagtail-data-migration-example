from django.db import models
from django.db.models import ImageField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.blocks import RichTextBlock, PageChooserBlock, StreamBlock
from wagtail.core.models import Page
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    pass


class ExamplePage(Page):
    content = StreamField(
        [
            ('image', ImageChooserBlock()),
            ('text', RichTextBlock()),
            ('docs',
             StreamBlock([
                 ('doc', DocumentChooserBlock()),
                 ('page', PageChooserBlock()),
             ])),
        ]
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]
