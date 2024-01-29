BASELINE_IN_METERS = 0.12
FOCAL_LENGTH_IN_PIXELS = 528

def get_disparity(depth, baseline=BASELINE_IN_METERS, focal_length=FOCAL_LENGTH_IN_PIXELS):
    return int((baseline*focal_length)/depth)
    

def get_depth(xl, xr, baseline=BASELINE_IN_METERS, focal_length=FOCAL_LENGTH_IN_PIXELS):
    if xl-xr == 0:
        return 1000
    return (baseline*focal_length)/(xl-xr)

def get_latitude(xl, depth):
    return (xl*depth)/FOCAL_LENGTH_IN_PIXELS