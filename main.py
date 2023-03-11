"""Dimentional Reduction on Botnet Data"""
"""Writen By: M. Aidiel Rachman Putra"""
"""Organization: Net-Centic Computing Laboratory | Institut Teknologi Sepuluh Nopember"""

import warnings
warnings.simplefilter(action='ignore')
import bin.interfaces.cli.main as cli
import bin.modules.spm4Detection.domain as spm4d
import bin.modules.sensorBasedPattern.domain as sbp

if __name__ == "__main__":
  listMenu = [
    ('Sensor Based Causality Analysis', sbp.main),
    ('Sequence Pattern Mining for Detection', spm4d.main),
  ]
  cli.menu(listMenu)