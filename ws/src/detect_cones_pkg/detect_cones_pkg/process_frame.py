from . import triangulation
from . import window_matching
from . import inference
from . import sort

CONFIDENCE_LIMIT = 0.8

def process(left_frame, right_frame):

    all_results = inference.infer(left_frame)
    all_results = [x for x in all_results]

    detected_cones = []

    cone_types = ["blue_cone", "yellow_cone", "orange_cone", "big_orange_cone", "unknown_color_node"]
    for cone_type in cone_types:
        results = [x for x in all_results if x["class"] == cone_type]
        results = sort.sort(results)

        previous_disparity = left_frame.shape[1]
        for result in results:
            xl, y, width, height = result["xywh"]

            # Window Matching 
            xr = window_matching.get_right_point(left_frame, right_frame, xl, y, width, height, previous_disparity)

            # Triangulation
            depth = triangulation.get_depth(xl, xr, left_frame.shape[1])
            latitude = triangulation.get_latitude(xl, depth, left_frame.shape[1])

            detected_cones.append({
                'type': cone_type,
                'x': depth,
                'y': latitude
            })

            previous_disparity = xl - xr

    return detected_cones
