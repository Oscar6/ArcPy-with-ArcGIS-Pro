import arcpy
aprx = arcpy.mp.ArcGISProject(
    r"projects path to aprx")
mapx = aprx.listMaps("Map")[0]
lyr = mapx.listLayers("Countries coloured by")[0]

sym = lyr.symbology
sym.updateRenderer('GraduatedColorsRenderer')

sym.renderer.classificationField = "POP_EST"
sym.renderer.breakCount = 8
sym.renderer.colorRamp = aprx.listColorRamps("White to Black")[0]

lyr.symbology  = sym
aprx.save()

