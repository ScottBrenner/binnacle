#!/usr/bin/python3
import subprocess
import json

installed_list = json.loads(subprocess.run(['helm', 'list', '--output', 'json'], stdout=subprocess.PIPE).stdout.decode('utf-8'))

installed_dict = {}

# subprocess.run(['helm', 'repo', 'update'])

for chart in installed_list['Releases']:
    installed_dict[chart['Chart'].rsplit('-',1)[0]] = chart['Chart'].rsplit('-',1)[1]

for installed_chart in installed_dict:
    print('=====')
    print(subprocess.run(['helm', 'search', installed_chart], stdout=subprocess.PIPE).stdout.decode('utf-8'))
    print('INSTALLED VERSION: ' + installed_dict[installed_chart])