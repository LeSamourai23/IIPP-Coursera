import simpleguitk as simplegui
import math

face = False
body = False
hands = False
legs = False 

def toggle_face():
    global face
    face = True

def toggle_body():
    global body
    body = True

def toggle_hands():
    global hands
    hands = True

def toggle_legs():
    global legs
    legs = True

def draw_handler(canvas):
    if face:
        canvas.draw_circle((500, 250), 50, 10, "pink", "orange")   #Face
    
    if body:
        canvas.draw_line((500, 300), (500, 550), 10, 'pink')    #Body
    
    if hands:
        canvas.draw_polyline([(500, 400), (300, 300), (500, 400), (700, 300)], 10, "pink")  #Hands

    if legs:
        canvas.draw_polyline([(350, 700), (500, 550), (650, 700)], 10, "pink")  #Legs


frame = simplegui.create_frame("Event", 1000, 1000)

#When you press these buttons each of these components will become active
frame.add_button("Face", toggle_face)
frame.add_button("Body", toggle_body)
frame.add_button("Hands", toggle_hands)
frame.add_button("Legs", toggle_legs)

frame.set_draw_handler(draw_handler)
frame.start()