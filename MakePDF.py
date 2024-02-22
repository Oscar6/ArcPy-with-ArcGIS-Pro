import arcpy,os

# Enable overwriting of outputs
arcpy.env.overwriteOutput = True

# Project object
aprx = arcpy.mp.ArcGISProject(
    r"path")

# Map object
mapx = aprx.listMaps("Map")[0]

# Layer object
countriesLayer = mapx.listLayers("Countries")[0]

# Layout object
lyt = aprx.listLayouts()[0]

# Map Frame object
mapFrame = lyt.listElements('MAPFRAME_ELEMENT',"Map Frame")[0]
mapFrame.elementWidth = lyt.pageWidth - 20
mapFrame.elementHeight = mapFrame.elementWidth
mapFrame.elementPositionX = 10
mapFrame.elementPositionY = lyt.pageHeight / 4

# Export to PDF and open in Adobe Acrobat Reader
lyt.exportToPDF(r"path")
os.startfile(r"path")

# Delete project object
del aprx

