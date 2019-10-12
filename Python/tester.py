import subprocess
for x in range(0, 9999):
    print("loading {}".format(x+1))
    a = subprocess.run('py "G:\\P\\Python Projects\\HKOI submissions\\Python\\D106.py" -n {}'.format(x), shell=True)