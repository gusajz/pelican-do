import click
import datetime
import textwrap
from jinja2 import Environment

# Custom filter method
def rst_title(s):
  return s + '\n' + '#' * len(s)

def pelican_datetime(value):
  return value.strftime('%Y-%m-%d %H:%M')
    

@click.group()
def main():
  pass

@main.command()
@click.argument('name')
@click.option('--format', default='rst', type=click.Choice(['rst']), help='Format used to write the article.')
@click.option('--title', type=str, help='Title for the article. By default, it will be the name.', default=None)
@click.option('--category', type=str, help='category for the article.', default=None)
def post(name, format, title, category):
  today = datetime.datetime.now()

  jinja_environment = Environment()
  jinja_environment.filters['rst_title'] = rst_title
  jinja_environment.filters['pelican_datetime'] = pelican_datetime

  # 2010-10-03 10:20
  template = jinja_environment.from_string(textwrap.dedent('''
    {{title|rst_title}}
    :date: {{date|pelican_datetime}}
    :modified: {{date|pelican_datetime}}
    :tags: thats, awesome
    :category: {{category}}
    :slug: my-super-post
    :authors: Alexis Metaireau, Conan Doyle
    :summary: Short version for index and feeds
  '''))
# >>> template.render(name='John Doe')

  filename = '%s-%s.rst' % (today.strftime('%Y-%m-%d'), name)

  print template.render(title=name or title, date=today)

  print 'creating %s' % filename