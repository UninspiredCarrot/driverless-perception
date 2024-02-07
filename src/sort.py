import math

def get_area(result):
    return result["xywh"][2]*result["xywh"][3]

def area_sort(results):
    return sorted(results, key=lambda result: result['xywh'][3]*result['xywh'][2], reverse=True)

def get_close_calls(results):
    close_calls = []
    for i, result in enumerate(results[1:-1]):
        i += 1
        if (get_area(result) - get_area(results[i+1])) < 100:
            close_calls.append({
                "index": i,
                "before": results[i-1],
                "close": (result, results[i+1]),
                })
    return close_calls

def get_magnitude(result1, result2):
    return math.sqrt((result1["xywh"][0]-result2["xywh"][0])**2 + (result1["xywh"][1]-result2["xywh"][1])**2)

def should_switch(call):
    if get_magnitude(call["before"], call["close"][0]) > get_magnitude(call["before"], call["close"][1]):
        return call["index"]
    return False


def sort(results):
    sorted_results = area_sort(results)
    close_calls = get_close_calls(sorted_results)
    for call in close_calls:
        index = should_switch(call)
        if index:
            temp = sorted_results[index]
            sorted_results[index] = sorted_results[index+1]
            sorted_results[index+1] = temp

    return sorted_results


    