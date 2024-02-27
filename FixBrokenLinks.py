import arcpy,pprint

##def print_source(layerName):
##    lyr2Print = mapx.listLayers(layerName)[0]
##    print("{0}: {1}".format(lyr2Print.name,lyr2Print.dataSource))
##
##def print_dict(dict2Print):
##    pprint.pprint(dict2Print)

aprx = arcpy.mp.ArcGISProject(
    r"projects path to aprx")
##mapx = aprx.listMaps("Basemap")[0]
##print_source("Countries")
##
##lyr = mapx.listLayers("Countries")[0]
##defaultGDB = r"path to db"
### lyr.dataSource = r"{0}\Countries_African".format(defaultGDB)
##origConnPropDict = lyr.connectionProperties
##print_dict(origConnPropDict)
####newConnPropDict = {'connection_info': {'database': defaultGDB},
####                   'dataset': "Countries_African",
####                   'workspace_factory': 'File Geodatabase'}
####lyr.updateConnectionProperties(origConnPropDict,newConnPropDict)
####print_dict(newConnPropDict)
##mapx.updateConnectionProperties("test.gdb","test2.gdb")
##print_source("Countries")
##print_source("Places")
aprx.updateConnectionProperties("test2.gdb",r"path to db")
aprx.save()

del aprx
