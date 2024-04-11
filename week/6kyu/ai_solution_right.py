def tower_builder(num_floors):
    # build here
    if not isinstance(num_floors, int) or num_floors <= 0:
        raise ValueError("Number of floors must be a positive integer.")
    tower = []
    for floor in range(1, num_floors + 1):
        # Calculate the number of stars in this floor
        stars = floor * 2 - 1
        # Add spaces to center the stars
        padding = " " * (num_floors - floor)
        # Create the floor string and add it to the tower
        tower.append(padding + "*" * stars + padding)

    return tower