import random

from rich.console import Console

console = Console()
from rich.progress import track
from time import sleep

from rich.table import Table

table = Table(show_header=True, header_style="bold")
table.add_column("Date", style="dim", width=12)
table.add_column("Title")
table.add_column("Product Budget", justify="right")
table.add_column("Box Office", justify="right")

table.add_row(
    "dec 20, 2019",
    "Star Wars: The Rise of Skywalker",
    "$70,000,000",
    "$25,151,347",
)
table.add_row(
    "may 25, 2018",
    "[red]Solo[/red]: The Rise of Skywalker",
    "$275,000,000",
    "$393,151,347",
)
table.add_row(
    "dec 15, 2017",
    "[red]Solo[/red]: The Rise of Skywalker",
    "$25,0,000",
    "$3,11,347",
)

console.print(table)