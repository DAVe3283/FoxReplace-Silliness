#! python
'''
Converts YAML substitution list into a JSON list for use in FoxReplace
'''
import sys
import yaml
import json
from pprint import pprint


rules = yaml.load(sys.stdin)
start_tag = '<span title="$1" style="text-shadow: 0em 0em 0.2em rgb(128, 133, 246)">'
end_tag = '</span>'

for group in rules['groups']:
    group['html'] = 'output'
    for sub in group['substitutions']:
        sub['inputType'] = 'regexp'
        sub['output'] = "".join([start_tag, sub['output'], end_tag])
        # pprint(sub)

json.dump(rules, sys.stdout, indent=2)
