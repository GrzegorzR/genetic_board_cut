def total_area(rect_list):
    result = 0
    for rect in rect_list:
        if rect:
            result += int(rect.xmax - rect.xmin) * int(rect.ymax - rect.ymin)
    return result

def fit_function(rect_list):
    return float(total_area(rect_list))