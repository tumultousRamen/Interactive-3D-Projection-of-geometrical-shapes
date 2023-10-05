# Interactive-3D-Projection-of-geometrical-shapes
Interactive projections 3 dimensional geometrical shape is rendered using the PyGame library.

Using 2D graphics only, the implementation creates a window which will display a 3D object defined by vertices and the edges of the faces of the object. Vertices are represented by small blue circles in the wireframe while the edges are created using straight blue lines. The edges will be lines which go between the vertices, and the faces would be transparent, such that a wireframe of the 3D object is displayed.
For the solid projection, the visible faces are solid and opaque. the color smoothly vary between #00005F (when the surface is viewed on edge, i.e. the normal of the surface makes a 90 degree angle to the Z-axis) and #0000FF (when the surface is viewed flat, i.e. orthogonal to the Z-axis) based on the angle with the Z-axis, such that the face is displayed similarly to how a shader would display it.
