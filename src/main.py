import validation

if __name__ == "__main__":
    # Prompt for package name
    pass
    try:
        pass # try validate_package_name()
    except:
        pass # print validation error and exit program

    # Prompt for lobby names
    pass
    try:
        pass # try validate_lobby_names()
    except:
        pass # print validation error and exit program

    # Prompt for folder including all maps
    pass
    maps = []

    # Loop through maps, unzip and validate
    all_maps_valid = True
    for map in maps:
        pass # unzip map
        try:
            pass # try validate_map()
        except validation.ValidationError as e:
            all_maps_valid = False
            # print and swallow error
        else:
            pass # print success

    if all_maps_valid == False:
        pass # exit program

    # Package mod
    pass

