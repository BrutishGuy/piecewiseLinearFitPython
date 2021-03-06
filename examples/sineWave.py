#   fit for a specified number of line segments
#   you specify the number of line segments you want, the library does the rest

#    import our libraires
import numpy as np
import matplotlib.pyplot as plt
import pwlf

#   generate sin wave data
x = np.linspace(0, 10, num=100)
y = np.sin(x*np.pi/2)
#   add noise to the data
y = np.random.normal(0,0.05, 100) + y

#   initialize piecwise linear fit with your x and y data
myPWLF = pwlf.piecewise_lin_fit(x,y)

#   fit the data for four line segments
res = myPWLF.fit(16)
#   Be patient! this one takes some time - It's a difficult problem
#   using this differential evolution algo + bfgs can be over 500,000.0 function
#   evaluations

#   predict for the determined points
xHat = np.linspace(min(x), max(x), num=10000)
yHat = myPWLF.predict(xHat)

#   plot the results
plt.figure()
plt.plot(x,y,'o')
plt.plot(xHat,yHat, '-')
plt.show()
