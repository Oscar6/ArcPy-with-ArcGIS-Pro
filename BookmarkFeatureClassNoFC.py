import arcpy

arcpy.env.overwriteOutput = True

aprx = arcpy.mp.ArcGISProject(
    r"projects path to aprx")
mapx = aprx.listMaps()[0]
lyt = aprx.listLayouts()[0]
mf = lyt.listElements('MAPFRAME_ELEMENT',"Map Frame")[0]
lyr = mapx.listLayers("bmFC")[0]
mapx.removeLayer(lyr)

pdfFile = r"path to pdf"
if arcpy.Exists(pdfFile):
    arcpy.management.Delete(pdfFile)
pdfDoc = arcpy.mp.PDFDocumentCreate(pdfFile)

for count,bm in enumerate(mapx.listBookmarks()):
    print(bm.name)
    mf.zoomToBookmark(bm)
    pdfPage = r"path to pdf".format(count)
    lyt.exportToPDF(pdfPage)
    pdfDoc.appendPages(pdfPage)
    arcpy.management.Delete(pdfPage)
pdfDoc.saveAndClose()

del bm,aprx,pdfDoc
