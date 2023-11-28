
import rich_click as click
import pkg_resources
import json
from rich.table import Table
from rich.console import Console
from dundie import core


click.rich_click.USE_RICH_MARKUP = True
click.rich_click.USE_MARKDOWN = True
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True
click.rich_click.SHOW_METAVARS_COLUMN = False
click.rich_click.APPEND_METAVARS_HELP = True


@click.group
@click.version_option(pkg_resources.get_distribution("dundie").version)
def main():
    """
    Dundie cli com click
    """


@main.command()
@click.argument("filepath", type=click.Path(exists=True))
def load(filepath):
    table = Table(title="Dunder Mifflin Associates")
    headers = ['name', "dept", "role","created", "e-mail"]
    for header in headers:
        table.add_column(header, style="magenta")
    result = core.load(filepath)
    for person in result:
        table.add_row(*[str(value) for value in person.values()])
    console = Console()
    console.print(table)


@main.command()
@click.option("--dept", required=False)
@click.option("--email", required=False)
@click.option("--output", default= None)
def show(output, **query):
    result = core.read(**query)

    if output:
        with open(output, "w") as output_file:
            output_file.write(json.dumps(result))

    if not result:
        print("Nothing to show")
        return
    table = Table(title="Dunder Mifflin Report")
    for key in result[0]:
        table.add_column(key.title(), style="magenta")
    
    for person in result:
        table.add_row(*[str(value) for value in person.values()]) 

    console = Console()
    console.print(table)


@main.command()
@click.argument("value", type=click.INT, required=True)
@click.option("--dept", required=False)
@click.option("--email", required=False)
@click.pass_context
def add(ctx, value, **query):
    core.add(value, **query)
    ctx.invoke(show, **query)
    
    

@main.command()
@click.argument("value", type=click.INT, required=True)
@click.option("--dept", required=False)
@click.option("--email", required=False)
@click.pass_context
def sub(ctx, value, **query):
    core.add(-value, **query)
    ctx.invoke(show, **query)
