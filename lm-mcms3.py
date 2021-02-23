def reward_function(params):
    '''
    Minimal curvature max speed reward
    '''
    
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    steering_abs = abs(params['steering_angle']) # Only need the absolute steering angle
    speed = params['speed']
    progress_reward = params['progress']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']

    if progress_reward >= 100:
        progress_reward = 7000
    else:
        progress_reward = progress_reward * 10

    # parameter to be optimized
    speed_treshold = 3000
    # calculated parameter
    steering_treshold = 50
    
    if steering_abs != 0.:
        steering_factor = steering_abs
    else:
        steering_factor = 0.1
    
    reward = progress_reward + steering_treshold/steering_factor + speed_treshold * speed * speed
    
    if distance_from_center <= 0.37 * track_width:
        distance_factor = (track_width - distance_from_center) / track_width
        reward = reward * distance_factor * distance_factor * distance_factor
    # we just do not accept the wheels off track
    if not params["all_wheels_on_track"]:
        reward = reward / 100.

    return float(reward)
