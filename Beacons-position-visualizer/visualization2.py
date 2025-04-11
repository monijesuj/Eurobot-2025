import matplotlib.pyplot as plt

# Blue Beacons
blue_x = [-0.094, -0.094, 3.094]
blue_y = [0.052, 1.948, 1.0]

# Yellow Beacons
yellow_x = [3.094, 3.094, -0.094]
yellow_y = [0.052, 1.948, 1.0]

# Plot field (0,0) to (3,2)
plt.figure()
plt.plot([0,3,3,0,0], [0,0,2,2,0], 'k-')  # Field boundary

# Plot beacons
plt.scatter(blue_x, blue_y, c='blue', label='Blue')
plt.scatter(yellow_x, yellow_y, c='orange', label='Yellow')
plt.legend()
plt.xlabel('x (m)'), plt.ylabel('y (m)')
plt.grid(True)
plt.show()