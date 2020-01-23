#in this script i'm printing the used masks/values of IPv4 unicast indirectly-connected routes.
# once you get the value of masks/values, you can trigger email to monitor tcam table

#below is the output of command

'show platform tcam utilization | i IPv4 unicast indirectly-connected routes'

IPv4 unicast indirectly-connected routes:    2048/2048         34/34


show platform tcam utilization

CAM Utilization for ASIC# 0                      Max            Used
                                             Masks/Values    Masks/values

 Unicast mac addresses:                       8412/8412         51/51
 IPv4 IGMP groups + multicast routes:         1120/1120          2/2
 IPv4 unicast directly-connected routes:      4096/4096          0/0
 IPv4 unicast indirectly-connected routes:    2048/2048         34/34
 IPv4 policy based routing aces:               442/442          12/12
 IPv4 qos aces:                                512/512          21/21
 IPv4 security aces:                           954/954          44/44

Note: Allocation of TCAM entries per feature uses
a complex algorithm. The above information is meant
to provide an abstract view of the current TCAM utilization

