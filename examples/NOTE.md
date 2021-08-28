---
title: OpenCASCADE
---

## make SOLID

- <https://dev.opencascade.org/doc/occt-7.5.0/refman/html/class_b_rep_builder_a_p_i___make_shape.html>
- BRepOffsetAPI_ThruSections
- BRepOffsetAPI_MakeOffset
- BRepPrimAPI_MakePrism

## make MESH

- <https://www.opencascade.com/doc/occt-7.5.0/refman/html/package_brepmesh.html>
- <https://www.opencascade.com/doc/occt-7.5.0/refman/html/package_imeshtools.html>
- <https://www.opencascade.com/doc/occt-7.5.0/refman/html/package_meshvs.html>
- BRepMesh_IncrementalMesh
- BRep_Tool.Triangulation

## OCCT

- pyocct
  - netgen4smesh
  - smesh4pyocct
- afem

```bash
conda create -n occt -c trelau -c conda-forge python=3.8 anaconda wxpython pyocct
conda install -c trelau -c conda-forge afem
pip install meshio[all]
pip install gmsh
pip install --force-reinstall --no-cache-dir gmsh-dev
pip install pygmsh
pip install opencv-python
pip install opencv-contrib-python
pip install --upgrade --force-reinstall --no-deps PyQt5
pip install PyQt3D

conda install -c conda-forge -c trelau pyocct --force-reintsall

conda remove -n occt --all
```

"""
  afem-1.1.0-py38_0
  arrow-1.1.1-py38haa95532_0
  binaryornot-0.4.4-pyhd3eb1b0_1
  cookiecutter-1.7.2-pyhd3eb1b0_0
  inflection-0.5.1-py38haa95532_0
  jinja2-time-0.2.0-py_2
  netgen4smesh-6.2.1804-he980bc4_0
  poyo-0.5.0-pyhd3eb1b0_0
  pthread-stubs-0.3-h3c9f919_1
  pyocct-7.4.0.0-py38he980bc4_1
  pypubsub-4.0.3-py_0
  python-slugify-5.0.2-pyhd3eb1b0_0
  qstylizer-0.1.10-pyhd3eb1b0_0
  smesh4pyocct-8.3.0.4-ha925a31_0
  text-unidecode-1.3-py_0
  tinycss-0.4-pyhd3eb1b0_1002
  unidecode-1.2.0-pyhd3eb1b0_0
  whichcraft-0.6.1-pyhd3eb1b0_0
  wxpython-4.1.1-py38heb73c8a_1
"""
