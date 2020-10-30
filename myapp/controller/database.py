from flask.cli import with_appcontext
import click
# from myapp.config.database import db
db = None

@click.command('create-schema')
@with_appcontext
def create_schema():
    """create new tables."""
    db.create_all()
    click.echo('Initialized the database.')


@click.command('drop-schema')
@with_appcontext
def drop_schema():
    """Drop the tables."""
    db.drop_all()
    click.echo('Drop the database.')
