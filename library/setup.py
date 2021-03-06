
# scale is 1:scale
scale = 2

number_of_houses = 20

# define the grid
grid_length = 160 * scale
grid_width = 180 * scale

# define type, length, width, free space, value, and incrementation for Eengezinswoning
house_e_type = "Eengezinswoning"
house_e_length = 8 * scale
house_e_width = 8 * scale
house_e_free = 2 * scale
house_e_value = 285000
house_e_increment = 0.03
house_e_number = int(12 * number_of_houses / 20)

# define type, length, width, free space, value, and incrementation for Bungalow
house_b_type = "Bungalow"
house_b_length = 10 * scale
house_b_width = int(7.5 * scale)
house_b_free = 3 * scale
house_b_value = 399000
house_b_increment = 0.04
house_b_number = int(5 * number_of_houses / 20)

# define type, length, width, free space, value, and incrementation for Maison
house_m_type = "Maison"
house_m_length = 11 * scale
house_m_width = int(10.5 * scale)
house_m_free = 6 * scale
house_m_value = 610000
house_m_increment = 0.06
house_m_number = int(3 * number_of_houses / 20)

# define type, length, and width for Water
water_type = "Water"
water_length = 38 * scale
water_width = 38 * scale
