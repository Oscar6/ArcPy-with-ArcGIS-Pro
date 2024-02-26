import arcpy

aprx = arcpy.mp.ArcGISProject(
    r"projects path to aprx")
lyt = aprx.listLayouts("Layout")[0]
mapSeries = lyt.mapSeries
mapSeries.exportToPDF(r"pdf path","RANGE","1-10")
del aprx
