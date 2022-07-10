import trimesh

def get_cad(path):
    if ".stl" in path.lower():
        cad = trimesh.load(path)
        return cad
    else:
        cad = trimesh.Trimesh(**trimesh.interfaces.gmsh.load_gmsh(file_name=path))
        return cad
        
def get_bound_dim(cad):
    return cad.extents

def get_billet_type(cad):
    billet = cad.bounding_primitive
    return str(billet).split(".")[-1].replace(">","")

def get_surface_area(cad):
    return round(cad.area,3)

def get_part_volume(cad):
    return round(cad.volume,3)

def get_png(cad,file_name):
    data = trimesh.Scene(cad).save_image()
    with open (file_name,"wb") as outdata:
        outdata.write(data)
    return file_name
    
def get_unit(cad):
    return trimesh.units.units_from_metadata(cad, guess=True)
 