# Interactive-3D-Projection-of-geometrical-shapes
Interactive projections 3 dimensional geometrical shape is rendered using the PyGame library.

Using 2D graphics only, the implementation creates a window which will display a 3D object defined by vertices and the edges of the faces of the object. Vertices are represented by small blue circles in the wireframe while the edges are created using straight blue lines. The edges will be lines which go between the vertices, and the faces would be transparent, such that a wireframe of the 3D object is displayed.
For the solid projection, the visible faces are solid and opaque. the color smoothly vary between #00005F (when the surface is viewed on edge, i.e. the normal of the surface makes a 90 degree angle to the Z-axis) and #0000FF (when the surface is viewed flat, i.e. orthogonal to the Z-axis) based on the angle with the Z-axis, such that the face is displayed similarly to how a shader would display it.

A sample object text file is attached in “object.txt.” The format of the file is:
-> The first line contains two integers. The first integer is the number of vertices that define the 3D
object, and the second number is the number of faces that define the 3D object.
-> Starting at the second line each line will define one vertex of the 3D object and will consist of an
integer followed by three real numbers. The integer is the ID of the vertex and the three real
numbers define the (x,y,z) coordinates of the vertex. The number of lines in this section will be
equal to the first integer in the file.
-> Following the vertex section will be a section defining the faces of the 3D object. The number of
lines in this section will be equal to the second integer on the first line of the file. Each line in
this section will consist of three integers that define a triangle that is a face of the object. The
three integers each refer to the ID of a vertex from the second section of the file.
