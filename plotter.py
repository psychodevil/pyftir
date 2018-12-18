import jcamp
import matplotlib.pyplot as plt
filename = 'a.jdx'
data = jcamp.JCAMP_reader(filename)
plt.plot(data['x'], data['y'])
plt.title(filename)
plt.xlabel(data['xunits'])
plt.ylabel(data['yunits'])

jcamp.JCAMP_calc_xsec(data, skip_nonquant=False, debug=False)
plt.gca().invert_xaxis()
plt.show()
#plt.figure()


