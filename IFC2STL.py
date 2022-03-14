import os
import subprocess
from obj2stl import obj2stl
name = "example"
ifc_name = "%s.ifc"%name
obj_name = "%s.obj"%name
stl_name = "%s.stl"%name
if(os.path.exists(obj_name)):
    os.remove(obj_name)
cmd = "IfcConvert.exe %s %s --sew-shells"%(ifc_name, obj_name)
subprocess.call(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
obj2stl.convert(input=obj_name, output=stl_name)
