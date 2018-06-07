from guizero import App, PushButton, Text, TextBox, Picture, info
import time
#Model_Y = Picture(app, image = "ModelYGif.gif")
picture_list = ["ModelXGif.gif", "Model3Gif.gif", "ModelSGif.gif", "ModelYGif.gif", "ModS1.jpg", "ModY1.jpg", "Mod31.jpg", "ModX1"]
index = 0

def hide_it():
    display_picture.hide()
def startup():
    global display_picture
    display_picture=Picture(app, image = "tesla.gif")
    display_picture.after(9000, hide_it)
    
def change_picture():
    global index
    display_picture.show()
    index = index + 1
    if index < len(picture_list):
        display_picture.value = picture_list[index]
    else:
        index = 0
        display_picture.value = picture_list[index]
        
def alert_textX():
    info_var = " Model X"
    info("GUI Tesla Ordering", "You Have Ordered A New Tesla Model X")
def alert_text3():
    info_var = " Model 3"
    info("GUI Tesla Ordering", "You Have Ordered A New Tesla Model 3")
def alert_textS():
    info_var = " Model S"
    info("GUI Tesla Ordering", "You Have Ordered A New Tesla Model S")
def alert_textY():
    info_var = " Model Y"
    info("GUI Tesla Ordering", "You Have Ordered A New Tesla Model Y")

app = App(title="GUI Tesla Ordering", bg="black")
startup()
app.bg = "lavender"
display_text = Text(app, text="Order a Tesla", color="dodger blue", size=20)
button3 = PushButton(app, text="Model 3  $35,000", command=alert_text3)
buttonX = PushButton(app, text="Model X  $79,500", command=alert_textX)
buttonY = PushButton(app, text="Model Y ~$35,000", command=alert_textY)
buttonS = PushButton(app, text="Model S  $74,500", command=alert_textS)

cycle = PushButton(app, text="Browse Teslas", command=change_picture)

app.display()




