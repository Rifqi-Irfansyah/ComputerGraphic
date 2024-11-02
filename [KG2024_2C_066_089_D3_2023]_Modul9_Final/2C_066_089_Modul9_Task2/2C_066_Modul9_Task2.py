import bpy
import math
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
    kerangkaBan = duplicate_object("Beam STR ESS BU06x01x01 - SPN-BEM-0043 (stemfie.org).001", "KerangkaBan", "MobilDepan")
    if kerangkaBan:
        rotate_object(kerangkaBan, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(kerangkaBan, -38.942, 91.4146, 28.434)
        resize_object(kerangkaBan, 1, 1, 1)

    kerangkaBan2 = duplicate_object("Beam STR ESS BU06x01x01 - SPN-BEM-0043 (stemfie.org).001", "KerangkaBan", "MobilDepan")
    if kerangkaBan2:
        rotate_object(kerangkaBan2, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(kerangkaBan2, -38.5046, 30.3902, 5.9819)
        resize_object(kerangkaBan2, 1, 1, 1)



    # Duplicate the object and optionally specify a collection
    badanKuda = duplicate_object("Beam STR ESS BU05x01x01 - SPN-BEM-0042 (stemfie.org)", "Badan", "Kuda")
    if badanKuda:
        rotate_object(badanKuda, x_degrees=0, y_degrees=0, z_degrees=0)
        set_location(badanKuda, 200, 3, 50)
        resize_object(badanKuda, 1, 1, 1)
    badanTambahan = duplicate_object("Brace STR ERR BU03x01x00.25 - SPN-BRC-0002 (stemfie.org)","BadanTambahan","Kuda")
    if badanTambahan:
        set_location(badanTambahan, 243.75 , 3.75, 56.25)
        rotate_object(badanTambahan, x_degrees=90, y_degrees=0, z_degrees=0)
    badanTambahan2 = duplicate_object("BadanTambahan","BadanTambahan2","Kuda")
    if badanTambahan2:
        set_location(badanTambahan2, 194, 5, 56)
        rotate_object(badanTambahan2, x_degrees=90, y_degrees=0, z_degrees=0)    
    badanTambahanr = duplicate_object("BadanTambahan","badanTambahanr","Kuda")
    if badanTambahanr:
        set_location(badanTambahanr, 243.75, 18.75, 56.25)
        rotate_object(badanTambahanr, x_degrees=90, y_degrees=0, z_degrees=0)
    badanTambahanr2 = duplicate_object("badanTambahanr","badanTambahanr2","Kuda")
    if badanTambahanr2:
        set_location(badanTambahanr2, 193.75, 18.7, 56.25)
        rotate_object(badanTambahanr2, x_degrees=90, y_degrees=0, z_degrees=0) 
        
    
    kakiKuda = duplicate_object("Brace STR ERR BU05x01x00.25 - SPN-BRC-0004 (stemfie.org)","Kaki","Kuda")
    kakiKuda2 = duplicate_object("Kaki","Kaki2","Kuda")    
    kakiKuda3 = duplicate_object("Kaki","Kaki3","Kuda")
    kakiKuda4 = duplicate_object("Kaki","Kaki4","Kuda")
    if kakiKuda:
        set_location(kakiKuda,256.25,18.75,56.25)
        rotate_object(kakiKuda, x_degrees=-90, y_degrees=60, z_degrees=0)
    if kakiKuda2:
        set_location(kakiKuda2,206.25,20,56.25)
        rotate_object(kakiKuda2, x_degrees=-90, y_degrees=125, z_degrees=0)
    if kakiKuda3:
        set_location(kakiKuda3,256,0,57)
        rotate_object(kakiKuda3, x_degrees=-90, y_degrees=60, z_degrees=0)
    if kakiKuda4:
        set_location(kakiKuda4,206.25,-1.25,56.25)
        rotate_object(kakiKuda4, x_degrees=-90, y_degrees=125, z_degrees=0)
        
        
    LeherKuda = duplicate_object("Brace STR ERR BU04x01x00.25 - SPN-BRC-0003 (stemfie.org)","LeherKuda","Kuda")
    if LeherKuda:
        set_location(LeherKuda,267.5,16.25,56.25)
        rotate_object(LeherKuda, x_degrees=90, y_degrees=-45, z_degrees=0)
        resize_object(LeherKuda, 1,1,4)
    Kepala1 = duplicate_object("Brace STR ERR BU03x01x00.25 - SPN-BRC-0002 (stemfie.org)","KepalaKuda1","Kuda")
    Kepala2 = duplicate_object("Brace STR ERR BU03x01x00.25 - SPN-BRC-0002 (stemfie.org)","KepalaKuda2","Kuda")
    if Kepala1:
        set_location(Kepala1,293.75,3.75,81.25)
        
    if Kepala2:
        set_location(Kepala2,293.75,18.75,81.25)
        
    rotate_object(Kepala1, x_degrees=90, y_degrees=30, z_degrees=0)
    rotate_object(Kepala2, x_degrees=90, y_degrees=30, z_degrees=0)
    Ekor = duplicate_object("Brace STR ERR BU02x01x00.25 - SPN-BRC-0001 (stemfie.org)","Ekor","Kuda")
    if Ekor:
        set_location(Ekor,186.25,15,65)
        rotate_object(Ekor, x_degrees=90, y_degrees=45, z_degrees=0)
        resize_object(Ekor, 1,1,3.5)
    
