# main function
def main():
    name = str(input("name the can? "))
    radius = float(input("enter the radius in cm "))  # in cm
    height = float(input("enter the radius in cm ")) # in cm
    area = can_surface_area(radius, height)
    volume = can_volume(radius, height)
    efficiency = volume / area
    print(f"The volume of a {name} can is {volume:.2f} cubic cm and the surface area is {area:.2f} square cm and the efficiency is {efficiency:.2f}.")

    name = str(input("#1 picnic"))
    radius = float(input("enter the radius in cm "))  # in cm
    height = float(input("enter the radius in cm ")) # in cm

    can_efficiency(name, radius, height)



# can efficiency function
def can_efficiency(name, radius, height):
    area = can_surface_area(radius, height)
    volume = can_volume(radius, height)
    efficiency = volume / area
    print(f"The volume of a {name} can is {volume:.2f} cubic cm and the surface area is {area:.2f} square cm and the efficiency is {efficiency:.2f}.")
    

# volume function
def can_volume(radius, height):
    import math
    volume = math.pi * radius ** 2 * height
    return volume
    

# surface area function
def can_surface_area(radius, height):
    import math
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area
# call main function
if __name__ == "__main__":
    main()
