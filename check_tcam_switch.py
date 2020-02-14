#in this script i'm printing the used masks/values of IPv4 unicast indirectly-connected routes:
# once you get the value of masks/values, you can trigger email to monitor tcam table

#below is the output of command 'show platform tcam utilization | i IPv4 unicast indirectly-connected routes'

# IPv4 unicast indirectly-connected routes:    2048/2048         34/34

import json
from napalm.base import get_network_driver

optional_args = {'port': '443'}
driver = get_network_driver('ios')
dev = driver(hostname='142.225.213.132', username='prabin', password='prabin')
dev.open()
return_dictionary = dev.cli(['show platform tcam utilization | i IPv4 unicast indirectly-connected routes', ])
a=(return_dictionary['show platform tcam utilization | i IPv4 unicast indirectly-connected routes'])

output=a.split("2048/2048",1)[1]
nums = [int(n) for n in output.split('/')]
print ('used  Masks/values is '+ str(nums[0])+str('/')+str(nums[0]))
dev.close()
