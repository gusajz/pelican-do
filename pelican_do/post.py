from jinja2 import Environment

import datetime
import textwrap

from pelican_do.lib.filters import *
import slugify

templates = {
  'rst': textwrap.dedent('''
    {{title|rst_title}}
    :date: {{date|pelican_datetime}}
    :modified: {{date|pelican_datetime}}
    :tags: {{tags|join(', ')}}
    :category: {{category}}
    :slug: {{slug}}
    :authors: Alexis Metaireau, Conan Doyle
    :summary: {{summary}}
  '''),

  'md': textwrap.dedent('''
    Title: {{title}}
    Date: {{date|pelican_datetime}}
    Modified: {{date|pelican_datetime}}
    Category: Python
    Tags: {{tags|join(', ')}}
    Slug: {{slug}}
    Authors: Alexis Metaireau, Conan Doyle
    Summary: {{summary}}

    This is the content of my super blog post.
  ''')
}

def post(today, name, format, title, category, tags, summary):
  title = title or name

  jinja_environment = Environment()
  jinja_environment.filters['rst_title'] = rst_title
  jinja_environment.filters['pelican_datetime'] = pelican_datetime

  # 2010-10-03 10:20
  template = jinja_environment.from_string(templates[format])
# >>> template.render(name='John Doe')

  filename = '%s-%s.%s' % (today.strftime('%Y-%m-%d'), name, format)

  slug = slugify.slugify(title)

  print template.render(title=title, date=today, tags=tags, slug=slug, summary=summary)

  print 'creating %s' % filename
