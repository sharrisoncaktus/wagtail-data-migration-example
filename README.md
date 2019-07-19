# Wagtail Data Migrations Example

[Wagtail](https://wagtail.io/) is a fantastic content management system framework that does a great job of making it easy for developers to get a new website up and running quickly and painlessly. It's no wonder that Wagtail has grown to become the leading Django-based CMS. [As one of the creators of Wagtail recently said](https://django-chat.simplecast.com/episodes/wagtail-cms-tom-dyson), It makes the initial experience of getting a website set up and running very good. 

*But:…* There are some points of pain for developers who work on large Wagtail projects. One of those those pain points is data migrations, particularly those that involve StreamFields. My informal survey of fellow-developers yielded the following helpful comments:

* "Wagtail migrations are evil."
* "As a rule, _avoid data migrations on streamfields at all costs_."

This repository contains a working example of StreamField migrations. 

## Installation

To install the latest version of the example app:

```bash
$ git clone https://github.com/sharrisoncaktus/wagtail-data-migration-example
$ cd wagtail-data-migration-example
$ mkvirtualenv wagtail-data-migration-example # or your prefered virtualenv setup
(wagtail-data-migration-example) $ pip install -r requirements.txt
```

## Rules for Wagtail Data Migrations

1. You can add fields to the model, and new blocks to StreamFields, with impunity — as long as you don’t move or rename anything.
2. When you merge migrations from two or more developers, and those migrations touch StreamFields, do another final `manage.py makemigrations` to capture the merged state of the StreamFields. 
3. If you are moving or renaming data and you have to do a data migration, split the migration into several steps:
   - **Step 1:** Add new fields to the model without moving or renaming anything.
   - **Step 2:** Create a data migration that maps / copies all the data from the old fields to the new fields, without modifying the existing fields. (Treat existing data as immutable at this point.)
   - **Step 3:** Deploy the migration and let editors review everything, making sure that all the data was correctly copied.
   - **Step 4:** Switch the site templates / API to the new fields.
   - **Step 5:** Create final migration that deletes the old data, and deploy it with updated templates that use the new fields.
4. Data migrations involving StreamFields are best done by using Page.to_json() and Revision.content_json as the data starting point.
   - These data structures are almost identical, so you can use the same function to map page / revision data to new values.
5. Data migrations involving StreamFields are best done by writing directly to the stream_data property of the StreamField.
   - Python-native data structure are a lot easier than trying to build the StreamValue directly.

## Worked Examples of the Rules and the Steps

The above rules & steps are shown in the revision history. To get the full experience, check out each of the revisions in order:

* [ffe4354a0a46e2c39df7730e0c95a26df8726db4](https://github.com/sharrisoncaktus/wagtail-data-migration-example/tree/ffe4354a0a46e2c39df7730e0c95a26df8726db4) – Adds ExamplePage model
* [148997a82c5470854dbe93e8dbfd120080c2260e](https://github.com/sharrisoncaktus/wagtail-data-migration-example/tree/148997a82c5470854dbe93e8dbfd120080c2260e) – Adds pages to docs StreamField in ExamplePage
* [8c4b22e32bd9421a3f89a49b7c1300c243606f5d](https://github.com/sharrisoncaktus/wagtail-data-migration-example/tree/8c4b22e32bd9421a3f89a49b7c1300c243606f5d) – Adds a content StreamField to ExamplePage
* [b58cb7226be9ab9eec808aaa5393c3b77d94ab08](https://github.com/sharrisoncaktus/wagtail-data-migration-example/tree/b58cb7226be9ab9eec808aaa5393c3b77d94ab08) – Data migration copies page data to ExamplePage.content
* [dfc33cdff13724e5485f515676970ac555d6c403](https://github.com/sharrisoncaktus/wagtail-data-migration-example/tree/dfc33cdff13724e5485f515676970ac555d6c403) – Removes old page data

For each tag, run the migrations, then run the server, and create / edit an ExamplePage that uses the model.

