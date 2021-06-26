# This file is part of AFEM which provides an engineering toolkit for airframe
# finite element modeling during conceptual design.
#
# Copyright (C) 2016-2018 Laughlin Research, LLC
# Copyright (C) 2019-2020 Trevor Laughlin
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
from OCCT.BRepCheck import BRepCheck_Analyzer
from OCCT.ShapeBuild import ShapeBuild_ReShape
from OCCT.ShapeFix import ShapeFix_Shape, ShapeFix_ShapeTolerance

from afem.topology.entities import Shape

__all__ = ["FixShape"]

_fix_tol = ShapeFix_ShapeTolerance()


class FixShape(object):
    """
    Attempt to fix the shape by applying a number of general fixes.

    :param afem.topology.entities.Shape shape: The shape.
    :param float precision: Basic precision value.
    :param float min_tol: Minimum allowed tolerance.
    :param float max_tol: Maximum allowed tolerance.
    :param afem.topology.entities.Shape context: The context shape.

    .. note::

        By default, the precision, minimum, and maximum tolerance values are
        Precision::Confusion() with OCCT, which is typically 1.0e-7.

    """

    def __init__(self, shape, precision=None, min_tol=None, max_tol=None,
                 context=None):
        self._tool = ShapeFix_Shape()

        if precision is not None:
            self._tool.SetPrecision(precision)
        if min_tol is not None:
            self._tool.SetMinTolerance(min_tol)
        if max_tol is not None:
            self._tool.SetMaxTolerance(max_tol)

        if context is not None:
            reshape = ShapeBuild_ReShape()
            reshape.Apply(context.object)
            self._tool.SetContext(reshape)

        self._tool.Init(shape.object)
        self._tool.Perform()

    @property
    def shape(self):
        """
        :return: The fixed shape.
        :rtype: afem.topology.entities.Shape
        """
        return Shape.wrap(self._tool.Shape())

    @property
    def context(self):
        """
        :return: The context.
        :rtype: OCCT.ShapeBuild.ShapeBuild_ReShape
        """
        return self._tool.Context()

    def apply(self, shape):
        """
        Apply substitutions to the shape (or sub-shape) and get the result.

        :param afem.topology.entities.Shape shape: The shape.

        :return: The new shape.
        :rtype: afem.topology.entities.Shape
        """
        return Shape.wrap(self.context.Apply(shape.object))

    @staticmethod
    def limit_tolerance(shape, tol=1.0e-7, styp=Shape.SHAPE):
        """
        Limit tolerances in a shape.

        :param afem.topology.entities.Shape shape: The shape.
        :param float tol: Target tolerance.
        :param OCCT.TopAbs.TopAbs_ShapeEnum styp: The level of shape to set
            (i.e., only vertices, only edges, only faces, or all shapes).

        :return: *True* if the shape is valid after limiting tolerance, *False*
            if not.
        :rtype: bool
        """
        # Limit tolerance then fix in case of invalid tolerances
        _fix_tol.LimitTolerance(shape.object, tol, tol, styp)
        ShapeFix_Shape(shape.object).Perform()
        return BRepCheck_Analyzer(shape.object, False).IsValid()

    @staticmethod
    def set_tolerance(shape, tol, styp=Shape.SHAPE):
        """
        Enforce tolerance on the given shape.

        :param afem.topology.entities.Shape shape: The shape.
        :param float tol: The tolerance.
        :param OCCT.TopAbs.TopAbs_ShapeEnum styp: The level of shape to set
            (i.e., only vertices, only edges, only faces, or all shapes).

        :return: None.
        """
        return _fix_tol.SetTolerance(shape.object, tol, styp)
