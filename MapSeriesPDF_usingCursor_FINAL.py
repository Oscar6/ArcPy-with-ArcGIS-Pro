import arcpy,os

arcpy.env.overwriteOutput = True

# Project object
aprx = arcpy.mp.ArcGISProject(
    r"projects path to aprx")

# Map objects
mainMap = aprx.listMaps("Main Map")[0]
overviewMap = aprx.listMaps("Overview Map")[0]

# Layer objects
countriesLayer = mainMap.listLayers("Countries")[0]

# Layout object
lyt = aprx.listLayouts()[0]

# Map Frame objects
mainMapFrame = lyt.listElements('MAPFRAME_ELEMENT',"Main Map Frame")[0]
overviewMapFrame = lyt.listElements('MAPFRAME_ELEMENT',"Overview Map Frame")[0]

finalPDF = r"path to pdf"
if arcpy.Exists(finalPDF):
    arcpy.Delete_management(finalPDF)
pdfDoc = arcpy.mp.PDFDocumentCreate(finalPDF)

countriesSortedByNameList = sorted([row[0] for row in arcpy.da.SearchCursor(
    countriesLayer,"NAME")])
for pageCount,countryName in enumerate(countriesSortedByNameList[:10]):
##with arcpy.da.SearchCursor(countriesLayer,["FID","NAME"],"FID < 10") as rows:
##    for row in rows:
    # Set what to zoom to, zoom to it and then zoom out by 5%
    # countryName = row[1]
    countriesLayer.definitionQuery = "NAME = '{0}'".format(countryName)
    selCountryExtent = mainMapFrame.getLayerExtent(countriesLayer)
    mainMapFrame.camera.setExtent(selCountryExtent)
    mainMapFrame.camera.scale = mainMapFrame.camera.scale * 1.05
    countriesLayer.definitionQuery = ""
    print(countryName)

    # Title text object
    titleText = lyt.listElements("TEXT_ELEMENT","Page Name")[0]
    titleText.text = countryName

    # Export PDF for this country's page
    lyt.exportToPDF(r"path to pdf".format(pageCount))
    pdfDoc.appendPages(r"path to pdf".format(pageCount))

# Save and close PDF and open in Adobe Acrobat Reader
pdfDoc.saveAndClose()
del pdfDoc
os.startfile(finalPDF)

# Delete project object
del aprx

