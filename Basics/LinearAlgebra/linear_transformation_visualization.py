import matplotlib.pyplot as plt
import numpy as np

# Create a single vector
V = np.array([2.5, 2.5])
new_i = np.array([1, 0])
new_j = np.array([1, 1])
shearing_matrix = np.concatenate((new_i, new_j)).reshape((2, 2), order='F')
rotation_angle = np.pi / 4  # 45 degrees (in radians)

# Apply the shearing transformation
V_sheared = shearing_matrix @ V

new_i = np.array([0, -1])
new_j = np.array([1, 0])
# Define the rotation matrix using new_i and new_j
rotation_matrix = np.column_stack((new_i, new_j))  # Basis vectors as columns
# could also use the rotation angle to define the rotation matrix
# rotation_matrix = np.array([[np.cos(rotation_angle), -np.sin(rotation_angle)],
#                             [np.sin(rotation_angle), np.cos(rotation_angle)]])
V_rotated = rotation_matrix @ V

new_i = np.array([1, 1])
new_j = np.array([1, 1])
# Define the scaling matrix using new_i and new_j
scaling_matrix = np.column_stack((new_i, new_j))  # Basis vectors as columns
V_scaled = scaling_matrix @ V

# Create three subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# Plot the sheared vector
ax1.quiver(0, 0, V[0], V[1], angles='xy', scale_units='xy', scale=1, color='r', label='Original Vector')
ax1.quiver(0, 0, V_sheared[0], V_sheared[1], angles='xy', scale_units='xy', scale=1, color='b', label='Sheared Vector')
ax1.set_xlim([-10, 10])
ax1.set_ylim([-10, 10])
ax1.set_title("Shearing Transformation")
ax1.grid(True)
ax1.legend()

# Plot the rotated vector
ax2.quiver(0, 0, V[0], V[1], angles='xy', scale_units='xy', scale=1, color='r', label='Original Vector')
ax2.quiver(0, 0, V_rotated[0], V_rotated[1], angles='xy', scale_units='xy', scale=1, color='g', label='Rotated Vector')
ax2.set_xlim([-10, 10])
ax2.set_ylim([-10, 10])
ax2.set_title("Rotational Transformation")
ax2.grid(True)
ax2.legend()

# Plot the scaled vector
ax3.quiver(0, 0, V[0], V[1], angles='xy', scale_units='xy', scale=1, color='r', label='Original Vector')
ax3.quiver(0, 0, V_scaled[0], V_scaled[1], angles='xy', scale_units='xy', scale=1, color='y', label='Scaled Vector')
ax3.set_xlim([-10, 10])
ax3.set_ylim([-10, 10])
ax3.set_title("Scaling Transformation")
ax3.grid(True)
ax3.legend()


plt.show()