import simpleguitk as simplegui

#Draw a diagnol line on the screen
def draw_a_line_handler(canvas):
    canvas.draw_line((0, 0), (1000, 1000), 2, 'Blue')
#                    point1   point2   line_width  color

#Draw a multiple point line on screen (In this case draw an X on screen)
def draw_a_polyline_handler(canvas):
    canvas.draw_polyline([(0,0), (500, 500), (1000, 0), (0, 1000), (500, 500), (1000, 1000)], 10, 'Pink')

#Draw a Polyogn in screen (In this case an hourglass)
def draw_a_polygon_handler(canvas):
    canvas.draw_polygon([(250, 250), (750, 250), (250, 750), (750, 750), (250, 250)], 10, 'Yellow', 'Orange')
#                                                                                       Border Color  Fill Color    

#Draw a Circle on Screen 
def draw_a_circle_handler(canvas):
    canvas.draw_circle((500, 500), 200, 5, 'Blue', 'White') 
#                   center_point, radius, line_width, line_color, fill_color = color      

frame = simplegui.create_frame("Practice", 1000, 1000)
frame.set_draw_handler(draw_a_circle_handler)  #Replace with different draw handlers
frame.start()