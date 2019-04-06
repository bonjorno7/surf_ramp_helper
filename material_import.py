# <import>
import os, subprocess
import bpy, bpy_extras
from . import common
# </import>

# <classes>
class ImportMaterial(bpy.types.Operator, bpy_extras.io_utils.ImportHelper):
    """Create materials with the names of the paths to your VMTs relative to the materials folder and import the VTFs as PNGs"""
    bl_idname = "base.import_material"
    bl_label = "Import Material(s)"
    bl_options = {"REGISTER", "UNDO"}

    files: bpy.props.CollectionProperty(type = bpy.types.PropertyGroup)

    def execute(self, context):
        folder, _ = os.path.split(self.properties.filepath)

        for f in self.files:
            if not f.name.lower().endswith(".vmt"): continue
            print(folder + os.sep + f.name)

        return {"FINISHED"}

class MaterialImportPanel(bpy.types.Panel):
    bl_idname = "base.material_import_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "objectmode"
    bl_category = "BASE"
    bl_label = "Material Importer"

    def draw_header(self, context):
        self.layout.label(icon = 'FILE_IMAGE')

    def draw(self, context):
        self.layout.operator("base.import_material")
# </classes>