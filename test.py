#!/usr/bin/env python

import unittest
import nbconvert
import os

import numpy as np

with open("assignment8.ipynb") as f:
    exporter = nbconvert.PythonExporter()
    python_file, _ = exporter.from_file(f)


with open("assignment8.py", "w") as f:
    f.write(python_file)


from assignment8 import KozenyCarmen

class TestSolution(unittest.TestCase):

    def test_transform(self):

        kc = KozenyCarmen('poro_perm.csv')

        np.testing.assert_allclose(kc.kc_model()[0:10], 
                                   np.array([0.00144518, 0.00144518, 0.00178167, 
                                             0.00073352, 0.0035369, 0.00123457, 
                                             0.00194181, 0.00199742, 0.0022314, 
                                             0.00205417]), atol=0.01)
        
    def test_transform_private(self):

        kc = KozenyCarmen('poro_perm.csv')

        np.testing.assert_allclose(kc.kc_model()[22:31], 
                                   np.array([0.00328828, 0.00183395, 0.00290263, 0.00241945,
                                             0.00211207, 0.00229286, 0.00144518, 0.00173048, 
                                             0.00217115]), atol=0.01)
        
if __name__ == '__main__':
    unittest.main()

