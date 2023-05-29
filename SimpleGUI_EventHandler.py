import simpleguitk as simplegui

text= "Hello"

# The text string will change to World and Background Color to White when click() is called 
def click():
    global text
    global bgColor     #To Call tbe global variable
    text= "World"
    frame.set_canvas_background("White")

def draw_handler(canvas):
    canvas.draw_text(text, (350, 500), 100, 'Blue')

frame = simplegui.create_frame("Event", 1000, 1000)
frame.add_button("Click", click)
frame.set_draw_handler(draw_handler)
frame.set_canvas_background("Black")
frame.start()