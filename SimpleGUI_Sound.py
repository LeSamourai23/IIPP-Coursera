import simpleguitk as simplegui

def draw_handler(canvas):
    canvas.draw_image(image, (1500//2, 1500//2), (1500, 1500), (500, 500), (1000, 1000) )

sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg")

def button_handler():
    sound.play()

image = simplegui.load_image("https://i.kym-cdn.com/entries/icons/original/000/029/029/cover4.jpg")

frame = simplegui.create_frame("Sound", 1000, 1000)
frame.set_draw_handler(draw_handler)
frame.add_button("Play", button_handler)
frame.start()
