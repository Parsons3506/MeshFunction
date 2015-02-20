def solveequation( function, x, y ):
    d = 10
    angledata = rs.Angle( (0,0,0), (x,y,0))
    a = 0.0
    if angledata: a = angledata[0] * math.pi/180
    try:
        z = eval(function)
    except:
        z = 0
    return z

def loadfunctiondata():
    try:
        file = open("MeshSettings_XY.txt", "r")
        items = file.readlines()
        file.close()
        function = str(items[0])
        domain = (float(items[1]), float(items[2]),
        float(items[3]), float(items[4]))
        resolution = int(items[5])
    except:
        function = "math.cos(math.sqrt(x**2+y**2))"
        domain = (-10.0, 10.0, -10.0, 10.0)
        resolution = 50
    return function, domain, resolution
def meshfunction_xy():
    zfunc, domain, resolution = loadfunctiondata()
    zfunc = rs.StringBox( zfunc, "Specify a function f(x,y[,D,A])", "Mesh function")
    if not zfunc: return
    while True:
        prompt = "Function domain x{%f,%f} y{%f,%f} @%d" % (domain[0], domain[1],
        domain[2], domain[3], resolution)
        result = rs.GetString(prompt, "Insert", ("xMin","xMax","yMin","yMax","Resolution","Insert"))
        
        if not result: return
        result = result.upper()
        if result=="XMIN":
            f = rs.GetReal("X-Domain start", domain[0])
        if f is not None: domain[0]=f
        elif result=="XMAX":
            f = rs.GetReal("X-Domain end", domain[1])
        if f is not None: domain[1]=f
        elif result=="YMIN":
            f = rs.GetReal("Y-Domain start", domain[2])
        if f is not None: domain[2]=f
        elif result=="YMAX":
            f = rs.GetReal("Y-Domain end", domain[3])
        if f is not None: domain[3]=f
        elif result=="RESOLUTION":
            f = rs.GetInteger("Resolution of the graph", resolution)
        if f is not None: resolution=f
        elif result=="INSERT": break
        verts = createmeshvertices(zfunc, domain, resolution)
        faces = createmeshfaces(resolution)
        rs.AddMesh(verts, faces)
        SaveFunctionData(zfunc, domain, resolution)
        
        
meshfunction_xy()