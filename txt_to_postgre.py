import glob
import os
import sys

input_workspace = sys.argv[1]

for file in glob.glob(os.path.join(input_workspace, '*.txt')):
	f = open(file).readlines()
	print(f[3].split(':')[1].split('-')[0])
	print(file)