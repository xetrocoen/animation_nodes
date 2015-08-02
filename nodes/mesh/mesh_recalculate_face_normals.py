import bpy, bmesh
from ... base_types.node import AnimationNode
from ... mn_execution import nodePropertyChanged, allowCompiling, forbidCompiling

class mn_MeshRecalculateFaceNormals(bpy.types.Node, AnimationNode):
    bl_idname = "mn_MeshRecalculateFaceNormals"
    bl_label = "Recalculate Normals"

    invert = bpy.props.BoolProperty(name = "Invert Normals", update = nodePropertyChanged)

    def init(self, context):
        forbidCompiling()
        self.inputs.new("mn_MeshSocket", "Mesh")
        self.outputs.new("mn_MeshSocket", "Mesh")
        allowCompiling()

    def draw_buttons(self, context, layout):
        layout.prop(self, "invert")

    def getInputSocketNames(self):
        return {"Mesh" : "bm"}
    def getOutputSocketNames(self):
        return {"Mesh" : "mesh"}

    def execute(self, bm):
        self.calculate_face_normals(bm)
        if self.invert:
            self.calculate_face_normals(bm)
        return bm

    def calculate_face_normals(self, bm):
        bmesh.ops.recalc_face_normals(bm, faces = bm.faces)