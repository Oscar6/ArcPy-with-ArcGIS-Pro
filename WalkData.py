import arcpy

# workspace = r"C:\Users\Artemis II\Desktop\LPA\Data"
workspace = r"C:\Users\Artemis II\Desktop\LPA"

dataList = []
for dirpath, dirnames, filenames in arcpy.da.Walk(workspace,datatype="FeatureClass",type=["Point","Polygon"]):
    for filename in filenames:
        dataList.append(r"{0}\{1}".format(dirpath, filename))
print(dataList)
print("\nFound {0} data elements in {1}".format(len(dataList),workspace))

print("\nScript completed")