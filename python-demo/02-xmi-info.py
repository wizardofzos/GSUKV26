import xmi
import json
from rich import print
from rich.console import Console

xmi_object = xmi.open_file("GSUK26V.XMIT")

console = Console()

with console.pager(styles=True):
    console.print(xmi_object.get_json())
