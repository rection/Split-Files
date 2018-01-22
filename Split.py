#!/bin/python

import subprocess
import os
link = raw_input('link : ')


subprocess.call(['wget','-O','Indirilen',link])

subprocess.call(['split','-n 4','Indirilen'])

os.remove('./Indirilen')
