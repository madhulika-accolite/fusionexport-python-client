#!/usr/bin/env python


from fusionexport import ExportManager, ExportConfig  # Import sdk

# Instantiate the ExportConfig class and add the required configurations
export_config = ExportConfig()

#export_config["chartConfig"] = "resources/multiple.json"

#export_config["templateFilePath"] = "resources/template.html"
export_config["templateFilePath"] = "resources/fusiontime.html"
#export_config["templateFilePath"] = "resources/template_timeseries.html"
#export_config["templateFilePath"] = "resources/all_charts.html"
export_config["type"] = "pdf"
#export_config["templateFormat"] = "A4"
#export_config["templateWidth"]= "1500"
#export_config["templateHeight"] = "1600"
export_config["asyncCapture"] = True
export_config["maxWaitForCaptureExit"]=8000

# Provide port and host of FusionExport Service
export_server_host ="127.0.0.1"
export_server_port = 1337

# Instantiate the ExportManager class
em = ExportManager(export_server_host, export_server_port)
# Call the export() method with the export config and the output location
exported_files = em.export(export_config, "./exports", True)
#print(exported_files)