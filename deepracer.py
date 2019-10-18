def reward_function(params):

    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    #x = params['x']
    #y = params['y']
    distance_from_center = params['distance_from_center']
    is_left_of_center = params['is_left_of_center']
    #heading = params['heading']
    #progress = params['progress']
    #steps = params['steps']
    speed = params['speed']
    steering_angle = abs(params['steering_angle'])
    track_width = params['track_width']
    #waypoints = params['waypoints']
    #clasest_waypoints = params['clasest_waypoints']

    reward = 1.0
    if steering_angle > 0 and steering_angle < 7 and speed > 4.5:
        reward += reward * 0.1
    elif steering_angle >= 7 and steering_angle < 15 and speed > 3.5 and speed < 4.5:
        reward += reward * 0.1
    elif steering_angle >= 15 and steering_angle < 25 and speed > 0.5 and speed < 3.5:
        reward += reward * 0.1
    elif steering_angle >= 25 and steering_angle < 30:
        reward = reward * 0.8

    if is_left_of_center == True and distance_from_center <= track_width / 4 and steering_angle < 5:
        reward = reward * 2

    marker = 1.1
    if steering_angle > 5 and is_left_of_center == False and distance_from_center <= track_width / 4:
        marker = 1.2
        if steering_angle > 10 and is_left_of_center == False and distance_from_center <= track_width / 2 and distance_from_center >= track_width / 1.5:
            marker = 1.5

    if marker == 1.2:
        reward += reward * 0.1
    if marker == 1.5:
        reward += reward * 0.5
        
    if all_wheels_on_track == False:
        reward = 1e-3 #very low

    return float(reward)
