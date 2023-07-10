#!/usr/bin/env python3

import sys
import random

value = random.randint(0, 3)
print("Returning: {}".format(value))
sys.exit(value)
