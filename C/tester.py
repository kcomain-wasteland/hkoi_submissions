import subprocess

p = subprocess.run(['grep', 'f'], stdout=subprocess.PIPE,input='')