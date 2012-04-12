"""
Sweep Splines 0.2
Written for CINEMA 4D R12.048

Copyright (C) 2011 by Donovan Keith (www.donovankeith.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE

Name-US: Sweep Splines
Description-US: Sweeps all selected spline objects with an instance object that defaults to a Rectangle.
"""


import c4d
from c4d import gui
#Welcome to the world of Python

def sweepSpline(spline, master_instance):
    #Create a new sweep object and insert it before the spline.
    sweep = c4d.BaseObject(c4d.Osweep)
    sweep.SetName( "".join([spline.GetName()," Sweep"]))
    sweep.InsertAfter(spline)
    doc.AddUndo(c4d.UNDOTYPE_NEW, sweep)

    #Move the spline into the sweep.
    doc.AddUndo(c4d.UNDOTYPE_CHANGE, spline)
    spline.Remove()
    spline.InsertUnder(sweep)
    
    #Create an instance that references the master_instance and
    #make it a child of the sweep nurbs.
    local_instance = c4d.BaseObject(c4d.Oinstance)
    local_instance.SetName( "".join([spline.GetName(),"SS Instance"]))
    local_instance[c4d.INSTANCEOBJECT_LINK] = master_instance
    doc.AddUndo(c4d.UNDOTYPE_NEW, local_instance)
    local_instance.InsertBefore(spline)
    pass

def main():
    doc.StartUndo()
    
    objList = doc.GetActiveObjects(childs=True)
 
    #Create Null
    null_obj = c4d.BaseObject(c4d.Onull)
    null_obj.SetName("SS Control Objects")
    doc.AddUndo(c4d.UNDOTYPE_NEW, null_obj)
    doc.InsertObject(null_obj)    
 
    #Create Master Rectangle
    rectangle = c4d.BaseObject(c4d.Osplinerectangle)
    rectangle[c4d.PRIM_RECTANGLE_WIDTH] = 10
    rectangle[c4d.PRIM_RECTANGLE_HEIGHT] = 10
    rectangle.SetName("SS Rectangle")
    doc.AddUndo(c4d.UNDOTYPE_NEW, rectangle)
    doc.InsertObject(rectangle,parent=null_obj)
    
    #Create Master Instance
    master_instance = c4d.BaseObject(c4d.Oinstance)
    master_instance.SetName("SS Master Instance [Don't Delete]")
    master_instance[c4d.INSTANCEOBJECT_LINK] = rectangle
    doc.AddUndo(c4d.UNDOTYPE_NEW, master_instance)
    doc.InsertObject(master_instance,pred=rectangle)
    
    doc.SetActiveObject(rectangle, c4d.SELECTION_NEW)
    
    #Create sweeps for each selected spline
    for obj in objList:
        if obj.GetRealSpline():
            sweepSpline(obj, master_instance)
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)

    c4d.EventAdd()
    doc.EndUndo()

if __name__=='__main__':
    main()