import bpy
import math
from mathutils import Vector, Matrix
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

def is_object_in_collection(obj, collection):
    # Cek jika objek ada di dalam koleksi atau koleksi bersarang
    if collection is None:
        return False
    if obj.name in collection.objects:
        return True
    for child_collection in collection.children:
        if is_object_in_collection(obj, child_collection):
            return True
    return False

def rotate_object_around_point(obj, point, angle):
    if obj is None:
        return

    obj_location = Vector(obj.location)

    to_obj_vector = obj_location - point

    rotation_matrix = Matrix.Rotation(angle, 4, 'Z')  # Rotasi pada sumbu Z

    new_vector = rotation_matrix @ to_obj_vector
    obj.location = point + new_vector

def get_first_collection_name_of_object(obj):
    if obj is None:
        return None 

    if obj.users_collection:
        return obj.users_collection[0].name
    else:
        return None

# Example usage:
if __name__ == "__main__":
    # Clear 
    all_objects = bpy.context.scene.objects
    for obj in all_objects:
        collection_name = "BanDepan"
        collection_template = bpy.data.collections.get("Sample STEMFIE parts (unhide collections)")
        collection_aspal = bpy.data.collections.get("Aspal")
        collection_setup = bpy.data.collections.get("SetUp")
        if not (is_object_in_collection(obj, collection_template) or is_object_in_collection(obj, collection_aspal) or is_object_in_collection(obj, collection_setup)):
            bpy.data.objects.remove(obj)


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
    kacaDepan9 = duplicate_object("Brace STR ERR BU04x01x00.25 - SPN-BRC-0003 (stemfie.org)", "KacaDepan1", "KacaDepan")
    kacaDepan10 = duplicate_object("Brace STR ERR BU04x01x00.25 - SPN-BRC-0003 (stemfie.org)", "KacaDepan1", "KacaDepan")
    kacaDepan11 = duplicate_object("Brace STR ERR BU04x01x00.25 - SPN-BRC-0003 (stemfie.org)", "KacaDepan1", "KacaDepan")
    kacaDepan12 = duplicate_object("Brace STR ERR BU05x01x00.25 - SPN-BRC-0004 (stemfie.org)", "KacaDepan1", "KacaDepan")
    kacaDepan13 = duplicate_object("Brace STR ERR BU04x01x00.25 - SPN-BRC-0003 (stemfie.org)", "KacaDepan1", "KacaDepan")
    kacaDepan14 = duplicate_object("Brace STR ERR BU05x01x00.25 - SPN-BRC-0004 (stemfie.org)", "KacaDepan1", "KacaDepan")
    kacaDepan15 = duplicate_object("Brace STR ERR BU04x01x00.25 - SPN-BRC-0003 (stemfie.org)", "KacaDepan1", "KacaDepan")
    kacaDepan16 = duplicate_object("Brace STR ERR BU05x01x00.25 - SPN-BRC-0004 (stemfie.org)", "KacaDepan1", "KacaDepan")
    if kacaDepan1:
        rotate_object(kacaDepan1, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(kacaDepan1, -40.1022, 83.6986, 39.7767)
    if kacaDepan2:
        rotate_object(kacaDepan2, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(kacaDepan2, -40.3252 , 115.664 , 65.2492)
    if kacaDepan3:
        rotate_object(kacaDepan3, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(kacaDepan3, -40.3252 , 127.714, 65.2492 )
    if kacaDepan4:
        rotate_object(kacaDepan4, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(kacaDepan4, -40.3252 , 140.48, 65.2492)
    if kacaDepan5:
        rotate_object(kacaDepan5, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(kacaDepan5, -40.3252 , 103.604, 65.2492)
    if kacaDepan6:
        rotate_object(kacaDepan6, x_degrees=-90, y_degrees=111, z_degrees=90)
        set_location(kacaDepan6, 39.1146 , 98.1226, 70.4194)
    if kacaDepan7:
        rotate_object(kacaDepan7, x_degrees=90, y_degrees=110, z_degrees=90)
        set_location(kacaDepan7, -45.1019, 98.1226, 70.4194)
    if kacaDepan8:
        rotate_object(kacaDepan8, x_degrees=90, y_degrees=90, z_degrees=90)
        set_location(kacaDepan8, -51.1934 , 147.257 , 71.3514)
    if kacaDepan9:
        rotate_object(kacaDepan9, x_degrees=-90, y_degrees=90, z_degrees=90)
        set_location(kacaDepan9, 44.9366  , 147.257 , 71.3514)
    if kacaDepan10:
        rotate_object(kacaDepan10, x_degrees=-90, y_degrees=180, z_degrees=90)
        set_location(kacaDepan10, 39.2498  , 147.257 , 71.3514)
    if kacaDepan11:
        rotate_object(kacaDepan11, x_degrees=-90, y_degrees=180, z_degrees=90)
        set_location(kacaDepan11, -41.9444   , 147.257 , 71.3514)
    if kacaDepan12:
        rotate_object(kacaDepan12, x_degrees=-90, y_degrees=180, z_degrees=90)
        set_location(kacaDepan12, 41.7022    , 147.616 , 71.3714)
    if kacaDepan13:
        rotate_object(kacaDepan13, x_degrees=90, y_degrees=90, z_degrees=90)
        set_location(kacaDepan13, -51.1934, 147.344, 71.5544 )
    if kacaDepan14:
        rotate_object(kacaDepan14, x_degrees=90, y_degrees=180, z_degrees=90)
        set_location(kacaDepan14, -48.3361, 147.616, 71.365 )
    if kacaDepan15:
        rotate_object(kacaDepan15, x_degrees=-90, y_degrees=90, z_degrees=90)
        set_location(kacaDepan15, 44.9366, 147.265, 71.5544  )
    if kacaDepan16:
        rotate_object(kacaDepan16, x_degrees=-90, y_degrees=180, z_degrees=90)
        set_location(kacaDepan16, 41.7022, 147.616, 71.3714 )

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

    banbelakang1 = duplicate_object("Spacer FRE BU00.25x01.00 - SPN-SPR-0050 (stemfie.org)", "banbelakang", "BanBelakang_AFRIZA")
    banbelakang2 = duplicate_object("Spacer FRE BU00.25x01.00 - SPN-SPR-0050 (stemfie.org)", "banbelakang", "BanBelakang_AFRIZA")
    banbelakang3 = duplicate_object("Spacer FRE BU00.25x01.00 - SPN-SPR-0050 (stemfie.org)", "banbelakang", "BanBelakang_AFRIZA")
    banbelakang4 = duplicate_object("Spacer FRE BU00.25x01.00 - SPN-SPR-0050 (stemfie.org)", "banbelakang", "BanBelakang_AFRIZA")
    banbelakang5 = duplicate_object("Spacer FRE BU00.25x01.00 - SPN-SPR-0050 (stemfie.org)", "banbelakang", "BanBelakang_AFRIZA")
    banbelakang6 = duplicate_object("Spacer FRE BU00.25x01.00 - SPN-SPR-0050 (stemfie.org)", "banbelakang", "BanBelakang_AFRIZA")
    if banbelakang1:
        rotate_object(banbelakang1, x_degrees=90, y_degrees=180, z_degrees=90)
        set_location(banbelakang1, 35.0344, 159.433, 14.1781)
        resize_object(banbelakang1, 2, 2, 1)
    if banbelakang2:
        rotate_object(banbelakang2, x_degrees=90, y_degrees=180, z_degrees=90)
        set_location(banbelakang2, 38.59 , 159.433, 14.1781)
        resize_object(banbelakang2, 2, 2, 1)
    if banbelakang3:
        rotate_object(banbelakang3, x_degrees=90, y_degrees=180, z_degrees=90)
        set_location(banbelakang3, 41.808 , 159.433, 14.1781)
        resize_object(banbelakang3, 2, 2, 1)
    if banbelakang4:
        rotate_object(banbelakang4, x_degrees=90, y_degrees=180, z_degrees=90)
        set_location(banbelakang4, -37.31, 159.433, 14.1781)
        resize_object(banbelakang4, 2, 2, 1)
    if banbelakang5:
        rotate_object(banbelakang5, x_degrees=90, y_degrees=180, z_degrees=90)
        set_location(banbelakang5, -40.5281, 159.433, 14.1781)
        resize_object(banbelakang5, 2, 2, 1)
    if banbelakang6:
        rotate_object(banbelakang6, x_degrees=90, y_degrees=180, z_degrees=90)
        set_location(banbelakang6, -44.0837, 159.433, 14.1781)
        resize_object(banbelakang6, 2, 2, 1)
        
    spakborBelakang1 = duplicate_object("Brace STR ERR BU03x01x00.25 - SPN-BRC-0002 (stemfie.org)", "Spakbor", "SpakborBelakang_AFRIZA")
    spakborBelakang2 = duplicate_object("Brace STR ERR BU03x01x00.25 - SPN-BRC-0002 (stemfie.org)", "Spakbor", "SpakborBelakang_AFRIZA")
    spakborBelakang3 = duplicate_object("Brace STR ERR BU03x01x00.25 - SPN-BRC-0002 (stemfie.org)", "Spakbor", "SpakborBelakang_AFRIZA")
    spakborBelakang4 = duplicate_object("Brace STR ERR BU03x01x00.25 - SPN-BRC-0002 (stemfie.org)", "Spakbor", "SpakborBelakang_AFRIZA")
    if spakborBelakang1:
        rotate_object(spakborBelakang1, x_degrees=-90, y_degrees=63.9379, z_degrees=90)
        set_location(spakborBelakang1, -45.2944, 172.54, 34.7869 )
    if spakborBelakang2:
        rotate_object(spakborBelakang2, x_degrees=-90, y_degrees=122, z_degrees=90)
        set_location(spakborBelakang2, 38.9612, 147.166, 34.0283 )
    if spakborBelakang3:
        rotate_object(spakborBelakang3, x_degrees=-90, y_degrees=63.9379, z_degrees=90)
        set_location(spakborBelakang3, 38.9612, 172.54, 34.7869  )
    if spakborBelakang4:
        rotate_object(spakborBelakang4, x_degrees=-90, y_degrees=122, z_degrees=90)
        set_location(spakborBelakang4, -45.2944, 147.166, 34.0283 )
  
    kapBelakang1 = duplicate_object("Beam STR ESS BU07x01x01 - SPN-BEM-0044 (stemfie.org)", "KapBelakang", "KapBelakang_AFRIZA")
    kapBelakang2 = duplicate_object("Beam STR ESS BU07x01x01 - SPN-BEM-0044 (stemfie.org)", "KapBelakang", "KapBelakang_AFRIZA")
    kapBelakang3 = duplicate_object("Brace STR ERR BU03x01x00.25 - SPN-BRC-0002 (stemfie.org)", "KapBelakang", "KapBelakang_AFRIZA")
    kapBelakang4 = duplicate_object("Brace STR ERR BU03x01x00.25 - SPN-BRC-0002 (stemfie.org)", "KapBelakang", "KapBelakang_AFRIZA")
    kapBelakang5 = duplicate_object("Brace STR ERR BU03x01x00.25 - SPN-BRC-0002 (stemfie.org)", "KapBelakang", "KapBelakang_AFRIZA")
    kapBelakang6 = duplicate_object("Brace STR ERR BU03x01x00.25 - SPN-BRC-0002 (stemfie.org)", "KapBelakang", "KapBelakang_AFRIZA")
    kapBelakang7 = duplicate_object("Brace STR ERR BU03x01x00.25 - SPN-BRC-0002 (stemfie.org)", "KapBelakang", "KapBelakang_AFRIZA")
    kapBelakang8 = duplicate_object("Beam STR ESS BU05x01x01 - SPN-BEM-0042 (stemfie.org)", "KapBelakang", "KapBelakang_AFRIZA")
    kapBelakang9 = duplicate_object("Beam STR ESS BU06x01x01 - SPN-BEM-0043 (stemfie.org)", "KapBelakang", "KapBelakang_AFRIZA")
    if kapBelakang1:
        rotate_object(kapBelakang1, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(kapBelakang1, -47.1192 , 153.166 , 53.2588  )
    if kapBelakang2:
        rotate_object(kapBelakang2, x_degrees=-0, y_degrees=0, z_degrees=0)
        set_location(kapBelakang2, -47.1192, 153.166 , 41.2748 )
    if kapBelakang3:
        rotate_object(kapBelakang3, x_degrees=-180, y_degrees=180, z_degrees=270)
        set_location(kapBelakang3, 21.3482, 159.211 , 40.8184  )
    if kapBelakang4:
        rotate_object(kapBelakang4, x_degrees=-180, y_degrees=180, z_degrees=270)
        set_location(kapBelakang4, 8.89246 , 159.211, 40.8184 )
    if kapBelakang5:
        rotate_object(kapBelakang5, x_degrees=-180, y_degrees=180, z_degrees=270)
        set_location(kapBelakang5, -3.67277 , 159.211, 40.8184 )
    if kapBelakang6:
        rotate_object(kapBelakang6, x_degrees=-180, y_degrees=180, z_degrees=270)
        set_location(kapBelakang6, -16.3416 , 159.211, 40.8184 )
    if kapBelakang7:
        rotate_object(kapBelakang7, x_degrees=-180, y_degrees=180, z_degrees=270)
        set_location(kapBelakang7, -29.1607, 159.211, 40.8184 )
    if kapBelakang8:
        rotate_object(kapBelakang8, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(kapBelakang8, -34.8818 , 178, 29.6415 )
    if kapBelakang9:
        rotate_object(kapBelakang9, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(kapBelakang9, -40.3483 , 178.498 , 17.0795 )
        
        
    kerangkaBelakang1 = duplicate_object("Brace STR ERR BU03x01x00.25 - SPN-BRC-0002 (stemfie.org)", "KerangkaBelakang", "KerangkaBelakang_AFRIZA")    
    kerangkaBelakang2 = duplicate_object("Brace STR ERR BU02x01x00.25 - SPN-BRC-0001 (stemfie.org)", "KerangkaBelakang", "KerangkaBelakang_AFRIZA")
    kerangkaBelakang3 = duplicate_object("Brace STR ERR BU06x01x00.25 - SPN-BRC-0005 (stemfie.org)", "KerangkaBelakang", "KerangkaBelakang_AFRIZA")
    kerangkaBelakang4 = duplicate_object("Brace STR ERR BU03x01x00.25 - SPN-BRC-0002 (stemfie.org)", "KerangkaBelakang", "KerangkaBelakang_AFRIZA")
    kerangkaBelakang5 = duplicate_object("Brace STR ERR BU03x01x00.25 - SPN-BRC-0002 (stemfie.org)", "KerangkaBelakang", "KerangkaBelakang_AFRIZA")
    kerangkaBelakang6 = duplicate_object("Brace STR ERR BU02x01x00.25 - SPN-BRC-0001 (stemfie.org)", "KerangkaBelakang", "KerangkaBelakang_AFRIZA")
    kerangkaBelakang7 = duplicate_object("Brace STR ERR BU06x01x00.25 - SPN-BRC-0005 (stemfie.org)", "KerangkaBelakang", "KerangkaBelakang_AFRIZA")
    kerangkaBelakang8 = duplicate_object("Brace STR ERR BU03x01x00.25 - SPN-BRC-0002 (stemfie.org)", "KerangkaBelakang", "KerangkaBelakang_AFRIZA")
    kerangkaBelakang9 = duplicate_object("Brace STR ERR BU02x01x00.25 - SPN-BRC-0001 (stemfie.org)", "KerangkaBelakang", "KerangkaBelakang_AFRIZA")
    kerangkaBelakang10 = duplicate_object("Brace STR ERR BU03x01x00.25 - SPN-BRC-0002 (stemfie.org)", "KerangkaBelakang", "KerangkaBelakang_AFRIZA")
    kerangkaBelakang11 = duplicate_object("Brace STR ERR BU03x01x00.25 - SPN-BRC-0002 (stemfie.org)", "KerangkaBelakang", "KerangkaBelakang_AFRIZA")
    
    if kerangkaBelakang1:
        rotate_object(kerangkaBelakang1, x_degrees=-90, y_degrees=180, z_degrees=90)
        set_location(kerangkaBelakang1, 31.6329, 184.357, 34.7869 )
    if kerangkaBelakang2:
        rotate_object(kerangkaBelakang2, x_degrees=-90, y_degrees=180, z_degrees=90)
        set_location(kerangkaBelakang2, 39.2498 , 123.327, 34.9549 )
    if kerangkaBelakang3:
        rotate_object(kerangkaBelakang3, x_degrees=90, y_degrees=0, z_degrees=-90)
        set_location(kerangkaBelakang3, 35.999, 184.69, 34.7576  )
    if kerangkaBelakang4:
        rotate_object(kerangkaBelakang4, x_degrees=90, y_degrees=180, z_degrees=90)
        set_location(kerangkaBelakang4, -48.3361, 159.374, 34.7869  )
    if kerangkaBelakang5:
        rotate_object(kerangkaBelakang5, x_degrees=-90, y_degrees=180, z_degrees=90)
        set_location(kerangkaBelakang5, -34.9049, 184.357, 34.7869 )
    if kerangkaBelakang6:
        rotate_object(kerangkaBelakang6, x_degrees=90, y_degrees=180, z_degrees=90)
        set_location(kerangkaBelakang6, -48.3361, 159.374 , 34.7869 )
    if kerangkaBelakang7:
        rotate_object(kerangkaBelakang7, x_degrees=-90, y_degrees=0, z_degrees=-90)
        set_location(kerangkaBelakang7, -41.9444, 184.69, 34.7576  )
    if kerangkaBelakang8:
        rotate_object(kerangkaBelakang8, x_degrees=-90, y_degrees=90, z_degrees=-90)
        set_location(kerangkaBelakang8, -51.6719 , 159.441 , 59.4747  )
    if kerangkaBelakang9:
        rotate_object(kerangkaBelakang9, x_degrees=90, y_degrees=180, z_degrees=-90)
        set_location(kerangkaBelakang9, -43.2268  , 109.125 , 34.9549   )
    if kerangkaBelakang10:
        rotate_object(kerangkaBelakang10, x_degrees=-90, y_degrees=180, z_degrees=90)
        set_location(kerangkaBelakang10, 42.2972  , 159.374  , 34.7869    )
    if kerangkaBelakang11:
        rotate_object(kerangkaBelakang11, x_degrees=-90, y_degrees=90, z_degrees=90)
        set_location(kerangkaBelakang11, 44.837  , 159.441   , 59.4747     )

    Scrup1 = duplicate_object("Beam STR ESS BU01x01x01 - SPN-BEM-0038 (stemfie.org)", "Scrup1", "KebutuhanScrup")
    Scrup2 = duplicate_object("Beam STR ESS BU01x01x01 - SPN-BEM-0038 (stemfie.org)", "Scrup1", "KebutuhanScrup")
    Scrup3 = duplicate_object("Beam STR ESS BU01x01x01 - SPN-BEM-0038 (stemfie.org)", "Scrup1", "KebutuhanScrup")
    Scrup4 = duplicate_object("Beam STR ESS BU01x01x01 - SPN-BEM-0038 (stemfie.org)", "Scrup1", "KebutuhanScrup")
    Scrup5 = duplicate_object("Nut CPN RH BU1x1.00 - SPN-NUT-0035 (stemfie.org)", "Scrup2", "KebutuhanScrup")
    Scrup6 = duplicate_object("Nut CPN RH BU1x1.00 - SPN-NUT-0035 (stemfie.org)", "Scrup2", "KebutuhanScrup")
    Scrup7 = duplicate_object("Nut CPN RH BU1x1.00 - SPN-NUT-0035 (stemfie.org)", "Scrup2", "KebutuhanScrup")
    Scrup8 = duplicate_object("Nut CPN RH BU1x1.00 - SPN-NUT-0035 (stemfie.org)", "Scrup2", "KebutuhanScrup")
    Scrup9 = duplicate_object("Nut PH CL BU1x5mm - SPN-NUT-0018 (stemfie.org)", "Scrup3", "KebutuhanScrup")
    Scrup10 = duplicate_object("Nut PH CL BU1x5mm - SPN-NUT-0018 (stemfie.org)", "Scrup3", "KebutuhanScrup")
    Scrup11 = duplicate_object("Nut PH CL BU1x5mm - SPN-NUT-0018 (stemfie.org)", "Scrup3", "KebutuhanScrup")
    Scrup12 = duplicate_object("Nut PH CL BU1x5mm - SPN-NUT-0018 (stemfie.org)", "Scrup3", "KebutuhanScrup")
    Scrup13 = duplicate_object("Screw RHD RH BU00.25 - SPN-SCR-0081 (stemfie.org)", "Scrup4", "KebutuhanScrup")
    Scrup14 = duplicate_object("Screw RHD RH BU00.25 - SPN-SCR-0081 (stemfie.org)", "Scrup4", "KebutuhanScrup")
    Scrup15 = duplicate_object("Screw RHD RH BU00.50 - SPN-SCR-0082 (stemfie.org)", "Scrup5", "KebutuhanScrup")
    Scrup16 = duplicate_object("Screw RHD RH BU00.50 - SPN-SCR-0082 (stemfie.org)", "Scrup5", "KebutuhanScrup")
    Scrup17 = duplicate_object("Screw RHD RH BU00.50 - SPN-SCR-0082 (stemfie.org)", "Scrup5", "KebutuhanScrup")
    Scrup18 = duplicate_object("Screw RHD RH BU00.50 - SPN-SCR-0082 (stemfie.org)", "Scrup5", "KebutuhanScrup")
    Scrup19 = duplicate_object("Screw RHD RH BU00.50 - SPN-SCR-0082 (stemfie.org)", "Scrup5", "KebutuhanScrup")
    Scrup20 = duplicate_object("Screw RHD RH BU00.50 - SPN-SCR-0082 (stemfie.org)", "Scrup5", "KebutuhanScrup")
    Scrup21 = duplicate_object("Screw RHD RH BU00.50 - SPN-SCR-0082 (stemfie.org)", "Scrup5", "KebutuhanScrup")
    Scrup22 = duplicate_object("Screw RHD RH BU00.50 - SPN-SCR-0082 (stemfie.org)", "Scrup5", "KebutuhanScrup")
    Scrup23 = duplicate_object("Screw RHD RH BU00.50 - SPN-SCR-0082 (stemfie.org)", "Scrup5", "KebutuhanScrup")
    Scrup24 = duplicate_object("Screw RHD RH BU00.50 - SPN-SCR-0082 (stemfie.org)", "Scrup5", "KebutuhanScrup")
    Scrup25 = duplicate_object("Screw RHD RH BU00.75 - SPN-SCR-0083 (stemfie.org)", "Scrup6", "KebutuhanScrup")
    Scrup26 = duplicate_object("Screw RHD RH BU00.75 - SPN-SCR-0083 (stemfie.org)", "Scrup6", "KebutuhanScrup")
    Scrup27 = duplicate_object("Screw RHD RH BU00.75 - SPN-SCR-0083 (stemfie.org)", "Scrup6", "KebutuhanScrup")
    Scrup28 = duplicate_object("Screw RHD RH BU00.75 - SPN-SCR-0083 (stemfie.org)", "Scrup6", "KebutuhanScrup")
    Scrup29 = duplicate_object("Screw RHD RH BU00.75 - SPN-SCR-0083 (stemfie.org)", "Scrup6", "KebutuhanScrup")
    Scrup30 = duplicate_object("Screw RHD RH BU00.75 - SPN-SCR-0083 (stemfie.org)", "Scrup6", "KebutuhanScrup")
    Scrup31 = duplicate_object("Screw RHD RH BU00.75 - SPN-SCR-0083 (stemfie.org)", "Scrup6", "KebutuhanScrup")
    Scrup32 = duplicate_object("Screw RHD RH BU00.75 - SPN-SCR-0083 (stemfie.org)", "Scrup6", "KebutuhanScrup")
    Scrup33 = duplicate_object("Screw RHD RH BU00.75 - SPN-SCR-0083 (stemfie.org)", "Scrup6", "KebutuhanScrup")
    Scrup34 = duplicate_object("Screw RHD RH BU00.75 - SPN-SCR-0083 (stemfie.org)", "Scrup6", "KebutuhanScrup")
    Scrup35 = duplicate_object("Screw RHD RH BU00.75 - SPN-SCR-0083 (stemfie.org)", "Scrup6", "KebutuhanScrup")
    Scrup36 = duplicate_object("Screw RHD RH BU00.75 - SPN-SCR-0083 (stemfie.org)", "Scrup6", "KebutuhanScrup")
    Scrup38 = duplicate_object("Screw RHD RH BU00.75 - SPN-SCR-0083 (stemfie.org)", "Scrup6", "KebutuhanScrup")
    Scrup39 = duplicate_object("Screw RHD RH BU00.75 - SPN-SCR-0083 (stemfie.org)", "Scrup6", "KebutuhanScrup")
    Scrup41 = duplicate_object("Screw RHD RH BU00.75 - SPN-SCR-0083 (stemfie.org)", "Scrup6", "KebutuhanScrup")
    Scrup42 = duplicate_object("Screw RHD RH BU00.75 - SPN-SCR-0083 (stemfie.org)", "Scrup6", "KebutuhanScrup")
    Scrup44 = duplicate_object("Screw RHD RH BU00.75 - SPN-SCR-0083 (stemfie.org)", "Scrup6", "KebutuhanScrup")
    Scrup45 = duplicate_object("Screw RHD RH BU00.75 - SPN-SCR-0083 (stemfie.org)", "Scrup6", "KebutuhanScrup")
    Scrup46 = duplicate_object("Screw RHD RH BU00.75 - SPN-SCR-0083 (stemfie.org)", "Scrup6", "KebutuhanScrup")
    Scrup48 = duplicate_object("Screw RHD RH BU00.75 - SPN-SCR-0083 (stemfie.org)", "Scrup6", "KebutuhanScrup")
    Scrup49 = duplicate_object("Screw RHD RH BU01.25 - SPN-SCR-0085 (stemfie.org)", "Scrup7", "KebutuhanScrup")
    Scrup50 = duplicate_object("Screw RHD RH BU01.25 - SPN-SCR-0085 (stemfie.org)", "Scrup7", "KebutuhanScrup")
    Scrup51 = duplicate_object("Screw RHD RH BU01.25 - SPN-SCR-0085 (stemfie.org)", "Scrup7", "KebutuhanScrup")
    Scrup52 = duplicate_object("Screw RHD RH BU01.25 - SPN-SCR-0085 (stemfie.org)", "Scrup7", "KebutuhanScrup")
    Scrup53 = duplicate_object("Spacer SPR FXD - BU1.00x0.25 - SPN-SPR-0004 (stemfie.org)", "Scrup8", "KebutuhanScrup")
    Scrup54 = duplicate_object("Spacer SPR FXD - BU1.00x0.25 - SPN-SPR-0004 (stemfie.org)", "Scrup8", "KebutuhanScrup")
    Scrup55 = duplicate_object("Spacer SPR FXD - BU1.00x0.25 - SPN-SPR-0004 (stemfie.org)", "Scrup8", "KebutuhanScrup")
    Scrup56 = duplicate_object("Spacer SPR FXD - BU1.00x0.25 - SPN-SPR-0004 (stemfie.org)", "Scrup8", "KebutuhanScrup")
    Scrup57 = duplicate_object("Spacer SPR FXD - BU1.00x0.25 - SPN-SPR-0004 (stemfie.org)", "Scrup8", "KebutuhanScrup")
    Scrup58 = duplicate_object("Spacer SPR FXD - BU1.00x0.25 - SPN-SPR-0004 (stemfie.org)", "Scrup8", "KebutuhanScrup")
   
    if Scrup1:
        rotate_object(Scrup1, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(Scrup1, 18.0016 , 53.498 , 8.24736   )
    if Scrup2:
        rotate_object(Scrup2, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(Scrup2, -36.9693 , 53.498  , 8.24736 )
    if Scrup3:
        rotate_object(Scrup3, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(Scrup3, 18.0016, 154.271 , 8.24736  )
    if Scrup4:
        rotate_object(Scrup4, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(Scrup4, -36.9693, 153.946, 8.24736 )
    if Scrup5:
        rotate_object(Scrup5, x_degrees=90, y_degrees=45, z_degrees=-90)
        set_location(Scrup5, -36.9157, 59.4115 , 14.6027 )
    if Scrup6:
        rotate_object(Scrup6, x_degrees=90, y_degrees=45, z_degrees=-90)
        set_location(Scrup6, -36.9157 , 159.859 , 14.6027  )
    if Scrup7:
        rotate_object(Scrup7, x_degrees=90, y_degrees=45, z_degrees=90)
        set_location(Scrup7, 31.7229 , 59.4115, 14.6027  )
    if Scrup8:
        rotate_object(Scrup8, x_degrees=90, y_degrees=45, z_degrees=90)
        set_location(Scrup8, 31.7229, 159.859, 14.6027  ) 
    if Scrup9:
        rotate_object(Scrup9, x_degrees=-90, y_degrees=177.789, z_degrees=-90)
        set_location(Scrup9, 39.4386 , 109.754, 35.0896   )
    if Scrup10:
        rotate_object(Scrup10, x_degrees=-90, y_degrees=137.608, z_degrees=-90)
        set_location(Scrup10, 39.4386 , 122.327, 35.2423  )
    if Scrup11:
        rotate_object(Scrup11, x_degrees=-90, y_degrees=137.608, z_degrees=-90)
        set_location(Scrup11, -49.9822 , 122.327, 35.2423  )
    if Scrup12:
        rotate_object(Scrup12, x_degrees=-90, y_degrees=177.789, z_degrees=-90)
        set_location(Scrup12, -49.9822, 109.754, 35.0896 )
    if Scrup13:
        rotate_object(Scrup13, x_degrees=0, y_degrees=180, z_degrees=0)
        set_location(Scrup13, 39.6457 , 89.0854 , 46.4472 )
    if Scrup14:
        rotate_object(Scrup14, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(Scrup14, -45.2395, 89.0854, 46.4472 )
    if Scrup15:
        rotate_object(Scrup15, x_degrees=90, y_degrees=0, z_degrees=0)
        set_location(Scrup15, 32.2531, 109.725, 35.328 )
    if Scrup16:
        rotate_object(Scrup16, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(Scrup16, 35.0904 , 83.6706, 13.4052 )
    if Scrup17:
        rotate_object(Scrup17, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(Scrup17, 35.0904, 134.796, 13.4052  )
    if Scrup18:
        rotate_object(Scrup18, x_degrees=0, y_degrees=180, z_degrees=0)
        set_location(Scrup18, -40.9454 , 83.6706 , 13.4052  )
    if Scrup19:
        rotate_object(Scrup19, x_degrees=0, y_degrees=180, z_degrees=0)
        set_location(Scrup19, -40.9454, 134.435 , 13.4052  )
    if Scrup20:
        rotate_object(Scrup20, x_degrees=45, y_degrees=0, z_degrees=0)
        set_location(Scrup20, 32.2531, 122.51, 35.338 )   
    if Scrup21:
        rotate_object(Scrup21, x_degrees=-45, y_degrees=180, z_degrees=0)
        set_location(Scrup21, -37.2995, 122.51 , 35.338  )
    if Scrup22:
        rotate_object(Scrup22, x_degrees=90, y_degrees=180, z_degrees=0)
        set_location(Scrup22, -37.2995, 109.725 , 35.338 )
    if Scrup23:
        rotate_object(Scrup23, x_degrees=-67.299, y_degrees=180, z_degrees=0)
        set_location(Scrup23, -41.9196 , 97.7149, 70.0181 )
    if Scrup24:
        rotate_object(Scrup24, x_degrees=67.299, y_degrees=0, z_degrees=0)
        set_location(Scrup24, 35.5836, 97.7149 , 70.0181 )
    if Scrup25:
        rotate_object(Scrup25, x_degrees=60, y_degrees=1880, z_degrees=0)
        set_location(Scrup25, 36.471, 184.741 , 34.3928  )
    if Scrup26:
        rotate_object(Scrup26, x_degrees=-60, y_degrees=0, z_degrees=0)
        set_location(Scrup26, -42.2672, 184.751  , 34.3928  )
    if Scrup27:
        rotate_object(Scrup27, x_degrees=60, y_degrees=180, z_degrees=0)
        set_location(Scrup27, 39.2194 , 183.484 , 11.9419 )
    if Scrup28:
        rotate_object(Scrup28, x_degrees=-60, y_degrees=0, z_degrees=0)
        set_location(Scrup28, -45.3106, 183.484  , 11.9419  )
    if Scrup29:
        rotate_object(Scrup29, x_degrees=-60, y_degrees=0, z_degrees=0)
        set_location(Scrup29, -45.486 , 172.54 , 34.3928 )
    if Scrup30:
        rotate_object(Scrup30, x_degrees=60, y_degrees=180, z_degrees=0)
        set_location(Scrup30, 39.2194, 172.387  , 34.3456  )
    if Scrup31:
        rotate_object(Scrup31, x_degrees=-60, y_degrees=180, z_degrees=0)
        set_location(Scrup31, 39.2194 , 47.0461 , 34.3456 )
    if Scrup32:
        rotate_object(Scrup32, x_degrees=-60, y_degrees=180, z_degrees=0)
        set_location(Scrup32, 39.2194 , 40.9918, 23.2081 )
    if Scrup33:
        rotate_object(Scrup33, x_degrees=60, y_degrees=180, z_degrees=0)
        set_location(Scrup33, 39.2194  , 72.9106, 34.3456 )
    if Scrup34:
        rotate_object(Scrup34, x_degrees=-60, y_degrees=0, z_degrees=0)
        set_location(Scrup34, -45.8064  , 72.9106 , 34.3456  )
    if Scrup35:
        rotate_object(Scrup35, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(Scrup35, -45.8064   , 37.1674, 11.9419  )
    if Scrup36:
        rotate_object(Scrup36, x_degrees=-60, y_degrees=0, z_degrees=0)
        set_location(Scrup36, -45.8064  , 47.0461 , 34.3456   )
    if Scrup38:
        rotate_object(Scrup38, x_degrees=0, y_degrees=180, z_degrees=0)
        set_location(Scrup38, 39.2194   , 35.987 , 12.1229   )
    if Scrup39:
        rotate_object(Scrup39, x_degrees=90, y_degrees=0, z_degrees=0)
        set_location(Scrup39, -51.6738    , 147.672, 72.1009  )

#    INI
    if Scrup41:
        rotate_object(Scrup41, x_degrees=90, y_degrees=180, z_degrees=0)
        set_location(Scrup41, 45.7305    , 37.1674, 147.662   )
    if Scrup42:
        rotate_object(Scrup42, x_degrees=90, y_degrees=180, z_degrees=0)
        set_location(Scrup42, 45.7305    , 147.672 , 72.1009   )
    if Scrup44:
        rotate_object(Scrup44, x_degrees=90, y_degrees=0, z_degrees=0)
        set_location(Scrup44, -51.9665   , 159.848 , 33.8304  )
    if Scrup45:
        rotate_object(Scrup45, x_degrees=90, y_degrees=0, z_degrees=0)
        set_location(Scrup45, -51.9665    , 159.848 , 46.7133   )
    if Scrup46:
        rotate_object(Scrup46, x_degrees=90, y_degrees=180, z_degrees=0)
        set_location(Scrup46, 45.7305     , 159.848 ,46.7133    )
#        INI
    if Scrup48:
        rotate_object(Scrup48, x_degrees=90, y_degrees=0, z_degrees=0)
        set_location(Scrup48, 45.7305    , 159.848 , 159.838   )
    if Scrup49:
        rotate_object(Scrup49, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(Scrup49, 18.3354     , 58.5801 , 14.1781   )
    if Scrup50:
        rotate_object(Scrup50, x_degrees=90, y_degrees=0, z_degrees=0)
        set_location(Scrup50, 17.7278     , 159.353 , 14.1781   )
    if Scrup51:
        rotate_object(Scrup51, x_degrees=90, y_degrees=0, z_degrees=-180)
        set_location(Scrup51, -24.1587     , 58.5801 , 14.1781    )
    if Scrup52:
        rotate_object(Scrup52, x_degrees=0, y_degrees=0, z_degrees=-180)
        set_location(Scrup52, -24.1587    , 159.028 , 14.1781   )
    if Scrup53:
        rotate_object(Scrup53, x_degrees=0, y_degrees=90, z_degrees=0)
        set_location(Scrup53, -51.453     , 83.6105 , 13.3125   )
    if Scrup54:
        rotate_object(Scrup54, x_degrees=0, y_degrees=90, z_degrees=-0)
        set_location(Scrup54, 42.193    , 83.6105 , 13.3125   )
    if Scrup55:
        rotate_object(Scrup55, x_degrees=0, y_degrees=90, z_degrees=0)
        set_location(Scrup55, 42.193    , 134.736 , 13.3125    )
    if Scrup56:
        rotate_object(Scrup56, x_degrees=0, y_degrees=90, z_degrees=0)
        set_location(Scrup56, -51.453     , 134.375 , 13.3125   )
    if Scrup57:
        rotate_object(Scrup57, x_degrees=-90, y_degrees=158, z_degrees=-90)
        set_location(Scrup57, -51.453    , 97.5451 , 69.7683   )
    if Scrup58:
        rotate_object(Scrup58, x_degrees=-90, y_degrees=158, z_degrees=-90)
        set_location(Scrup58, 41.9249     , 97.5451  , 69.7783    )

    # ANIMASI
    bpy.context.scene.frame_start = 1
    frame_middle = 100
    bpy.context.scene.frame_end = 200

    moving_objects = []
    all_objects = bpy.context.scene.objects
    for obj in all_objects:
        if not (is_object_in_collection(obj, collection_template) or is_object_in_collection(obj, collection_aspal) or is_object_in_collection(obj, collection_setup)):
            moving_objects.append(obj)
    
    distance =100

    #ANIMASI
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


    #DUPLICATE
    dup_obj = []
    for obj in all_objects:
        if not (is_object_in_collection(obj, collection_template) or is_object_in_collection(obj, collection_aspal) or is_object_in_collection(obj, collection_setup)):
            dup_collection = "dup" + get_first_collection_name_of_object(obj)
            dup = duplicate_object(obj.name, obj.name, dup_collection)
            if dup:
                rotate_object(dup, math.degrees(obj.rotation_euler.x), math.degrees(obj.rotation_euler.y), math.degrees(obj.rotation_euler.z))
                set_location(dup, obj.location.x, (obj.location.y)-320, obj.location.z)
                resize_object(dup, obj.scale.x, obj.scale.y, obj.scale.z)
                dup_obj.append(dup)

    #ANIMASI
    for obj in dup_obj:
        obj.location.y -= 0
        collection = bpy.data.collections.get("dupBanDepan")
        if collection:
            if obj.name in collection.objects:
                obj.rotation_euler = (obj.rotation_euler)
        obj.keyframe_insert(data_path="location", frame=bpy.context.scene.frame_start)
        obj.keyframe_insert(data_path="rotation_euler", frame=bpy.context.scene.frame_start)
        
        obj.location.y += distance
        collection = bpy.data.collections.get("dupBanDepan")
        if collection:
            if obj.name in collection.objects:
                obj.rotation_euler = (obj.rotation_euler.x, ((360 * (bpy.context.scene.frame_end / bpy.context.scene.frame_end)) * (3.14159 / 180)), obj.rotation_euler.z)

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