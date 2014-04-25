#!/usr/bin/env python

import random
import os

lat = str(random.uniform(49.3208494, 49.1881387))
lon = str(random.uniform(-123.2880123, -122.8656566))

os.system("xdg-open 'http://maps.google.com/maps?&z=10&q="+lat+"+"+lon+"&ll="+lat+"+"+lon+"'")

