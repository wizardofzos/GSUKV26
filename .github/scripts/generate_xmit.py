import os
from pathlib import Path
from xmi import create_xmi


inputfile = Path('GSUK26V.PDS')
outputfile = Path('GSUK26V.XMIT')

create_xmi(inputfile, output_file=outputfile, from_user="WIZARD", from_node="GITHUB")