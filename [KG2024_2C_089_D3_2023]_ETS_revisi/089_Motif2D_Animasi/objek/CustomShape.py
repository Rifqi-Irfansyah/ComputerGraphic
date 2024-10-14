import primitif.basic as basic

def buat_lingkaran(xc, yc, radius, start, end):
        circle_points = basic.draw_circle(radius, xc, yc, "solid")
        num_points = len(circle_points)/360
        selected_points=[]
        #DRAW
        i = 0
        for x, y in circle_points:
            i += 1
            if(i >= num_points*start) and (i<= num_points*end):
                selected_points.append((x, y))
            elif(i > num_points*end):
                selected_points.append((x, y))
                break
        return selected_points
    
def buat_ellipse(xc, yc, Rx, Ry, start, end):
    ellipse_points = basic.draw_patterned_ellipse(Rx, Ry, xc, yc, "solid")
    num_points = len(ellipse_points)/360
    selected_points=[]
    #DRAW
    i = 0
    for x, y in ellipse_points:
        i += 1
        if(i >= num_points*start) and (i<= num_points*end):
            selected_points.append((x, y))

        elif(i > num_points*end):
            selected_points.append((x, y))
            break
    return selected_points