from guizero import App, PushButton, Text, TextBox, Picture
import time

def hide_it():
    display_picture.hide()





picture_list = ["ModelXGif.gif", "Model3Gif.gif", "ModelSGif.gif", "ModelYGif.gif"]
index = 0
app = App(title="GUI Tesla Ordering", bg="lavender")
display_text = Text(app, text="Order a Tesla", color="dodger blue")

display_picture=Picture(app, image = "tesla.gif")
display_picture.after(2000, hide_it)
app.display()


