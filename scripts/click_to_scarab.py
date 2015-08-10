#!/usr/bin/env python3

import sys
import yaml
from sh import rostopic

seq = 0

NAMESPACE = 'scarab'
ROBOT_NAME = 'lane'

out = {
'header': {
  'seq': 0,
  'stamp': {
    'secs': 0,
    'nsecs': 0
  },
  'frame_id': 'map_hokuyo'
},
'pose': {
  'position': {
    'x': -22.5,
    'y': 17.9,
    'z': 0.0},
  'orientation': {
    'x': 0.0,
    'y': 0.0,
    'z': 0.0,
    'w': 1.0}
   }
}


blob = ''
while True:
	line = sys.stdin.readline()
	if line[0:3] == '---':
		c = yaml.load(blob)

		out['header']['seq'] = seq
		seq += 1

		out['pose']['position']['x'] = c['point']['x']
		out['pose']['position']['y'] = c['point']['y']

		# sys.stdout.write('{}\n'.format(out))
		# sys.stdout.flush()

		rostopic('pub', '-1', '/{0}/{1}/goal'.format(NAMESPACE, ROBOT_NAME), 'geometry_msgs/PoseStamped', '{}'.format(out))

		blob = ''
	else:
		blob += line


