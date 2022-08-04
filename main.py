from datetime import datetime
from jsonrpclib import Server
from jinja2 import Template, Environment, FileSystemLoader
import os, sys, re
import json

# Function - Read a json file
def readDataJsonFile(file):
  with open(file) as jsondata:
    data = json.load(jsondata)
  return data

# Step1 - Read the json file for the leaf
leafConfig = readDataJsonFile('leaf.json')


# Step2 - lsRender Jinja2
file_loader = FileSystemLoader('')
env = Environment(loader=file_loader,trim_blocks=True,lstrip_blocks=True)
template = env.get_template('leaf.j2')
output = template.render(leafConfig)
print(output)

# Write the configuration in the directory
with open('configurationFinale/testLeaf.json', 'w') as outfile:
  json.dump(data, outfile)
outfile.close()