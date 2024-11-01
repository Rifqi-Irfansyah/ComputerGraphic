import bpy

table_width = 1.5
table_length = 3.0
table_height = 0.5
ob = []

table_top = bpy.ops.mesh.primitive_plane_add(
    size=table_width*1.3,
    enter_editmode=False,
    location=(0, 0, table_height*1.126)
)

table_leg_1 = bpy.ops.mesh.primitive_cube_add(
    size=table_width/12,
    enter_editmode=False,
    location=(-table_length/2 + table_width/2, -table_width/2 + table_height/2, table_height/2),
)
ob.append(bpy.context.object)

table_leg_2 = bpy.ops.mesh.primitive_cube_add(
    size=table_width/12,
    enter_editmode=False,
    location=(-table_length/2 + table_width/2, table_width/2 - table_height/2, table_height/2),
)
ob.append(bpy.context.object)

table_leg_3 = bpy.ops.mesh.primitive_cube_add(
    size=table_width/12,
    enter_editmode=False,
    location=(table_length/2 - table_width/2, -table_width/2 + table_height/2, table_height/2),
)
ob.append(bpy.context.object)

table_leg_4 = bpy.ops.mesh.primitive_cube_add(
    size=table_width/12,
    enter_editmode=False,
    location=(table_length/2 - table_width/2, table_width/2 - table_height/2, table_height/2),
)
ob.append(bpy.context.object)

for leg in ob:
    leg.scale[0] = 2
    leg.scale[1] = 1
    leg.scale[2] = 5