# This file is part of AFEM which provides an engineering toolkit for airframe
# finite element modeling during conceptual design.
#
# Copyright (C) 2016-2018  Laughlin Research, LLC (info@laughlinresearch.com)
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
from afem.exchange import *
from afem.topology import *

# Build a box and get faces
builder = BoxBySize()
solid = builder.solid
f1 = builder.top_face
f2 = builder.bottom_face
f3 = builder.front_face
f4 = builder.back_face
f5 = builder.left_face
f6 = builder.right_face

# Initialize a document
doc = XdeDocument(False)

# Add label for the main shape
main = doc.add_shape(solid, 'The Box')

# Add labels for the sub-shapes
doc.add_subshape(main, f1, 'top face')
doc.add_subshape(main, f2, 'bottom face')
doc.add_subshape(main, f3, 'front face')
doc.add_subshape(main, f4, 'back face')
doc.add_subshape(main, f5, 'left face')
doc.add_subshape(main, f6, 'right face')

# Save document
doc.save_as('named_box')
