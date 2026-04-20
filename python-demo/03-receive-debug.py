import xmi
import logging

xmi_object = xmi.open_file("GSUK26V.XMIT", loglevel=logging.DEBUG)

xmi_object.set_output_folder(".")
xmi_object.extract_all()
