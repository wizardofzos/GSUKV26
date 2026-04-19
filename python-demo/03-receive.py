import xmi

xmi_object = xmi.open_file("GSUK26V.XMIT")

xmi_object.set_output_folder(".")
xmi_object.extract_all()
