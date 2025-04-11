import matplotlib.pyplot as plt
import numpy as np

# Define the coordinates
blue = np.array([[-0.094, -0.094, 3.094],
                 [ 0.052,  1.948, 1.0]])
yellow = np.array([[3.094, 3.094, -0.094],
                   [0.052, 1.948, 1.0]])

# # Plot blue beacons
# plt.figure(figsize=(6, 4))
# plt.scatter(blue[0, :], blue[1, :], color='blue', label='Blue Beacons', s=100)
# for i, pos in enumerate(blue.T):
#     plt.text(pos[0], pos[1]+0.05, f'B{i+1}', color='blue', fontsize=12)

# plt.xlim(-0.2, 3.2)
# plt.ylim(0, 2.1)
# plt.xlabel('X (meters)')
# plt.ylabel('Y (meters)')
# plt.title('Blue Beacon Positions')
# plt.legend()
# plt.grid(True)
# plt.show()

# # Plot yellow beacons
# plt.figure(figsize=(6, 4))
# plt.scatter(yellow[0, :], yellow[1, :], color='goldenrod', label='Yellow Beacons', s=100)
# for i, pos in enumerate(yellow.T):
#     plt.text(pos[0], pos[1]+0.05, f'Y{i+1}', color='goldenrod', fontsize=12)

# plt.xlim(-0.2, 3.2)
# plt.ylim(0, 2.1)
# plt.xlabel('X (meters)')
# plt.ylabel('Y (meters)')
# plt.title('Yellow Beacon Positions')
# plt.legend()
# plt.grid(True)
# plt.show()

# Plot combined six beacons
plt.figure(figsize=(6, 4))
# Plot blue beacons in blue
plt.scatter(blue[0, :], blue[1, :], color='blue', label='Blue Beacons', s=100)
for i, pos in enumerate(blue.T):
    plt.text(pos[0]-0.1, pos[1]+0.05, f'B{i+1}', color='blue', fontsize=12)
# Plot yellow beacons in yellow
plt.scatter(yellow[0, :], yellow[1, :], color='goldenrod', label='Yellow Beacons', s=100)
for i, pos in enumerate(yellow.T):
    plt.text(pos[0]+0.1, pos[1]+0.05, f'Y{i+1}', color='goldenrod', fontsize=12)

plt.xlim(-0.2, 3.2)
plt.ylim(0, 2.1)
plt.xlabel('X (meters)')
plt.ylabel('Y (meters)')
plt.title('Combined Beacon Positions')
plt.legend()
plt.grid(True)
plt.show()
