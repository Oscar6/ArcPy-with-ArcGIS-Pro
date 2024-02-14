# coding: utf-8
import arcpy

arcpy.env.overwriteOutput = True

# countryName = "China"
countryName = arcpy.GetParameterAsText(0)

arcpy.env.workspace = r"C:\Users\Artemis II\Desktop\LPA\Projects\FrameworkProject\FrameworkProject.gdb"

arcpy.analysis.Select(
    in_features=r"C:\Users\Artemis II\Desktop\LPA\Data\ne_10m_admin_0_countries.shp",
    out_feature_class=r"C:\Users\Artemis II\Desktop\LPA\Projects\FrameworkProject\FrameworkProject.gdb\SelCountry",
    where_clause="NAME = '{0}'".format(countryName)
)

arcpy.analysis.Buffer(
    in_features="SelCountry",
    out_feature_class = "SelCountry_Buffer",
    buffer_distance_or_field="200 Kilometers",
    line_side="FULL",
    line_end_type="ROUND",
    dissolve_option="NONE",
    dissolve_field=None,
    method="PLANAR"
)

arcpy.analysis.Clip(
    in_features=r"C:\Users\Artemis II\Desktop\LPA\Data\ne_10m_populated_places.shp",
    clip_features="SelCountry_Buffer",
    out_feature_class="Places_Clip",
    cluster_tolerance=None
)

arcpy.AddMessage("There are {0} populated places in or within 200km of {1}".format(arcpy.management.GetCount("Places_Clip"),countryName))
