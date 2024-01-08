import arcpy
import os

Capa_Dissolve = arcpy.GetParameterAsText(0)
Field_Dissolve = arcpy.GetParameterAsText(1)
Capa_Mz = arcpy.GetParameterAsText(2)
Field_Mz = arcpy.GetParameterAsText(3)

#Ruta_Salida
salida_feature_class = arcpy.GetParameterAsText(4)
ruta_salida = arcpy.ValidateTableName(os.path.splitext(os.path.basename(salida_feature_class))[0])#Extrae el contenido de la ruta para que se guarde con el nombre y lo valida
# Eliminar la capa existente si ya existe
if arcpy.Exists("CapaPrincipal_Layer"):
    arcpy.Delete_management("CapaPrincipal_Layer")
#Add_Join
arcpy.MakeFeatureLayer_management(capa_principal, "CapaPrincipal_Layer")
arcpy.AddJoin_management("CapaPrincipal_Layer", Field_Dissolve, tabla_de_union, campo_relacionado)

#Crea el export
arcpy.CopyFeatures_management("CapaPrincipal_Layer", ruta_salida)

#Elimina el Join inicial(Temporal)
arcpy.RemoveJoin_management("CapaPrincipal_Layer")

#Abre el shp en la tabla de contenido
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]
arcpy.mapping.AddLayer(df, arcpy.mapping.Layer(ruta_salida))
arcpy.RefreshActiveView()
