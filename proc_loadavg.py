#!/usr/bin/env python
import graphitesend

g = graphitesend.init(group='loadavg_', suffix='min', dryrun=True)
(la1, la5, la15) = open('/proc/loadavg').read().strip().split()[:3]
print g.send_dict({'1': la1, '5': la5, '15': la15})
