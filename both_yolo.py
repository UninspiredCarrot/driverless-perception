from inference import infer

previous_right_frame_results = {}

def get_right_point(left_result, right_frame, id):
    
    if id in previous_right_frame_results:
        right_results = previous_right_frame_results[id]
    else:
        right_results = infer(right_frame)
        previous_right_frame_results[id] = right_results

    min_loss = float("inf")
    xr = 0

    for right_result in right_results:
        
        if right_result["class"] == left_result["class"] and right_result["confidence"] > 0.8:
            loss = sum([(l - r)**2 for l, r in zip(left_result["xywh"], right_result["xywh"])])
            if loss < min_loss:
                min_loss = loss
                xr, _, _, _ = right_result["xywh"]
    
    return xr