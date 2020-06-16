from flask.cli import with_appcontext
import click
from myapp import config


@click.command('create-schema')
@with_appcontext
def create_schema():
    """create new tables."""
    config.database.db.create_all()
    click.echo('Initialized the database.')


@click.command('drop-schema')
@with_appcontext
def drop_schema():
    """Drop the tables."""
    config.database.db.drop_all()
    click.echo('Drop the database.')
