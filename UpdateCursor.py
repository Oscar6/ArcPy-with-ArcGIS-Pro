import arcpy

shp = r"C:\Users\Artemis II\Desktop\LPA\Data\ne_10m_admin_0_countries.shp"
fc = r"C:\Users\Artemis II\Desktop\LPA\Projects\CursorProject\CursorProject.gdb"

arcpy.env.overwriteOutput = True
arcpy.management.CopyFeatures(shp,fc)
arcpy.management.AddField(fc,"GDPperPerson","FLOAT")

with arcpy.da.UpdateCursor(fc,["NAME","GDP_MD_EST","POP_EST","GDPperPerson"]) as cursor:
    for row in cursor:
        row[0] = row[0].upper()
        if row[2] == 0:
            row[3] = 0
        else:
            row[3] = (row[1]*1000000) / row[2]
        if row[3] >= 10000:
            cursor.deleteRow()
        else:
            cursor.updateRow(row)
            print("{0} GDPPP: US${1}".format(row[0],int(row[3])))
        # print(row[0])

print("\nScript completed!")
