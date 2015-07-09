import sys
import yaml
from sh import rostopic

seq = 0

out = {
'header': {
  'seq': 0,
  'stamp': {
    'secs': 0,
    'nsecs': 0
  },
  'frame_id': 'map_hokuyo'
},
'goal_id': {
  'id': '',
  'stamp': {
    'secs': 0,
    'nsecs': 0
  }
},
'goal': {
  'stop': False,
  'target_poses': [{
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
   ]
}
}



blob = ''
while True:
	line = sys.stdin.readline()
	if line[0:3] == '---':
		c = yaml.load(blob)

		out['header']['seq'] = seq
		out['goal_id']['id'] = 'hi{}'.format(seq)
		seq += 1

		out['goal']['target_poses'][0]['pose']['position']['x'] = c['point']['x']
		out['goal']['target_poses'][0]['pose']['position']['y'] = c['point']['y']

		# sys.stdout.write('{}\n'.format(out))
		# sys.stdout.flush()

		rostopic('pub', '-1', '/scarab/scarab/move/goal', 'scarab_msgs/MoveActionGoal', '{}'.format(out))

		blob = ''
	else:
		blob += line


