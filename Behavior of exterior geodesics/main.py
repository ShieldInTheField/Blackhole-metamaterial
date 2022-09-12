"""
This code has been developed to calculate a light ray path passing by a Schwarzschild black hole.
For a more accurate result, it's recommended to edit the "diffPhi" and scape condition parameters according to your initial parameters.
Although this code simulates the ray path correctly (in range of its accuracy) unrelated to input's physical meanings,
if you choose the initial radius from the center of the black hole proportional to its mass, the output will make more physical sense.
If you find it useful, for further info's don't hesitate to contact me via email.

Author's name: Soroush Ataee
Author's email: ataeesoroush@gmail.com
"""


# Dependencies
import math
from constant import *
import matplotlib.pyplot as plt

# Functions
def schwarzschild_refraction_index(local_mass, local_radius):
    refraction_index = math.pow((1 + (local_mass / (2 * local_radius))), 3) / (
        1 - ((local_mass) / (2 * local_radius))
    )
    return refraction_index


def c_constant(local_theta):
    return (
        schwarzschild_refraction_index(black_hole_mass, initial_radius)
        * initial_radius
        * math.sin(math.radians(local_theta))
    )


def single_light_ray_trajectories(local_theta):
    phi_list = [initial_phi]
    radius_list = [initial_radius]
    flag = True
    counter = 0
    while flag:

        # creating list of radiuses
        radius = radius_list[counter]
        refractionIndex = schwarzschild_refraction_index(black_hole_mass, radius)
        radical_index = (
            pow(radius, 2) * pow(refractionIndex, 2) / pow(c_constant(local_theta), 2)
        ) - 1
        # checking if ray hits the horizon
        if refractionIndex >= 0:
            delta_radius = -diffPhi * radius * math.sqrt(abs(radical_index))
            # checking if the ray can scape from black hole
            if (-delta_radius / diffPhi) <= pow(10, -3):
                print("It's not gonna hit the horizon")
                flag = False

            else:
                radius = radius + delta_radius
                radius_list.append(radius)

                # creating list of phis
                phi = phi_list[counter]
                phi = phi + diffPhi
                phi_list.append(phi)

                counter = counter + 1

        else:
            print("It has reached the black hole horizon")
            print(radius_list[len(radius_list) - 1])
            print(
                "Accuracy for calculation of black hole horizon radius is",
                (black_hole_mass / 2) - radius_list[len(radius_list) - 1],
            )
            flag = False

    # Uncomment this part of the code if the pure calling of this function is wanted
    """
    # Plotting
    fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
    ax.plot(phi_list, radius_list)
    plt.show()
    """
    return [phi_list, radius_list]


# main function and calling subfunctions
single_light_ray_trajectories()  # Must enter the initial thetas
