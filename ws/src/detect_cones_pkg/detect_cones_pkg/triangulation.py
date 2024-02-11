BASELINE_IN_METERS = 0.11995

def get_disparity(depth, frame_width, baseline=BASELINE_IN_METERS):
    if frame_width == 2208 :
        focal_length = 1067.11
    elif frame_width == 1920 :
        focal_length = 1068.1
    elif frame_width == 1280 :
        focal_length = 534.05
    elif frame_width == 672 :
        focal_length = 267.025
    return int((baseline*focal_length)/depth)
    

def get_depth(xl, xr, frame_width, baseline=BASELINE_IN_METERS):
    if frame_width == 2208 :
        focal_length = 1067.11
    elif frame_width == 1920 :
        focal_length = 1068.1
    elif frame_width == 1280 :
        focal_length = 534.05
    elif frame_width == 672 :
        focal_length = 267.025
    if xl-xr == 0:
        return 1000
    return (baseline*focal_length)/(xl-xr)

def get_latitude(xl, depth, frame_width):
    if frame_width == 2208 :
        focal_length = 1067.11
    elif frame_width == 1920 :
        focal_length = 1068.1
    elif frame_width == 1280 :
        focal_length = 534.05
    elif frame_width == 672 :
        focal_length = 267.025
    return ((xl-(frame_width/2))*depth)/focal_length