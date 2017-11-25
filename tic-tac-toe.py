from tkinter import *
import tkinter.messagebox


def win():
      if player == "O":
            tkinter.messagebox.showinfo("","Green win!")
            quit()
      else:
            tkinter.messagebox.showinfo("","Yello win!")
            quit()


def check():
      if list[0]["text"] == list[3]["text"] == list[6]["text"] != "     ":
            win()
      elif list[1]["text"] == list[4]["text"] == list[7]["text"] != "     ":
            win()
      elif list[2]["text"] == list[5]["text"] == list[8]["text"] != "     ":
            win()
      elif list[0]["text"] == list[1]["text"] == list[2]["text"] != "     ":
            win()
      elif list[3]["text"] == list[4]["text"] == list[5]["text"] != "     ":
            win()
      elif list[6]["text"] == list[7]["text"] == list[8]["text"] != "     ":
            win()
      elif list[0]["text"] == list[4]["text"] == list[8]["text"] != "     ":
            win()
      elif list[2]["text"] == list[4]["text"] == list[6]["text"] != "     ":
            win()
      

def checked(i) :
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"

      if player == "X" :
            check()
            player = "O"
            button["bg"] = "yellow"
      else :
            check()
            player = "X"
            button["bg"] = "lightgreen"

window = Tk()
player = "X"
list= []

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)

window.mainloop()
