import jcamp
import matplotlib.pyplot as plt
import subprocess

proc = subprocess.Popen("ls jdx/", stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
files = out.decode('utf-8').split('\n')[:-1]
del proc, out, err
for file_n in files:
    filename = "./jdx/" + file_n
    data = jcamp.JCAMP_reader(filename)
    plt.plot(data['x'], data['y'])
    plt.title(filename)
    plt.xlabel(data['xunits'])
    plt.ylabel(data['yunits'])
    plt.gca().invert_xaxis()
    plt.figure()
plt.show()

