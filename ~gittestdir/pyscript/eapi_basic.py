#!/usr/bin/python

import pyeapi
import yaml
from pprint import pprint as pp

veos1 = pyeapi.connect_to('veos1')


pp(veos1.enable('show version'))

veos1.config('hostname VEOS1')


shrun = veos1.enable('show running-config')

pp(veos1.enable('show version'))

veos1.config('hostname VEOS1')


shrun = veos1.enable('show running-config')
pp(shrun)

print "\n\n\nnow I'm going to the next section \n\n\n"

output = shrun[0]['result']['cmds']['interface Management1']['cmds']

test = output.keys()

print test
