import bpy
import math
import mathutils
import random
def duplicate_object(original_name, new_name, collection_name=None):
    original_object = bpy.data.objects.get(original_name)
    if original_object is None:
        print("Object not found")
        return None

    new_object_data = original_object.data.copy()
    new_object = bpy.data.objects.new(new_name, new_object_data)

    # Manage collection
    if collection_name:
        # Check if the collection exists
        collection = bpy.data.collections.get(collection_name)
        if not collection:
            # Create new collection if it does not exist
            collection = bpy.data.collections.new(collection_name)
            bpy.context.scene.collection.children.link(collection)
        collection.objects.link(new_object)
    else:

        original_collection = original_object.users_collection[0]  # Assumes the object is in at least one collection
        original_collection.objects.link(new_object)

    return new_object

def rotate_object(obj, x_degrees=0, y_degrees=0, z_degrees=0):
    if obj:
        obj.rotation_euler[0] += math.radians(x_degrees)
        obj.rotation_euler[1] += math.radians(y_degrees)
        obj.rotation_euler[2] += math.radians(z_degrees)
        bpy.context.view_layer.update()

def set_location(obj, x, y, z):
    if obj:
        obj.location = (x, y, z)
        bpy.context.view_layer.update()

def resize_object(obj, scale_x, scale_y, scale_z):
    if obj:
        obj.scale = (scale_x, scale_y, scale_z)
        bpy.context.view_layer.update()
        
def parent_objects(parent_obj, child_obj):
    """
    Set one object as the parent of another.
    """
    child_obj.parent = parent_obj


# Example usage:
if __name__ == "__main__":
    # Clear 
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()


    kerangkaBan = duplicate_object("Beam STR ESS BU06x01x01 - SPN-BEM-0043 (stemfie.org)", "KerangkaBan", "MobilDepan")
    kerangkaBan2 = duplicate_object("Beam STR ESS BU06x01x01 - SPN-BEM-0043 (stemfie.org)", "KerangkaBan", "MobilDepan")
    kerangkaBan3 = duplicate_object("Brace STR ERR BU06x01x00.25 - SPN-BRC-0005 (stemfie.org)", "KerangkaBan", "MobilDepan")
    kerangkaBan4 = duplicate_object("Brace STR ERR BU06x01x00.25 - SPN-BRC-0005 (stemfie.org)", "KerangkaBan", "MobilDepan")
    if kerangkaBan:
        rotate_object(kerangkaBan, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(kerangkaBan, -38.942, 91.4146, 28.434)
    if kerangkaBan2:
        rotate_object(kerangkaBan2, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(kerangkaBan2, -38.5046, 30.3902, 5.9819)
    if kerangkaBan3:
        rotate_object(kerangkaBan3, x_degrees=90, y_degrees=0, z_degrees=-90)
        set_location(kerangkaBan3, 35.999 , 110.163 , 34.7576 )
    if kerangkaBan4:
        rotate_object(kerangkaBan4, x_degrees=-90, y_degrees=0, z_degrees=-90)
        set_location(kerangkaBan4, -41.9444 , 110.163 , 34.7576 )

    spakbor1 = duplicate_object("Brace STR ERR BU03x01x00.25 - SPN-BRC-0002 (stemfie.org)", "Spakbor1", "SpakborDepan")
    spakbor2 = duplicate_object("Brace STR ERR BU03x01x00.25 - SPN-BRC-0002 (stemfie.org)", "Spakbor1", "SpakborDepan")
    spakbor3 = duplicate_object("Brace STR ERR BU04x01x00.25 - SPN-BRC-0003 (stemfie.org)", "Spakbor1", "SpakborDepan")
    spakbor4 = duplicate_object("Brace STR ERR BU03x01x00.25 - SPN-BRC-0002 (stemfie.org)", "Spakbor2", "SpakborDepan")
    spakbor5 = duplicate_object("Brace STR ERR BU03x01x00.25 - SPN-BRC-0002 (stemfie.org)", "Spakbor2", "SpakborDepan")
    spakbor6 = duplicate_object("Brace STR ERR BU04x01x00.25 - SPN-BRC-0003 (stemfie.org)", "Spakbor2", "SpakborDepan")
    if spakbor1:
        rotate_object(spakbor1, x_degrees=-90, y_degrees=63.9379, z_degrees=90)
        set_location(spakbor1, 38.9612, 72.5052, 34.7869 )
    if spakbor2:
        rotate_object(spakbor2, x_degrees=-90, y_degrees=118.86, z_degrees=90)
        set_location(spakbor2, 38.9612, 47.6193, 34.7869 )
    if spakbor3:
        rotate_object(spakbor3, x_degrees=90, y_degrees=-180, z_degrees=-90)
        set_location(spakbor3, 38.9612, 84.2188, 13.0101  )
    if spakbor4:
        rotate_object(spakbor4, x_degrees=-90, y_degrees=118.86, z_degrees=-90)
        set_location(spakbor4, -45.1019, 72.5052, 34.7869 )
    if spakbor5:
        rotate_object(spakbor5, x_degrees=-90, y_degrees=63.9379, z_degrees=-90)
        set_location(spakbor5, -45.4662, 47.6193, 34.7869 )
    if spakbor6:
        rotate_object(spakbor6, x_degrees=90, y_degrees=180, z_degrees=90)
        set_location(spakbor6, -45.076,121.936,13.0101  )

    kapmobil1 = duplicate_object("Brace STR ERR BU05x01x00.25 - SPN-BRC-0004 (stemfie.org)", "Kapmobil1", "KapMobil")
    kapmobil2 = duplicate_object("Brace STR ERR BU05x01x00.25 - SPN-BRC-0004 (stemfie.org)", "Kapmobil1", "KapMobil")
    kapmobil3 = duplicate_object("Brace STR ERR BU05x01x00.25 - SPN-BRC-0004 (stemfie.org)", "Kapmobil1", "KapMobil")
    kapmobil4 = duplicate_object("Brace STR ERR BU05x01x00.25 - SPN-BRC-0004 (stemfie.org)", "Kapmobil1", "KapMobil")
    kapmobil5 = duplicate_object("Brace STR ERR BU05x01x00.25 - SPN-BRC-0004 (stemfie.org)", "Kapmobil1", "KapMobil")
    kapmobil6 = duplicate_object("Brace STR ERR BU05x01x00.25 - SPN-BRC-0004 (stemfie.org)", "Kapmobil1", "KapMobil")
    kapmobil7 = duplicate_object("Brace STR ERR BU05x01x00.25 - SPN-BRC-0004 (stemfie.org)", "Kapmobil1", "KapMobil")
    if kapmobil1:
        rotate_object(kapmobil1, x_degrees=0, y_degrees=0, z_degrees=90 )
        set_location(kapmobil1, -32.9743, 47.6834, 939.653)
    if kapmobil2:
        rotate_object(kapmobil2, x_degrees=0, y_degrees=0, z_degrees=90 )
        set_location(kapmobil2, -20.715, 47.6834, 39.653)
    if kapmobil3:
        rotate_object(kapmobil3, x_degrees=0, y_degrees=0, z_degrees=90 )
        set_location(kapmobil3, -7.99311, 47.6834, 39.653)
    if kapmobil4:
        rotate_object(kapmobil4, x_degrees=0, y_degrees=0, z_degrees=90 )
        set_location(kapmobil4, 4.2662, 47.6834, 39.653)
    if kapmobil5:
        rotate_object(kapmobil5, x_degrees=0, y_degrees=0, z_degrees=90 )
        set_location(kapmobil5, 16.9881, 47.6834, 39.653 )
    if kapmobil6:
        rotate_object(kapmobil6, x_degrees=0, y_degrees=0, z_degrees=90 )
        set_location(kapmobil6, 29.2474, 47.6834, 39.653 )  
    if kapmobil7:
        rotate_object(kapmobil7, x_degrees=0, y_degrees=0, z_degrees=90 )
        set_location(kapmobil7, -32.7106, 47.6834, 39.653 )    

    kacaDepan1 = duplicate_object("Beam STR ESS BU06x01x01 - SPN-BEM-0043 (stemfie.org)", "KacaDepan1", "KacaDepan")
    kacaDepan2 = duplicate_object("Beam STR ESS BU06x01x01 - SPN-BEM-0043 (stemfie.org)", "KacaDepan1", "KacaDepan")
    kacaDepan3 = duplicate_object("Beam STR ESS BU06x01x01 - SPN-BEM-0043 (stemfie.org)", "KacaDepan1", "KacaDepan")
    kacaDepan4 = duplicate_object("Beam STR ESS BU06x01x01 - SPN-BEM-0043 (stemfie.org)", "KacaDepan1", "KacaDepan")
    kacaDepan5 = duplicate_object("Brace STR ERR BU04x01x00.25 - SPN-BRC-0003 (stemfie.org)", "KacaDepan1", "KacaDepan")
    kacaDepan6 = duplicate_object("Brace STR ERR BU04x01x00.25 - SPN-BRC-0003 (stemfie.org)", "KacaDepan1", "KacaDepan")
    kacaDepan7 = duplicate_object("Brace STR ERR BU04x01x00.25 - SPN-BRC-0003 (stemfie.org)", "KacaDepan1", "KacaDepan")
    kacaDepan8 = duplicate_object("Brace STR ERR BU04x01x00.25 - SPN-BRC-0003 (stemfie.org)", "KacaDepan1", "KacaDepan")
    if kacaDepan1:
        rotate_object(kacaDepan1, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(kacaDepan1, -38.942, 84.6455, 39.7767)
    if kacaDepan2:
        rotate_object(kacaDepan2, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(kacaDepan2, -38.942, 109.216, 61.6338)
    if kacaDepan3:
        rotate_object(kacaDepan3, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(kacaDepan3, -38.942, 121.486, 61.6338)
    if kacaDepan4:
        rotate_object(kacaDepan4, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(kacaDepan4, -38.942, 134.035, 61.6338)
    if kacaDepan5:
        rotate_object(kacaDepan5, x_degrees=90, y_degrees=118.833, z_degrees=90)
        set_location(kacaDepan5, 38.0616, 102.922, 67.8693)
    if kacaDepan6:
        rotate_object(kacaDepan6, x_degrees=90, y_degrees=118.833, z_degrees=90)
        set_location(kacaDepan6, -44.9312, 102.922, 67.8693)
    if kacaDepan7:
        rotate_object(kacaDepan7, x_degrees=90, y_degrees=180, z_degrees=90)
        set_location(kacaDepan7, 38.0616, 140.504, 67.8693)
    if kacaDepan8:
        rotate_object(kacaDepan8, x_degrees=90, y_degrees=180, z_degrees=90)
        set_location(kacaDepan8, -45.2341, 140.504, 67.8693)

    bandepan1 = duplicate_object("Spacer FRE BU00.25x01.00 - SPN-SPR-0050 (stemfie.org)", "bandepan", "BanDepan")
    bandepan2 = duplicate_object("Spacer FRE BU00.25x01.00 - SPN-SPR-0050 (stemfie.org)", "bandepan", "BanDepan")
    bandepan3 = duplicate_object("Spacer FRE BU00.25x01.00 - SPN-SPR-0050 (stemfie.org)", "bandepan", "BanDepan")
    bandepan4 = duplicate_object("Spacer FRE BU00.25x01.00 - SPN-SPR-0050 (stemfie.org)", "bandepan", "BanDepan")
    bandepan5 = duplicate_object("Spacer FRE BU00.25x01.00 - SPN-SPR-0050 (stemfie.org)", "bandepan", "BanDepan")
    bandepan6 = duplicate_object("Spacer FRE BU00.25x01.00 - SPN-SPR-0050 (stemfie.org)", "bandepan", "BanDepan")
    if bandepan1:
        rotate_object(bandepan1, x_degrees=90, y_degrees=180, z_degrees=90)
        set_location(bandepan1, 41.808, 59.8251, 14.1781)
        resize_object(bandepan1, 2, 2, 1)
    if bandepan2:
        rotate_object(bandepan2, x_degrees=90, y_degrees=180, z_degrees=90)
        set_location(bandepan2, 38.59 , 59.8251, 14.1781)
        resize_object(bandepan2, 2, 2, 1)
    if bandepan3:
        rotate_object(bandepan3, x_degrees=90, y_degrees=180, z_degrees=90)
        set_location(bandepan3, 35.0344 , 59.8251, 14.1781)
        resize_object(bandepan3, 2, 2, 1)
    if bandepan4:
        rotate_object(bandepan4, x_degrees=90, y_degrees=180, z_degrees=90)
        set_location(bandepan4, -37.31, 59.8251, 14.1781)
        resize_object(bandepan4, 2, 2, 1)
    if bandepan5:
        rotate_object(bandepan5, x_degrees=90, y_degrees=180, z_degrees=90)
        set_location(bandepan5, -40.5281, 59.8251, 14.1781)
        resize_object(bandepan5, 2, 2, 1)
    if bandepan6:
        rotate_object(bandepan6, x_degrees=90, y_degrees=180, z_degrees=90)
        set_location(bandepan6, -44.0837, 59.8251, 14.1781)
        resize_object(bandepan6, 2, 2, 1)


    bpy.context.scene.frame_start = 1
    frame_middle = 200
    bpy.context.scene.frame_end = 400

    moving_objects = []
    all_objects = bpy.context.scene.objects
    for obj in all_objects:
        if obj.name != 'Point' and obj.name != 'Camera':
            moving_objects.append(obj)

    distance = 200
    
    for obj in moving_objects:
        obj.location.y -= 0
        collection_name = "BanDepan"
        collection = bpy.data.collections.get(collection_name)
        if collection:
            if obj.name in collection.objects:
                obj.rotation_euler = (obj.rotation_euler)
        obj.keyframe_insert(data_path="location", frame=bpy.context.scene.frame_start)
        obj.keyframe_insert(data_path="rotation_euler", frame=bpy.context.scene.frame_start)
        
        obj.location.y -= distance
        collection_name = "BanDepan"
        collection = bpy.data.collections.get(collection_name)
        if collection:
            if obj.name in collection.objects:
                obj.rotation_euler = (obj.rotation_euler.x, ((-360 * (bpy.context.scene.frame_end / bpy.context.scene.frame_end)) * (3.14159 / 180)), obj.rotation_euler.z)

        obj.keyframe_insert(data_path="location", frame=frame_middle)
        obj.keyframe_insert(data_path="rotation_euler", frame=frame_middle)

        for fcurve in obj.animation_data.action.fcurves:
            for keyframe in fcurve.keyframe_points:
                keyframe.interpolation = 'LINEAR'
        
        obj.location.x += random.uniform(1, 100)
        obj.location.y -= random.uniform(1, 100)
        obj.location.z += random.uniform(1, 100)
        random_rotation_x = (random.uniform(1, 360) * (bpy.context.scene.frame_end / bpy.context.scene.frame_end)) * (3.14159 / 180)
        random_rotation_y = (random.uniform(1, 360) * (bpy.context.scene.frame_end / bpy.context.scene.frame_end)) * (3.14159 / 180)
        random_rotation_z = (random.uniform(1, 360) * (bpy.context.scene.frame_end / bpy.context.scene.frame_end)) * (3.14159 / 180)
        obj.rotation_euler = (random_rotation_x, random_rotation_y, random_rotation_z)
        obj.keyframe_insert(data_path="location", frame=bpy.context.scene.frame_end)
        obj.keyframe_insert(data_path="rotation_euler", frame=bpy.context.scene.frame_end)

    bpy.ops.screen.animation_play()