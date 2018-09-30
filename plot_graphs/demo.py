import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1,6, 12)
print(type(x), x)

y = x ** 2

print(y)

# functional
# plt.plot(x,y,'g')
# plt.xlabel("time")
# plt.ylabel("distance in km")
# plt.title("distance covered in time,...")

#
# p1 = plt.subplot(3,2,1)
# p1.plot(x,y, 'r')
#
#
# p2 = plt.subplot(3,2,2)
# p2.plot(y, x, 'g')
#
# p3 = plt.subplot(3,2,3)
# p3.plot(y, x, 'g')
#
# p4 = plt.subplot(3,2,4)
# p4.plot(x,y, 'r')
#
# p5 = plt.subplot(3,2,5)
# p5.plot(x,y, 'r')
#
# plt.show()




# OO

figure = plt.figure()

axis = figure.add_axes([0.1,0.1,0.8,0.8])
axis.plot(x,y)
axis.set_xlabel("thisdfsd")

axis2 = figure.add_axes([0.2,0.6,0.2,0.2])
axis2.plot([1,2,3,4],[1,2,3,4])

figure.show()



#
# fig, axis = plt.subplots(nrows=2,ncols=3)
#
# print(type(axis))
#
#
# axis[0,1].plot(x,y)
# # for a in axis:
# #     a.plot(x,y)
#
#
# plt.show()