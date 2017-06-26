from tkinter import *
from random import randint
from tkinter import messagebox
visit=dict()
P = None
color = ['Black','White']
A,B,D=2*19,3*19,1*19
E,F = B,0
def count(x,y,a,b):
	global P,color,C,visit
	i,j=x,y
	index = 1
	while (i+a,j+b) in visit and C.itemconfig(visit[(i+a,j+b)])['fill'][-1] == color[0]:
		index,i,j = index+1,i+a,j+b
	i,j=x,y
	while (i-a,j-b) in visit and C.itemconfig(visit[(i-a,j-b)])['fill'][-1] == color[0]:
		index,i,j = index+1,i-a,j-b
	return index
	
def win(x,y):
	if count(x,y,B,0)==5:
		return True
	if count(x,y,0,B)==5:
		return True
	if count(x,y,B,-B)==5:
		return True
	if count(x,y,B,B)==5:
		return True		
	return False
	

	
def click(event):
	global P,color,C,visit
	x,y=event.x-(event.x-E)%B,event.y-(event.y-F)%B
	if E<=x<=E+14*B and F<=y<=F+14*B and (x,y) not in visit:
		visit[(x,y)] = C.create_oval(x, y, x+A, y+A,fill=color[0])
		if win(x,y):
			C.itemconfigure(P, state='hidden')
			messagebox.showinfo('Game Over','%s Win'%(color[0]))
			for key in visit.keys():
				C.delete(visit[key])
			visit.clear()
			color = ['Black','White']
			C.itemconfigure(P, state='normal')
			motion(event)
		else:
			color = color[::-1]
			motion(event)
			
def motion(event):
	global P,color,C,visit
	x,y=event.x-D,event.y-D
	if P is None:
		P = C.create_oval(x, y, x+A, y+A,fill=color[0])
	else:
		C.coords(P, (x, y, x+A, y+A))
		C.itemconfig(P, fill=color[0])
		C.tag_raise(P)

def draw_board():
	global P,color,C,visit
	x,y=E,F
	for i in range(15):
		C.create_line(x+D,y+i*B+D,x+B*14+D,y+i*B+D,fill = 'black')
		C.create_line(x+i*B+D,y+D,x+i*B+D,y+B*14+D,fill = 'black')
	for i in range(3,12,4):
		for j in range(3,12,4):
			C.create_oval(x+B*i+A//3,y+B*j+A//3,x+B*i+A//2,y+B*j+A//2,fill = 'black')
	C.bind("<Button-1>", click)
	C.bind('<Motion>', motion)
	C.pack()
	
def main():
	global P,color,C,visit
	top = Tk()
	top.wm_title("Gomoku")
	#top.geometry("1080x600")
	C = Canvas(top, bg = '#F7DCB4', height =B*15, width = B*17)
	draw_board()
	top.mainloop()
if __name__ == '__main__':
	main()
	

