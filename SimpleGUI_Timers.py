import simpleguitk as simplegui

message= "Good Morning"
display = True
timer_interval = 1000  #in milliseconds

def input_handler(text):
    global message
    message = (f'Good Morning {text}')

#Switches weather or not the text is visible
def timer_handler():
    global display
    display = not display

def draw_handler(canvas):
    if display:
        canvas.draw_text(message, (300,500), 20, "Aqua")

frame = simplegui.create_frame("Timer", 1000, 1000)
frame.add_input("Your Name: ", input_handler, 200)
frame.set_draw_handler(draw_handler)

timer= simplegui.create_timer(timer_interval, timer_handler)

timer.start()
frame.start()




