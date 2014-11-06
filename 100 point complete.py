#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")

# Create your "enemies" here, before the class

enemy = drawpad.create_rectangle(10, 10, 100,100, fill='magenta')
direction = 1
def animate():
    global direction
    x1, y1, x2, y2 = drawpad.coords(enemy)
    if x2 > drawpad.winfo_width(): 
        direction = - 5
    elif x1 < 0:
        direction = 5
    drawpad.move(enemy,direction,0)
    drawpad.after(1, animate)

enemy2 = drawpad.create_rectangle(10, 300, 100,400, fill='blue')
direction = 1
def animate2():
    global direction
    x1, y1, x2, y2 = drawpad.coords(enemy2)
    if x2 > drawpad.winfo_width(): 
        direction = - 1
    elif x1 < 0:
        direction = 1
    drawpad.move(enemy2,direction,0)
    drawpad.after(1, animate2)

enemy3 = drawpad.create_rectangle(10, 500, 100, 600, fill='yellow')
direction = 1
def animate3():
    global direction
    x1, y1, x2, y2 = drawpad.coords(enemy3)
    if x2 > drawpad.winfo_width(): 
        direction = - 10
    elif x1 < 0:
        direction = 10
    drawpad.move(enemy3,direction,0)
    drawpad.after(50, animate3)


animate()
animate2()
animate3()

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=0)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    #70 point
       	    self.left = Button(self.myContainer1)
            self.left.configure(text='left', background= "yellow")
            self.left.grid(row=0,column=1)
            self.left.bind("<Button-1>", self.leftClicked)
	
	    self.right = Button(self.myContainer1)
            self.right.configure(text='right', background= "orange")
            self.right.grid(row=0,column=2)
            self.right.bind("<Button-1>", self.rightClicked)
            
            self.down = Button(self.myContainer1)
            self.down.configure(text='down', background= "blue")
            self.down.grid(row=0,column=3)
            self.down.bind("<Button-1>", self.downClicked)
                        
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=RIGHT)
       	    # call the animate function to start our recursion
       	    self.animate()
	
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    
	    # Uncomment this when you're ready to test out your animation!
	    #drawpad.after(10,self.animate)
		
	def upClicked(self, event):   
	   global drawpad
	   global player
	   drawpad.move(player,0,-20)

                   
        def leftClicked(self, event):
            global drawpad
            global player
            drawpad.move(player,-20,0)


        def rightClicked(self, event):
            global drawpad
            global player
            drawpad.move(player,20,0)
        
        def downClicked(self, event):
            global drawpad
            global player
            drawpad.move(player,0,20)


app = MyApp(root)
root.mainloop()