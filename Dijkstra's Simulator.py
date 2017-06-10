''' save save as differnce
    curved edges
    file handling diff
'''
    



from tkinter import *
from tkinter.ttk import *
from tkinter.tix import *
from tkinter import messagebox,filedialog
import time
import struct
import os
import math



try:
    import images
except:
    pass
INF=10000000000000
root=Tk()
root.title("Untitled - DIJKSTRA'S ALGORITHM")
root.state("zoomed")
try:
    root.iconbitmap("algo.ico")
except:
    pass



##------------------------Dijkstra's Algorithm----------------------##

        
##---------------End of Dijkstra's Algorithm------------------##





                                                     #Menu Functions
                                        #File


class App(object):
    
    def __init__(self):
        

        self.one=0
        self.disz=0
        self.statusbar=Label(root,relief=SUNKEN,bd=4,bg="white")
        self.statusbar.place(x=0,y=625,width=1030)
        global file

        b = Balloon(root,statusbar=self.statusbar)
        

        self.flag1,self.flag2,self.flag3,self.flag4,self.flag5,self.flag6,self.flag7,self.flag8,self.flag9,self.flag10,self.flag11=0,0,0,0,0,0,0,0,0,0,0
        #head=StringVar()
        #head.set("Dijkstra's Algorithm")
                 # Menu Bar
        foot=StringVar()
        head=StringVar()
        foot.set('@ KD AND KVNT')
        foot_label=Label(root,relief=SUNKEN,bg="white",fg="black",textvariable=foot)
        foot_label.place(x=0,y=655,height=30,width=1030)

        menubar=Menu(root)
        filemenu=Menu(menubar,tearoff=0)
        filemenu.add_command(label="New      ",command=self.NEW)
        filemenu.add_command(label="Open...        ",command=self.OPEN)
        filemenu.add_command(label="Save",command=self.SAVE)
        filemenu.add_command(label="Save As ",command='')
        filemenu.add_command(label="Print ",command='')
        filemenu.add_command(label="Exit",command=self.EXIT)
        menubar.add_cascade(label="File",menu=filemenu)

        

        helpmenu=Menu(menubar,tearoff=0)
        helpmenu.add_command(label="module Help",command=self.create_sol)
        helpmenu.add_command(label="About Algo",command='')
        menubar.add_cascade(label="Help",menu=helpmenu)

        root.bind("<Alt-F4>",self.EXIT)
        root.bind("<Control-s>",self.SAVE)
        root.bind("<Control-S>",self.SAVE)
        root.bind("<Control-o>",self.OPEN)
        root.bind("<Control-O>",self.OPEN)
        root.bind("<Control-n>",self.NEW)
        root.bind("<Control-N>",self.NEW)
        root.bind("<F5>",self.RUN)
        root.configure(menu=menubar)


        
        
        


               # graphFrame  for canvas
         
        self.graphframe=Frame(root,relief=SUNKEN,bd=4)
        
    
        
            
        
        
        self.graphframe.grid(row=0,column=0,padx=38)
        self.canvas=Canvas(self.graphframe,height=600,width=970,scrollregion=(0,0,0,0))
        self.canvas.config(bg="white")
        
        self.vscrollbar=Scrollbar(self.graphframe)
        self.vscrollbar.pack(side=RIGHT,fill=Y)
        self.vscrollbar.config( command = self.canvas.yview )

        self.hscrollbar=Scrollbar(self.graphframe,orient=HORIZONTAL)
        self.hscrollbar.pack(side=BOTTOM,fill=X)
        self.hscrollbar.config( command = self.canvas.xview )
        self.canvas.config(yscrollcommand=self.vscrollbar.set,xscrollcommand=self.hscrollbar.set)
        self.canvas.pack(fill=BOTH,expand=True)


        
        #grid=PhotoImage(file="grid1.gif")
        #self.canvas.create_image(50, 50, anchor=NE, image=grid)
        self.hl,self.vl=[],[]
        for x in range(30,2500,30):
            a=self.canvas.create_line(x,0,x,15000,fill="gray")
            self.hl.append(a)
        for y in range(30,2500,30):
            z=self.canvas.create_line(0,y,15000,y,fill="gray")
            self.vl.append(z)
        


        




        frame=Frame(root,bg="grey",bd=5,relief=RAISED)
        frame.place(x=1030,y=0,height=960,width=335)
                                                        #explaination Frame


        exframe=Frame(frame,bg="white",bd=2,relief=SUNKEN).place(x=0,y=0,width=325,height=210)
        exlabel=Label(frame,bg="purple",text="Brief Explanation").place(x=0,y=0,height=30,width=325)
        desc="Dijkstra's algorithm, conceived by, an\
  computer scientist 'Edsger Dijkstra' in \
1956 and published in 1959, is an graph search algorithm that solves the  singlesource shortest path problem for a graph\
with non-negative edge path cost, which produce a shortest path tree.\n\n\
This  algorithm is often used in routingand as a subroutine in other graph algo-rithms."
        self.brief=Text(frame,relief=SUNKEN,bg="white",fg="black")
        self.brief.place(x=0,y=30,height=250,width=324)
        self.brief.insert(INSERT,desc)
        self.brief.config(state=DISABLED)
        
                                                        #frame 1
        frame1=Frame(frame,bg="white",bd=2,relief=SUNKEN)
        frame1.place(x=0,y=280,height=150,width=325)
        
        label1=Label(frame1,text="Graph Construction",relief=RAISED,bg="purple")
        label1.place(x=0,y=0,width=325,height=30)
                                                        #Nodes
        label_node=Label(frame1,text="Nodes ",relief=RAISED,bg="grey",fg="black",bd=2)
        label_node.place(x=0,y=30,width=325,height=20)

        
        self.set_nodes=Button(frame1,text="Set",state=ACTIVE,command=self.AddNode,bd=2,relief=RAISED)
        self.set_nodes.place(x=20,y=57,height=25,width=50)
        #set_nodes.config(image=self.nodeimg,height="10",width="10")

        b.bind_widget(self.set_nodes, balloonmsg='Set Nodes',statusmsg='Start Setting the Nodes in the Graph')


        
        del_nodes=Button(frame1,text="Del",state=ACTIVE,command=self.DelNode,bd=2,relief=RAISED)
        del_nodes.place(x=140,y=57,height=25,width=50)
        #del_nodes.config(image=self.delnimg,height="10",width="10")

        b.bind_widget(del_nodes, balloonmsg='Delete Nodes',
                      statusmsg='Delete Last Node from the Grpah')

        clear_nodes=Button(frame1,state=ACTIVE,text="Clear All",command=self.NodeClear,bd=2,relief=RAISED)
        clear_nodes.place(x=250,y=57,height=25,width=50)

        b.bind_widget(clear_nodes, balloonmsg='Delete All Nodes',
                      statusmsg='Delete all Nodes from the Grpah')

        
                                                        #Edges
        label_edge=Label(frame1,text="Edges ",relief=RAISED,bg="grey",fg="black",bd=2)
        label_edge.place(x=0,y=88,width=325,height=20)

        

        

        self.set_edge=Button(frame1,state=ACTIVE,text="Set",command=self.AddEdges,bd=2,relief=RAISED)
        self.set_edge.place(x=20,y=113,height=25,width=50)

        b.bind_widget(self.set_edge, balloonmsg='Set Edges',
                      statusmsg='Start setting Edges from one Node to another Node')
        
        del_edge=Button(frame1,state=ACTIVE,text="Del",command=self.DelEdge,bd=2,relief=RAISED)
        del_edge.place(x=140,y=113,height=25,width=50)

        b.bind_widget(del_edge, balloonmsg='Delete Edges',
                      statusmsg='Delete last added edge from the Graph')

        clear_edge=Button(frame1,state=ACTIVE,text="Clear All",command=self.EdgeClear,bd=2,relief=RAISED)
        clear_edge.place(x=250,y=113,height=25,width=50)

        b.bind_widget(clear_edge, balloonmsg='Delete All Edges',
                      statusmsg='Delete all the Edges from the Graph')

                                                        #frame 2
        self.frame2=Frame(frame,bg="white",bd=2,relief=SUNKEN)
        self.frame2.place(x=0,y=430,width=325,height=290)
        label2=Label(self.frame2,relief=RAISED,text="Check Algorithm Results",bg="purple")
        label2.place(x=0,y=0,width=325,height=30)

        self.run=Button(self.frame2,state=ACTIVE,bd=2,relief=RAISED,text="Run Algorithm",command=self.RUN)
        self.run.place(x=115,y=79,width=100,height=25)
        label_src=Label(self.frame2,text="                          \
Source Node",fg="black",anchor=W,bd=2,relief=RAISED).place(x=0,y=30,width=325,height=25)
        
        label_check=Label(self.frame2,text="Check Results",relief=RAISED,bg="grey",fg="black")
        label_check.place(x=0,y=107,width=325,height=20)

        self.chk=Button(self.frame2,state=ACTIVE,bd=2,relief=RAISED,text="Check Solution",command=self.Show)
        

        b.bind_widget(self.chk, balloonmsg='Check Graph Solution',
                      statusmsg='Check step by step solution of the graph you made')

        label_run=Label(self.frame2,text="RUN",relief=RAISED,bg="grey",fg="black").place(x=0,y=54,height=20,width=325)
                                                        #frame 3
        frame3=Frame(frame,bg="white",bd=2,relief=SUNKEN)
        frame3.place(x=0,y=594,width=325,height=122)
        label3=Label(frame3,text=" Options ",relief=RAISED,bg="purple")
        label3.place(x=0,y=0,width=325,height=30)

        help_button=Button(frame3,text="Help",state=ACTIVE,relief=RAISED,command=self.Help)
        help_button.place(x=20,y=45,width=50,height=30)

        reset_button=Button(frame3,text="Reset",command=self.RESET,state=ACTIVE,relief=RAISED)
        reset_button.place(x=140,y=45,width=50,height=30)
        self.f=frame
        self.g=exframe
        exit_button=Button(frame3,text="Exit",command=self.EXIT,state=ACTIVE,relief=RAISED)
        exit_button.place(x=250,y=45,width=50,height=30)

        self.startx=None
        self.starty=None

        self.msg=StringVar()
        #self.msg.set("X:   Y:  ")
        self.trace=Message(self.statusbar,textvariable=self.msg,anchor=W,bg="white",bd=0,relief=SUNKEN)

        self.def_dist=Label(root,text="Default   Distance  ",relief=RAISED,bd=2,fg="black",anchor=W)
        self.def_dist.place(x=40,y=628,width=155,height=26)

        self.def_d=StringVar()
        self.def_d.set('1')
        Entry(self.def_dist,bd=2,textvariable=self.def_d,relief=SUNKEN).place(x=113,height=23,width=40)
        #self.canvas.bind('<Enter>')
        self.canvas.bind('<Motion>',self.track)
        self.canvas.bind('<Leave>',self.track1)
        #msg.place(root,fg="black",x=100,y=100)
        self.trace.pack(side=RIGHT)
        self.chk.place(x=115,y=132,width=100,height=25)
        self.toolframe=Frame(root,relief=RAISED,bd=3,height=653,width=37)
        self.toolframe.place(x=1,y=0)
        try:
            grid=PhotoImage(file="images/grid.gif",width=35,height=35)
            self.gridtool=Button(self.toolframe,height=30,text="grid",width=30,bd=0,image=grid,relief=SUNKEN,command=self.removegrid)
            self.gridtool.grid=grid
            self.gridtool.place(x=0,y=210)
        except:
            pass
        try:
            play=PhotoImage(file="images/play.gif",width=35,height=35)
            self.playtool=Button(self.toolframe,height=30,text="run",width=30,bd=0,image=play,relief=SUNKEN,command=self.RUN)
            self.playtool.play=play
            self.playtool.place(x=0,y=0)
        except:
            pass
        try:
            undo=PhotoImage(file="images/undo.gif",width=35,height=35)
            self.undotool=Button(self.toolframe,height=30,text="run",width=30,bd=0,image=undo,relief=SUNKEN,command=self.undo)
            self.undotool.undo=undo
            self.undotool.place(x=0,y=140)
        except:
            pass
        try:
            save=PhotoImage(file="images/save.gif",width=35,height=35)
            self.savetool=Button(self.toolframe,height=30,text="save",width=30,bd=0,image=save,relief=SUNKEN,command=self.SAVE)
            self.savetool.save=save
            self.savetool.place(x=0,y=105)
        except:
            pass
        try:
            reset=PhotoImage(file="images/reset.gif",width=35,height=35)
            self.resettool=Button(self.toolframe,height=30,text="reset",width=30,bd=0,image=reset,relief=SUNKEN,command=self.RESET)
            self.resettool.reset=reset
            self.resettool.place(x=0,y=175)
        except:
            pass
        try:
            new=PhotoImage(file="images/new.gif",width=35,height=35)
            self.newtool=Button(self.toolframe,height=30,text="new",width=30,bd=0,image=new,relief=SUNKEN,command=self.NEW)
            self.newtool.new=new
            self.newtool.place(x=0,y=35)
        except:
            pass
        try:
            openf=PhotoImage(file="images/open.gif",width=35,height=35)
            self.openftool=Button(self.toolframe,height=30,text="open",width=30,bd=0,image=openf,relief=SUNKEN,command=self.OPEN)
            self.openftool.openf=openf
            self.openftool.place(x=0,y=70)
        except:
            pass

        try:
            move=PhotoImage(file="images/move.gif",width=35,height=35)
            self.movetool=Button(self.toolframe,bg="white",height=30,text="move",width=30,bd=0,image=move,relief=FLAT,command=self.Move)
            self.movetool.move=move
            self.movetool.place(x=0,y=245)
        except:
            pass
        self.val_init()

    def track(self,event):
        self.trace.configure(width=100,bd=3)
        self.msg.set("X: %s Y: %s "%(event.x,event.y))

    def track1(self,event):
        #self.msg.set("X:   Y:  ")
        self.msg.set("")
        self.trace.configure(width=0,bd=0)

    def removegrid(self):
        
        for i in range(len(self.hl)):
            self.canvas.delete(self.hl[i])
            self.canvas.delete(self.vl[i])
        self.hl,self.vl=[],[]
        self.gridtool.config(text="P",command=self.placegrid)

    def placegrid(self):
        for x in range(30,2500,30):
            a=self.canvas.create_line(x,0,x,15000,fill="gray")
            self.canvas.tag_lower(a)
            self.hl.append(a)
            b=self.canvas.create_line(0,x,15000,x,fill="gray")
            self.canvas.tag_lower(b)
            self.vl.append(b)
        
            
        self.gridtool.config(text="R",command=self.removegrid)
        
            
            
        

        
    def val_init(self):
        self.open_chk_flag=0
        self.new_nodes=[]
        self.str_s=StringVar()
        self.i=0
        self.nodes=[]
        self.edges=[]
        self.v=[]
        self.distance=[]
        self.ent_count=0
        self.count=0
        self.entry_values=[]
        self.label_values=[]
        self.dis_count=0
        self.flagchk=0
        self.node_placing=[]
        self.edge_placing=[]
        self.ecor=[]
        self.ent_get_values=[]
        self.history=[]
        root.protocol("WM_DELETE_WINDOW", self.EXIT)
        self.str_ent=Entry(self.frame2,bd=3,textvariable=self.str_s).place(x=180,y=30,height=23,width=40)
        self.fileopen=0
        self.DIR_BIT=0
        self.dir_flag=0
        self.filecor=0
        

    def GET_BIT(self):
        s=IntVar()
        
        s=self.var_val.get()
        if s==0:
            tkinter.messagebox.showinfo("Warning", "Select an option and then click on OK.")
        else:
            #self.canvas.bind("<Button-1>",self.Node)
            self.child.grab_release()
            self.child.destroy()
            if s==1:
                self.DIR_BIT=1
            self.dir_flag=1
        #print(s)
 
        
    def DIR_BIT_SET(self):
        self.child=Toplevel()
        self.child.grab_set()
        self.child.title("Select ...")
        self.child.geometry("200x100")
        self.child.attributes("-toolwindow",1)
        self.child.resizable(0,0)
        self.child.transient(root)
        self.child.frame()
        #self.child.bind("<Enter>",self.GET_BIT)
        self.child.protocol("WM_DELETE_WINDOW", self.OPT_EXIT)
        self.var_val = IntVar()
        
        R1 = Radiobutton(self.child, text="Directed Graph", variable=self.var_val, value=1)
        R1.pack( anchor = W )

        R2 = Radiobutton(self.child, text="Undirected Graph", variable=self.var_val, value=2)
        R2.pack( anchor = W )
        
        self.child_ok=Button(self.child,text="OK",command=self.GET_BIT)
        self.child_ok.place(x=80,y=70)
        
    def OPT_EXIT(self):
        tkinter.messagebox.showinfo("Warning", "Select an option and then click on OK.")
        
        

    
    def AddNode(self):
        #print(self.dir_flag)
        #if(self.dir_flag==1):
        self.AddNode2()
        #else:
            #tkinter.messagebox.showinfo("Warning", "Select an option and then click on OK.")

    def AddNode2(self):
        if self.open_chk_flag==0 and self.fileopen==0:
            self.DIR_BIT_SET()
        self.flag10=1
        #if(self.dir_flag==0):
            #self.DIR_BIT_SET()
        if len(self.label_values)>0:
            for i in range(len(self.label_values)):
                self.label_values[i].place_forget()
        if self.flag2==1:
            self.StopEdges()
            
            self.flagchk=0
        '''if self.flag1==1:
            self.i=self.i + 1'''
        self.StopMove()
        self.canvas.configure(cursor="plus")   
        self.set_nodes.config(bg="lawn green")
        self.canvas.bind("<Button-1>",self.Node)
        
    def Node(self,event):
        
        
        s=(event.x,event.y)
        chk=self.NotINNodes(s)
        if(chk==1):
            
            self.nodes.append(s)
            print(s)
            x=self.canvas.create_oval((s[0]-15,s[1]-15,s[0]+15,s[1]+15),fill="violet red",width=2,outline="gray",tag='bubbles')
            y=self.canvas.create_text(s[0],s[1],font=6,text=self.i+1,activefill="green",fill="white")
            
            self.node_placing.append(x)
            self.node_placing.append(y)
            self.i=self.i+1
            self.history.append("nodeadd")
        self.flag4=1

    def NotINNodes(self,tmp):
        for i in range(len(self.nodes)):
            temp=self.nodes[i]
            #print(temp)
            a=(0,0)
            if((tmp[0]<=temp[0]+45 and tmp[0]>=temp[0]-45) and(tmp[1]<=temp[1]+45 and tmp[1]>=temp[1]-45)):
                
                return 0
        return 1

    def StopNode(self):
        self.canvas.configure(cursor="arrow")
        self.set_nodes.config(bg="white")
        self.canvas.bind("<Button-1>","")


    def AddEdges(self):
        if len(self.nodes)==0:
            self.empty()
        else:
            self.flag6=1
            if len(self.label_values)>0:
                for i in range(len(self.label_values)):
                    self.label_values[i].place_forget()
            self.flag2,self.flag1,self.flagchk=1,1,1
            self.StopNode()
            
            self.set_edge.config(bg="lawn green")
            
            self.mat= [[0 for _ in range(self.i)] for _ in range(self.i)]
        
        
        
            self.canvas.bind("<Button-1>",self.StartAdd)
            self.canvas.bind("<B1-Motion>",self.MidAdd)
            self.canvas.bind("<ButtonRelease-1>",self.EndAdd)

    def empty(self):
        tkinter.messagebox.showinfo("Warning", "First Add any Node.")

    def StartAdd(self,event):
        
        t1=(event.x,event.y)
        #print(t1)
        global c1
        c1=self.search(t1)
        self.fflag=0
        for i in range(len(self.nodes)):
            if(c1==self.nodes[i]):
                self.fflag=1
        global x_axis
        x_axis=self.search2(t1)
        #print(c1)
        

    def search(self,tmp):
        for i in range(len(self.nodes)):
            temp=self.nodes[i]
            #print(temp)9
            a=(0,0)
            if((tmp[0]<=temp[0]+15 and tmp[0]>=temp[0]-15) and(tmp[1]<=temp[1]+15 and tmp[1]>=temp[1]-15)):
                a=temp
                return a
    def search2(self,tmp):
        for i in range(len(self.nodes)):
            temp=self.nodes[i]
            #print(temp)
            a=(0,0)
            if((tmp[0]<=temp[0]+15 and tmp[0]>=temp[0]-15) and(tmp[1]<=temp[1]+15 and tmp[1]>=temp[1]-15)):
               
                return i

    
    def MidAdd(self,event):
        
        if(self.fflag==1):
            tmp=(event.x,event.y)
            for i in range(len(self.nodes)):
                temp=self.nodes[i]
                if((c1[0]<=temp[0]+15 and c1[0]>=temp[0]-15) and(c1[1]<=temp[1]+15 and c1[1]>=temp[1]-15)):
                    l=self.canvas.create_line((c1[0],c1[1],tmp[0],tmp[1]),fill="lawn green",width=2)
                    self.v.append(l)
            if(len(self.v)>0):
                for i in range(len(self.v)-1):
                    self.canvas.delete(self.v[i])
        else:
            c=0
        
            
  

    
        

    def EndAdd(self,event):
        global c1,x_axis,mat
        t2=(event.x,event.y)
        c2=self.search(t2)
        
        y_axis=self.search2(t2)
        a=(x_axis,y_axis)
        try:
            if(c2 is None):
                self.click_node()
            elif((c2[0] is not c1[0]) and (c2[1] is not c1[1])):
                self.canvas.delete(self.v[len(self.v)-1])
                if a not in self.edges:
                    x1,y1,x2,y2=c1[0],c1[1],c2[0],c2[1]
                    m=abs((y2-y1)/(x2-x1))
                    theta=(math.atan(m))

                    #print(theta)
                    if(x1<=x2 and y1>=y2):
                        c1=(x1+15*math.cos(theta),y1-15*math.sin(theta))
                        c2=(x2-15*math.cos(theta),y2+15*math.sin(theta))
                    elif(x1>x2 and y1>y2):
                        c1=(x1-15*math.cos(theta),y1-15*math.sin(theta))
                        c2=(x2+15*math.cos(theta),y2+15*math.sin(theta))
                    elif(x1<x2 and y1<y2):
                        c1=(x1+15*math.cos(theta),y1+15*math.sin(theta))
                        c2=(x2-15*math.cos(theta),y2-15*math.sin(theta))
                    elif(x1>x2 and y1<y2):
                        c1=(x1-15*math.cos(theta),y1+15*math.sin(theta))
                        c2=(x2+15*math.cos(theta),y2-15*math.sin(theta))
                    
                    
                    if self.DIR_BIT==1:
                       
                        
                        x=self.canvas.create_line((c1[0],c1[1],c2[0],c2[1]),fill="lawn green",width=3,joinstyle=ROUND,arrow=LAST,capstyle=ROUND,arrowshape=(16,20,6),smooth=TRUE)
                    else:
                        x=self.canvas.create_line((c1[0],c1[1],c2[0],c2[1]),fill="lawn green",width=3,smooth=TRUE)
                    self.edge_placing.append(x)
                    self.str_e=StringVar()
                    self.distance.append(self.str_e)
                    self.ent_count=self.ent_count+1
                    self.flag10=0
                    self.distance[self.count]=self.def_d
                    e=Entry(self.canvas,textvariable=self.distance[self.count],width=3,bg="tomato")
                    tmp1,tmp2=(c1[0]+c2[0])/2,(c1[1]+c2[1])/2
                    e.place(x=((c1[0]+tmp1)/2),y=((c1[1]+tmp2)/2))
                #print(c1,c2)
                    self.entry_values.append(e)
                    self.ent_count=self.ent_count+1
            
                    self.count=self.count+1
            
                    edge=(x_axis,y_axis)
                    self.edges.append(edge)
                    self.history.append("edgeadd")
                
                else:
                    self.muledgemsg()
            else:
                if a in self.edges:
                    self.muledgemsg()
                else:
                    
                    if c1[1]>300:
                        x=self.canvas.create_line(c1[0]-16,c1[1]+3,c1[0]+10,c1[1]+130 ,c2[0]+15,c2[1]+5, width=3, fill = "lawn green",joinstyle=ROUND,arrow=LAST,capstyle=ROUND,arrowshape=(16,20,6), smooth = True)
                    else:
                        x=self.canvas.create_line(c1[0]-16,c1[1]+3,c1[0]+10,c1[1]-130 ,c2[0]+15,c2[1]+5, width=3, fill = "lawn green",joinstyle=ROUND,arrow=LAST,capstyle=ROUND,arrowshape=(16,20,6), smooth = True)
                        self.canvas.tag_lower(x)
                    
                    self.edge_placing.append(x)
                    self.str_e=StringVar()
                    self.distance.append(self.str_e)
                    self.ent_count=self.ent_count+1
                    self.flag10=0
                    e=Entry(self.canvas,textvariable=self.distance[self.count],width=3,bg="tomato")
                    tmp1,tmp2=(c1[0]+c2[0])/2,(c1[1]+c2[1])/2
                    if c1[1]>300:
                        e.place(x=((c1[0]+tmp1)/2),y=((c1[1]+tmp2)/2)+60)
                    else:
                        e.place(x=((c1[0]+tmp1)/2),y=((c1[1]+tmp2)/2)-60)
                    self.entry_values.append(e)
                    self.ent_count=self.ent_count+1
            
                    self.count=self.count+1
            
                    edge=(x_axis,x_axis)
                    self.edges.append(edge)
                    self.history.append("edgeadd")
    
        except:
            pass
        
        
    def undo(self):
        if len(self.history)>0:
            x=self.history[len(self.history)-1]
            if x=="nodeadd":
                self.DelNode()
                self.history=self.history[:-1]
            if x=="edgeadd":
                self.DelEdge()
                self.history=self.history[:-1]
            
                
    def DisInput(self):
        self.dis_count=0
        for i in range(len(self.edges)):
            y=self.distance[i]
            input=y.get()
            if(len(input)==0):
                c=0
            else:
                try:
                    x=int(input)
                    #print(x)
                    
                    if x==0:
                        
                        tkinter.messagebox.showinfo("Warning","Distance should not be 0(zero).")
                        self.disz=1
                        break
                    else:
                        ee=self.edges[i]
                        #print(ee)
                        if self.DIR_BIT==1:
                            self.mat[ee[0]][ee[1]]=x
                        else:
                            self.mat[ee[0]][ee[1]]=x
                            self.mat[ee[1]][ee[0]]=x
                    
                        self.dis_count=self.dis_count+1
                except:
                    self.flag5=0
                    self.flag8=1
                    self.inv()
                
        
        
        

    def StopEdges(self):
        
        self.set_edge.configure(bg="white")
        self.canvas.bind("<Button-1>",'')
        self.canvas.bind("<B1-Motion>",'')
        self.canvas.bind("<ButtonRelease-1>",'')

    def PrintMatrix(self):

        global i
        for k in range(self.i):
            for l in range(self.i):
                print(self.mat[k][l],sep=' ',end=' ')
            print('\n')

    def click_node(self):
        try:
            self.canvas.delete(self.v[len(self.v)-1])
        except:
            c=0

    def same_node(self):
        tkinter.messagebox.showinfo("Warning", "Do not drop cursor on the same node.Try to drop on another node.")

    def RUN(self,event=0):
        self.flag9=1
        self.disz=0
        if len(self.nodes)>0:
            self.RUN2()
        else:
            
            self.nothing()
    def RUN2(self):
        self.flag1=1
        self.flag5=1
        if self.flagchk==0:
            self.mat= [[0 for _ in range(self.i)] for _ in range(self.i)]
        

        self.set_nodes.config(bg="white")
        self.set_edge.config(bg="white")
        self.run.config(bg="lawn green")
        self.canvas.bind("","")
            
        self.StopEdges()
        self.StopNode()
        self.DisInput()
        #self.PrintMatrix()
        if self.disz is not 1:
            self.run3()

    def run3(self):
        if((self.dis_count > len(self.edges)) or (self.dis_count < len(self.edges))):
            if(self.flag8 ==0):
                self.any_dis()
        else:
            input=self.str_s.get()
            if(len(input)==0):
                self.none_message()
            else:
                try:
                    res=int(input)
                    if(res>self.i or res<1):
                        self.out_of_range()
                    else:
                        
                        
                        self.dijkstra(self.mat,res-1,self.i)
                        
                    self.flag5=0
                except:
                    self.flag5=0
                    self.invalid()

    def inv(self):
        tkinter.messagebox.showinfo("Warning", "There is some invalid distance.")

        
    def invalid(self):
        
        tkinter.messagebox.showinfo("Warning", "Invalid Starting Node.")

    def any_dis(self):
        
        tkinter.messagebox.showinfo("Warning", "Some Distances are empty.")

    def none_message(self):
        tkinter.messagebox.showinfo("Warning", "Starting Node cannot be Empty.")

    def nothing(self):
        tkinter.messagebox.showinfo("Warning", "Graph is Empty.First draw a graph (isolated graph also), then click RUN.")

    def out_of_range(self):
        tkinter.messagebox.showinfo("Caution", "This Node does not exist in your Graph.")

    def RESET(self):
        if (messagebox.askyesno(message='Are you sure you want to Reset?' ,icon='question' ,title='Reset')):
            App()
    def EXIT(self):
        if len(self.nodes)==0:
            root.destroy()
            try:
                self.win.destroy()
            except:
                pass
            try:
                self.win2.destroy()
            except:
                pass
        else:
            self.exit2()

    def exit2(self):
            
        s=messagebox.askyesnocancel(message='Do you want to save your work before Exit?' ,icon='question' ,title='Exit')
        if s==None:
            pass
        elif s==False:
            root.destroy()
            try:
                self.win.destroy()
            except:
                pass
            try:
                self.win2.destroy()
            except:
                pass
            
        elif s==True:
            if len(self.nodes)>0:
                self.SAVE()
            root.destroy()
            try:
                self.win.destroy()
            except:
                pass
            try:
                self.win2.destroy()
            except:
                pass
      
    def NodeClear(self):
        
        if len(self.node_placing)>0:
            if (messagebox.askyesno(message='Are you sure you want to Clear all the Nodes?' ,icon='question' ,title='Verify')):
                if len(self.label_values)>0:
                    for i in range(len(self.label_values)):
                        self.label_values[i].place_forget()
                for i in range(len(self.node_placing)):
                    self.canvas.delete(self.node_placing[i])
                self.node_placing=self.node_placing[:-len(self.node_placing)]
                if len(self.edge_placing)>0:
                    for i in range(len(self.edge_placing)):
                        self.canvas.delete(self.edge_placing[i])
                    
                        self.entry_values[i].place_forget()
                #print(self.i)
                
                self.i=0
                #print(self.i)
            
                del self.nodes
                self.nodes=[]
                App()
        else:
            self.nodemsg()

    def nodemsg(self):
        tkinter.messagebox.showinfo("Warning", "There is no node in the Graph.")

    def EdgeClear(self):
        
        if len(self.edge_placing)>0:
            if (messagebox.askyesno(message='Are you sure you want to Clear all the Edges?' ,icon='question' ,title='Verify')):
                if len(self.label_values)>0:
                    for i in range(len(self.label_values)):
                        self.label_values[i].place_forget()
                for i in range(len(self.edge_placing)):
                    self.canvas.delete(self.edge_placing[i])
                    self.entry_values[i].place_forget()
                self.edge_placing=[]
                self.entry_values=[]
                self.distance=[]
                self.ent_count=0
                self.count=0
                self.matclear()
                
                
        else:
            self.edgemsg()

    def edgemsg(self):
        tkinter.messagebox.showinfo("Warning", "There is no Edge in the Graph.")

    def finddel(self):
        
        l=len(self.node_placing)
        x=self.i-1
        
        #print(self.ent_get_values)
        #print(self.edges)
        #print(x)
        a,g,l,e=[],[],[],[]
        #self.PrintMatrix()
        #print(self.entry_values)
        #for i in range(self.i):
            #print(self.mat[x][i],end='      ')
        for i in range(len(self.edges)):
            b=self.edges[i]
            if x==b[0] or x==b[1]:
                a.append(i)
                l.append(self.edge_placing[i])
                #e.append(i])
                g.append(b)
        #print(self.edge_placing)
        #print(self.edges)
        #print(a)
                
        #print(self.ent_get_values)
        if len(a)>0:
            for i in range(len(a)):
                c=a[i]
                self.canvas.delete(self.edge_placing[c])
                self.ent_count=self.ent_count-1
                self.count=self.count-1
                e.append(self.entry_values[c])
                self.entry_values[c].place_forget()
                
                
                
        if len(g)>0:
            for i in range(len(g)):
                y=g[i]
                self.mat[y[0]][y[1]]=0
                self.mat[y[1]][y[0]]=0
                self.edges.remove(y)
        if len(l)>0:
            for i in range(len(l)):
                self.edge_placing.remove(l[i])
        #print(a)
        self.distance=[i for j,i in enumerate(self.distance) if j not in a]

        if len(e)>0:
            for i in range(len(e)):
                self.entry_values.remove(e[i])
        
        #print(self.edges)
        #print(self.entry_values)
        #print(self.edge_placing)
        #print(self.ent_get_values)      
        #self.PrintMatrix()
        

        
    def DelNode(self):
        
        
        l=len(self.node_placing)
        if l>0:
            if len(self.edges)>0:
                self.finddel()
            if len(self.label_values)>0:
                for i in range(len(self.label_values)):
                    self.label_values[i].place_forget()
            self.canvas.delete(self.node_placing[l-1])
            self.canvas.delete(self.node_placing[l-2])
            self.node_placing=self.node_placing[:-2]
            self.nodes=self.nodes[:-1]
            self.i=self.i-1
            if len(self.edges)>0:
                self.mat= [[0 for _ in range(self.i)] for _ in range(self.i)]
                '''for i in range(self.i):
                    for j in range(self.i):
                        self.mat2[i][j]=self.mat[i][j]'''
                #self.mat=self.mat2
                #del self.mat2

            
            '''for k in range(self.i):
                for l in range(self.i):
                    print(self.mat[k][l],sep=' ',end=' ')
                print('\n')'''
                
            #self.PrintMatrix()
            if(len(self.nodes))==0:
                App()
                
        else:
            self.nodemsg()
            App()
        
            

    def DelEdge(self):
        
        if self.flag7==1 or self.flag7==0:
            l=len(self.edge_placing)
            if l>0:
                if len(self.label_values)>0:
                    for i in range(len(self.label_values)):
                        self.label_values[i].place_forget()
                self.canvas.delete(self.edge_placing[l-1])
                self.entry_values[l-1].place_forget()
                self.edge_placing=self.edge_placing[:-1]
                self.entry_values=self.entry_values[:-1]
                #print(self.edges)
                self.ent_count=self.ent_count-1
                self.count=self.count-1
                self.distance=self.distance[:-1]
                x=self.edges[len(self.edges)-1]
                #print(x)
                self.mat[x[0]][x[1]]=0
                self.mat[x[1]][x[0]]=0
                self.edges=self.edges[:-1]
                #print(self.edges)
            else:
                self.edgemsg()
        

    def nodemsg2(self):
        tkinter.messagebox.showinfo("Warning", "Node cannot be deleted when there is an edge in graph.")

    def edgemsg2(self):
        tkinter.messagebox.showinfo("Warning", "Edges cannot be deleted.")

    def muledgemsg(self):
        tkinter.messagebox.showinfo("Warning", "Multiple Edges are not allowed.")

    def no_sol(self):
        tkinter.messagebox.showinfo("Warning", "First make a graph and Run algorithm ,then check for detailed solution. ") 

    def matclear(self):
        
        self.edges=[]
        
        
        self.mat= [[0 for _ in range(self.i)] for _ in range(self.i)]

    def create_sol(self):
        c=0
        

    def mindis(self,dist,sptset,v):
        m=INF
        for i in range(0,v):
            if(sptset[i]==0 and dist[i]<=m):
                m=dist[i]
                min_index=i
        return min_index


    def dijkstra(self,graph,src,n):
        self.flag11=1
        
        global file
        
        file=open("tmp.txt","w")
        text1="The solution of the graph entered by you is given as follows:"
        file.write(text1)
        file.write("\n Make two arrays:-\n\n dist={}   -- The output array.dist[i] will hold the shortest distance from src to i.\n sptset={}  --\
 sptSet[i] will true if vertex i is included in shortest path tree or shortest distance from src to i is finalized")
        file.write("\n\n Source Node = ")
        file.write(str(src))
        file.write("\n")
        file.write("\n\nStep 0: Initialization.\n")
        file.write("\n\t //Initialize all distances as INFINITE and stpSet[] as false")
        file.write("\n\n\t dist -->  ")
        
        dist=[0 for _ in range(n)]
        sptset=[False for _ in range(n)]
        for i in range(len(dist)):
            file.write(str(dist[i]))
            file.write("  ")
        file.write("\n\n\t sptset -->  ")
        for i in range(len(sptset)):
            file.write(str(sptset[i]))
            file.write("  ")
        
        file.write("\n\n Step 1: Make dist[")
        file.write(str(src))
        file.write("]=0 and initialise dist INF .\n")

        
    

        for i in range(0,n):
            dist[i],sptset[i]=INF,False
        dist[src]=0
        file.write("\n\n\t dist -->  ")
        for i in range(len(dist)):
            if dist[i]==INF:
                file.write("INF")
            else:
                file.write(str(dist[i]))
            file.write("  ")
        file.write("\n\n\t sptset -->  ")
        for i in range(len(sptset)):
            file.write(str(sptset[i]))
            file.write("  ")
        
        for i in range(0,n-1):
            file.write("\n Step ")
            tmp=i+2
            file.write(str(tmp))
            file.write(":\n")
            
            u=self.mindis(dist,sptset,n)
            sptset[u]=1
            for j in range(0,n):
                if(sptset[j]==False and graph[u][j] and (dist[u] is not INF) and dist[u]+graph[u][j]<dist[j]):
                    dist[j]=dist[u]+graph[u][j]
            file.write("\n\n\t dist -->  ")
            for i in range(len(dist)):
                if dist[i]==INF:
                    file.write("INF")
                else:
                    file.write(str(dist[i]))
                file.write("  ")
            file.write("\n\n\t sptset -->  ")
            for i in range(len(sptset)):
                file.write(str(sptset[i]))
                file.write("  ")
            file.write("\n")
        file.write("\n Final Results:\n")
        file.write("\n\n           Source Node = ")
        file.write(str(src+1))
        file.write("\n")
        file.write("\n\t\t Node \t\t Distance\n\n")
        for i in range(len(dist)):
            file.write("\t\t ")
            x=i+1
            file.write(str(i+1))
            file.write(" \t\t ")
            if dist[i]==INF:
                file.write("INF")
            else:
                file.write(str(dist[i]))
            file.write("\n\n")
        file.close()
        
        #print(sptset)
        #print(dist)

        self.prin(src,dist,n)


    def out(self,src,dist,n):
        for i in range(src,n):
            
            tmp=self.nodes[i]
            if((int)(dist[i])==INF):
                l=Label(self.canvas,text="INF",width=3,bg="khaki")
                l.place(x=tmp[0]+10,y=tmp[1]-10)
                self.label_values.append(l)
            
            else:
                l=Label(self.canvas,text=(int)(dist[i]),width=3,bg="cyan")
                l.place(x=tmp[0]+10,y=tmp[1]-10)
                self.label_values.append(l)
            self.canvas.update()


    def prin(self,src,dist,n):
        if len(self.label_values)>0:
            for i in range(len(self.label_values)):
                self.label_values[i].place_forget()
                
        if(src>0):
            self.out(src,dist,n)
            self.out(0,dist,src)
        elif(src==0):
            self.out(0,dist,n)
    def Show(self):
        if self.flag9==0:
            self.no_sol()
        else:
            self.show_sol()
    
    def show_sol(self):
        self.win=Tk()
        self.win.title("Solution")
        self.win.attributes("-toolwindow",1)
        self.win.geometry("705x500")
        self.win.resizable(0,0)
        f=Frame(self.win,width=650,height=485,bd=3,relief=SUNKEN)
        f.place(x=17,y=15)
        Button(self.win,text="Close",command=self.win.destroy).place(x=380,y=435)
        Button(self.win,text="Save As..",command=self.save).place(x=200,y=435)
        t=Text(f,bg="white",wrap=NONE)
        vscrollbar=Scrollbar(f)
        vscrollbar.pack(side=RIGHT,fill=Y)
        vscrollbar.config( command = t.yview )

        hscrollbar=Scrollbar(f,orient=HORIZONTAL)
        hscrollbar.pack(side=BOTTOM,fill=X)
        hscrollbar.config( command = t.xview )
        t.config(yscrollcommand=vscrollbar.set,xscrollcommand=hscrollbar.set)
        t.pack()
        fin=open("tmp.txt","r")
        
        txt=fin.read()
        t.insert(END,txt)
        t.config(state=DISABLED)
        

    def save(self):
        try:
            filename=StringVar()
            filename.set(filedialog.asksaveasfilename(defaultextension = ".txt", filetypes=[("All Types", ".*")]))
            s=filename.get()
            
            fin=open("tmp.txt","r")
            txt=fin.read()
            fout=open(s,"w")
            fout.write(txt)
        except:
            tkinter.messagebox.showinfo("Warning", "File not saved. ")


    def Help(self):
        self.win2=Tk()
        self.win2.title("Help")
        self.win2.geometry("600x560")
        self.win2.resizable(0,0)
        self.win2.attributes("-toolwindow",1)
        Label(self.win2,text="Setting Nodes",bg="white").place(x=20,y=5)
        node="For making nodes in the graph,first click on 'Set' under Nodes in the 'Graph Construction' Tab.\
\n\n    ** Then click anywhere in the graph to set Nodes.\
\n    ** Del button delete the latest added node in the graph.\
\n    ** Clear All button removes all the nodes and their associated        edges from the graph and makes graph empty."
        t=Text(self.win2,bg="white",width=70,height=8)
        t.pack(pady=35)
        t.insert(END,node)
        t.config(state=DISABLED)
        edge="For making edges in the graph,first click on 'Set' under Edges in the 'Graph Construction' Tab.\
\n\n    ** Then click on the first Nodes and drag upto the another node to    create an edge between two nodes.\
\n    ** Del button delete the latest added edge in the graph.\
\n    ** Clear All button removes all the edges from the graph."
        Label(self.win2,text="Setting Edges",bg="white").place(x=20,y=175)
        t1=Text(self.win2,bg="white",width=70,height=8)
        t1.pack(pady=5)
        t1.insert(END,edge)
        t1.config(state=DISABLED)
        run="'Run Algorithm' Button runs the algorithm and shows the result.\
\n\n    ** To run an algorithm first provide the starting node in the         respective entry box."
        Label(self.win2,text="Run Algorithm",bg="white").place(x=20,y=345)
        t1=Text(self.win2,bg="white",width=70,height=4)
        t1.pack(pady=27)
        t1.insert(END,run)
        t1.config(state=DISABLED)
        chk="'Check solution' button gives the detailed solution of the graph that can be saved into a file."
        Label(self.win2,text="Check Solution",bg="white").place(x=20,y=445)
        t1=Text(self.win2,bg="white",width=70,height=4)
        t1.pack(pady=5)
        t1.insert(END,chk)
        t1.config(state=DISABLED)


    def NEW(self):
        
        if len(self.nodes)==0:
            App()
        else:
            s=messagebox.askyesnocancel(message='Do you want to save your work?' ,icon='question' ,title='New..')
            if s==None:
                pass
            elif s==False:
                App()
            elif s==True:
                self.SAVE()
                App()
            

    def SAVE(self):
        if len(self.nodes)==0:
            messagebox.showinfo("Warning","The Graph is empty. First draw a graph ,ten save the file.")
        else:
            self.save2()

    def save2(self):
        
        if self.fileopen==1:
            s=self.filename
        else:
            filename=StringVar()
            if self.DIR_BIT==1:
                filename.set(filedialog.asksaveasfilename(defaultextension = ".ddij", filetypes=[("Algorithm Files", ".ddij"),("All Files", ".*")]))
            else:
                filename.set(filedialog.asksaveasfilename(defaultextension = ".udij", filetypes=[("Algorithm Files", ".udij"),("All Files", ".*")]))
            s=filename.get()
        try:
            fout=open(s,"wb")
            
            endl='\n'
            mul=[]
            
            for i in range(len(self.nodes)):
                x=list(self.nodes[i])
                a=int(x[0]/127)
                mul.append(a)
                x[0]=x[0]%127
                if(x[0]==10):
                    x[0]=x[0]+1
                b=int(x[1]/127)
                mul.append(b)
                x[1]=x[1]%127
                if(x[1]==10):
                    x[1]=x[1]+1
            
                fout.write(struct.pack('2b',*x))
        
            fout.write(endl.encode('ascii'))
            p=str(len(mul))+'b'
            fout.write(struct.pack(p,*mul))
        
            fout.write(endl.encode('ascii'))
            mul=[]
            for i in range(len(self.edges)):
                x=list(self.edges[i])
                
                fout.write(struct.pack('2b',*x))
        
             
            fout.write(endl.encode('ascii'))
            val=[]
            
            for i in range(len(self.edges)):
                y=self.distance[i]
                input=y.get()
                if(len(input)==0):
                    val.append(0)
                else:
                    try:
                        x=int(input)
                        val.append(x)
                    except:
                        messagebox.showinfo("Warning","Unable to save file.There is some invalid distance.")
            #print(val)
            l1=len(val)
            p=str(l1)+'Q'
            for i in range(l1):
                fout.write(struct.pack('l',val[i]))
            
            messagebox.showinfo("Message","File Saved.")

            
            fout.close()
        except:
            messagebox.showinfo("Warning","File not saved.")
        
            
        

    def ClearCan(self):
        if len(self.edge_placing)>0:
            if len(self.label_values)>0:
                for i in range(len(self.label_values)):
                    self.label_values[i].place_forget()
            for i in range(len(self.edge_placing)):
                self.canvas.delete(self.edge_placing[i])
                self.entry_values[i].place_forget()
            self.edge_placing=[]
            self.entry_values=[]
            self.distance=[]
            self.ent_count=0
            self.count=0
            self.matclear()
        l=len(self.node_placing)
            
        if l>0:
            while True:
                if l==0:
                    break
                else:
                    self.canvas.delete(self.node_placing[l-1])
                    self.canvas.delete(self.node_placing[l-2])
                    self.node_placing=self.node_placing[:-2]
                    self.nodes=self.nodes[:-1]
                    self.i=self.i-1
                    l=l-2
        self.val_init()
            
                
        

    def OPEN(self):
        if len(self.nodes)==0:
            self.Open2()
            
        elif self.one==0:
            
            self.Open2()
            
        elif self.one==1:
            s=messagebox.askyesnocancel(message='Do you want to save your work?' ,icon='question' ,title='Open file')
            if s==None:
                pass
            elif s==False:
                
                self.Open2()
            elif s==True:
                self.SAVE()
                
                self.Open2()
        

    def Open2(self):
        
        
        filename=StringVar()
        x=filedialog.askopenfilename(defaultextension = (".ddij",".udij"), filetypes=[("Algorithm Files", ".ddij"),("Algorithm Files", ".udij"),("All Files", ".*")])
        
        dia=filename.set(x)
        
        s=filename.get()
        
        if '.ddij' in s or '.udij' in s:
            self.ClearCan()
            self.open1(s)
            
            
        else:
            if len(x) is not 0:
                self.open_chk_flag=1
                self.val_init()
            
            if dia is not None:
                self.filecor=1
                messagebox.showinfo("Warning","Not a supported file.")

    def open1(self,s):
        
        cnt=0
        self.filename=s
        self.fileopen=1
        if '.ddij' in s:
            self.DIR_BIT=1
        else:
            self.DIR_BIT=0
        #print(self.DIR_BIT)
        with open(s,"rb") as fin:
            values=[]
            for l in fin:
                l.split()
                if l:
                    l=[int(i) for i in l]
                    cnt=cnt+1
                    if cnt is not 4:
                        l=l[:-1]
                    
                    values.append(l)
        #print(values)
        f1,f2,f3=0,0,0
        global n,e,d
        try:
            n=values[0]
            m=values[1]
            f1=1
        except:
            messagebox.showinfo("Message","The file is empty.")

        try:
            if len(values[2])>0:
                e=values[2]
                
                f2=1
            elif len(values)==3 and len(values[2])==0:
                values=values[:-1]
        except:
            pass
        d1=[]
        try:
            if len(values[3])>0:
                for i in range(3,len(values)):
                    x=values[i]
                    d1=d1+x
                f3=1
        except:
            pass
        #print("d1=",d1)
        self.d=[]
        self.mul=[]
        k=0
        while True:
            if k==len(d1) or k >len(d1)+1:
                break
            else:
                self.d.append(d1[k]%256)
                try:
                    self.mul.append(d1[k+1])
                except:
                    pass
                k=k+4


        #print("a=",self.d)
        #print(self.mul)
        #print(f1,f2,f3)
        flag=0
        if f1==1:
            c1=0
            #print(n)
            try:
                while True:
                    if c1==len(n):
                        break
                    else:
                
                        a=((n[c1]+(m[c1]*127)),(n[c1+1]+(m[c1+1]*127)))
                
                        self.nodes.append(a)
                        c1=c1+2
            
            
                
                for i in range(len(self.nodes)):
                    s=self.nodes[i]
                    x=self.canvas.create_oval((s[0]-15,s[1]-15,s[0]+15,s[1]+15),fill="violet red",width=2,outline="gray",tag='bubbles')
                    y=self.canvas.create_text(s[0],s[1],font=6,text=self.i+1,activefill="green",fill="white")
            
                    self.node_placing.append(x)
                    self.node_placing.append(y)
                    self.i=self.i+1
                    self.mat= [[0 for _ in range(self.i)] for _ in range(self.i)]
            
                
            
                
            except:
                messagebox.showinfo("Message","File cannot be opened.The file may be corrupted.")
                flag=1
                
                App()
            if f2==1 and flag==0:
                self.op2(e,s,f3)
            else:
                self.changename()
            
                
    

    def op1(self,n):
        print("op1")
        

    def op2(self,e,nf,f3):
        c2=0
        flag=0
        try:
            
            while True:
                if c2==len(e):
                    break
                else:
                
                    a=(e[c2],e[c2+1])
                
                    self.edges.append(a)
                    c2=c2+2
            for i in range(len(self.edges)):
                s=self.edges[i]
                c1,c2=self.nodes[s[0]],self.nodes[s[1]]
                if s[0]==s[1]:
                    if c1[1]>300:
                        x=self.canvas.create_line(c1[0]-16,c1[1]+3,c1[0]+10,c1[1]+130 ,c2[0]+15,c2[1]+5, width=3, fill = "lawn green",joinstyle=ROUND,arrow=LAST,capstyle=ROUND,arrowshape=(16,20,6), smooth = True)
                    else:
                        x=self.canvas.create_line(c1[0]-16,c1[1]+3,c1[0]+10,c1[1]-130 ,c2[0]+15,c2[1]+5, width=3, fill = "lawn green",joinstyle=ROUND,arrow=LAST,capstyle=ROUND,arrowshape=(16,20,6), smooth = True)
                else:
                    x1,y1,x2,y2=c1[0],c1[1],c2[0],c2[1]
                    m=abs((y2-y1)/(x2-x1))
                    theta=(math.atan(m))

                    #print(theta)
                    if(x1<=x2 and y1>=y2):
                        c1=(x1+15*math.cos(theta),y1-15*math.sin(theta))
                        c2=(x2-15*math.cos(theta),y2+15*math.sin(theta))
                    elif(x1>x2 and y1>y2):
                        c1=(x1-15*math.cos(theta),y1-15*math.sin(theta))
                        c2=(x2+15*math.cos(theta),y2+15*math.sin(theta))
                    elif(x1<x2 and y1<y2):
                        c1=(x1+15*math.cos(theta),y1+15*math.sin(theta))
                        c2=(x2-15*math.cos(theta),y2-15*math.sin(theta))
                    elif(x1>x2 and y1<y2):
                        c1=(x1-15*math.cos(theta),y1+15*math.sin(theta))
                        c2=(x2+15*math.cos(theta),y2-15*math.sin(theta))
                    if self.DIR_BIT==1:
                        x=self.canvas.create_line((c1[0],c1[1],c2[0],c2[1]),fill="lawn green",width=3,joinstyle=ROUND,arrow=LAST,capstyle=ROUND,arrowshape=(16,20,6),smooth=TRUE)
                    else:
                        x=self.canvas.create_line((c1[0],c1[1],c2[0],c2[1]),fill="lawn green",width=3,smooth=TRUE)
                
                self.edge_placing.append(x)
                self.str_e=StringVar()
                self.distance.append(self.str_e)
                self.ent_count=self.ent_count+1
                self.flag10=0
                e=Entry(self.canvas,textvariable=self.distance[self.count],width=3,bg="tomato")
                tmp1,tmp2=(c1[0]+c2[0])/2,(c1[1]+c2[1])/2
                if s[0]==s[1]:
                    if c1[1]>300:
                        e.place(x=((c1[0]+tmp1)/2),y=((c1[1]+tmp2)/2)+60)
                    else:
                        e.place(x=((c1[0]+tmp1)/2),y=((c1[1]+tmp2)/2)-60)
                else:
                    e.place(x=((c1[0]+tmp1)/2),y=((c1[1]+tmp2)/2))
            #print(c1,c2)
                self.entry_values.append(e)
                self.ent_count=self.ent_count+1
                self.count=self.count+1
            

        except:
                messagebox.showinfo("Message","File cannot be opened.The file may be corrupted.")
                flag=1
                
                App()
        if flag==0 and f3==1:
            self.op3(nf)
        else:
            self.changename()
                        
        
        
        #print(self.edges)
        
            

    def op3(self,nf):

        c3=0
        self.dis_count=0
        #print(self.d,self.mul)
        try:
            
            for i in range(len(self.edges)):
                y=(self.mul[i]*256)+(self.d[i])
                #print(y)
                if self.d[i]==0:
                    
                    self.dis_count=self.dis_count+1
                else:
                    self.entry_values[i].insert(END,y)
                    self.dis_count=self.dis_count+1
        except:
                messagebox.showinfo("Message","File cannot be opened.The file may be corrupted.")
                
                
                App()
        if self.filecor==0:
            self.changename()

    def changename(self):
        na=self.filename
        
        '''k=len(na)-5
        
        cx=""
        while(True):
            
            if (na[k]=='/'):
                break
            else:
                cx=cx+na[k]
            k=k-1
        l=len(cx)-1'''
        sc=""
        '''while l>=0:
            sc+=cx[l]
            l=l-1'''
        sc+=na
        sc+=" - DIJKSTRA'S ALGORITHM"
        #print(sc)
        root.title(sc)
                    
            
            
           
        
        

    def StopMove(self):
        self.canvas.bind("","")

        
    def Move(self):
        self.movetool.configure(relief=SUNKEN)
        self.StopEdges()
        if len(self.label_values)>0:
            for i in range(len(self.label_values)):
                self.label_values[i].place_forget()
        self.canvas.bind("<Button-1>",self.movenodes)
        
    def movenodes(self,event):
        if len(self.label_values)>0:
                    for i in range(len(self.label_values)):
                        self.label_values[i].place_forget()
        s=(event.x,event.y)
        self.ind=self.INNodes(s)
        print(self.ind)
        #print(ind)
        if self.ind is not -1:
            self.reled,self.reln,self.orien,self.ed=[],[],[],[]
            for i in range(len(self.edges)):
                b=self.edges[i]
                #print(b)
                if self.ind==b[0] or self.ind==b[1]:
                    if self.ind==b[0]:
                        self.reln.append(b[1])
                        self.orien.append(0)
                    elif self.ind==b[1]:
                        self.reln.append(b[0])
                        self.orien.append(1)
                    self.ed.append(b)
                    self.reled.append(i)
            #print(self.reln)
            self.canvas.bind("<B1-Motion>",self.MidMove)
            #self.canvas.bind("<ButtonRelease-1>",self.EndMove)
        else:
            self.canvas.bind("<B1-Motion>",self.Empty)
            pass

    def Empty(self,event):
        return 0
    
    def MidMove(self,event):
        
        self.canvas.delete(self.node_placing[self.ind*2])
        self.canvas.delete(self.node_placing[self.ind*2+1])
        for i in range(len(self.reled)):
            self.canvas.delete(self.edge_placing[self.reled[i]])
            self.entry_values[self.reled[i]].place_forget()
        s=(event.x,event.y)
        
        x=self.canvas.create_oval((s[0]-15,s[1]-15,s[0]+15,s[1]+15),fill="violet red",width=2,outline="gray",tag='bubbles')
        y=self.canvas.create_text(s[0],s[1],font=6,text=self.ind+1,activefill="green",fill="white")
        
        c1=s
        x3,y1=c1[0],c1[1]
        for i in range(len(self.reled)):
            
            c2=self.nodes[self.reln[i]]
            a=self.ed[i]
            x2,y2=c2[0],c2[1]
            numer,denom=(y2-y1),(x2-x3)
            if denom is 0:
                
                return
            if numer is 0:
                
                return
            
            m=abs(numer/denom)
            theta=(math.atan(m))

                    #print(theta)
            if(x3<=x2 and y1>=y2):
                c1=(x3+15*math.cos(theta),y1-15*math.sin(theta))
                c2=(x2-15*math.cos(theta),y2+15*math.sin(theta))
            elif(x3>x2 and y1>y2):
                c1=(x3-15*math.cos(theta),y1-15*math.sin(theta))
                c2=(x2+15*math.cos(theta),y2+15*math.sin(theta))
            elif(x3<x2 and y1<y2):
                c1=(x3+15*math.cos(theta),y1+15*math.sin(theta))
                c2=(x2-15*math.cos(theta),y2-15*math.sin(theta))
            elif(x3>x2 and y1<y2):
                c1=(x3-15*math.cos(theta),y1+15*math.sin(theta))
                c2=(x2+15*math.cos(theta),y2-15*math.sin(theta))

            if a[0]==a[1]:
                
                if c1[1]>300:
                    x1=self.canvas.create_line(c1[0]-16,c1[1]+3,c1[0]+10,c1[1]+130 ,c2[0]+15,c2[1]+5, width=3, fill = "lawn green",joinstyle=ROUND,arrow=LAST,capstyle=ROUND,arrowshape=(16,20,6), smooth = True)
                else:
                    x1=self.canvas.create_line(c1[0]-15,c1[1]+3,c1[0]+10,c1[1]-130 ,c2[0]+15,c2[1]+5, width=3, fill = "lawn green",joinstyle=ROUND,arrow=LAST,capstyle=ROUND,arrowshape=(16,20,6), smooth = True)
                
                self.canvas.tag_lower(x1)
                e=Entry(self.canvas,textvariable=self.distance[self.reled[i]],width=3,bg="tomato")
                tmp1,tmp2=(c1[0]+c2[0])/2,(c1[1]+c2[1])/2
                if c1[1]<300:
                    e.place(x=((c1[0]+tmp1)/2),y=((c1[1]+tmp2)/2)-60)
                else:
                    e.place(x=((c1[0]+tmp1)/2),y=((c1[1]+tmp2)/2)+60)
                self.entry_values[self.reled[i]]=e
            elif self.orien[i]==0 and (a[0] is not a[1]) and self.DIR_BIT==1:
                

                x1=self.canvas.create_line((c1[0],c1[1],c2[0],c2[1]),fill="lawn green",width=3,joinstyle=ROUND,arrow=LAST,capstyle=ROUND,arrowshape=(16,20,6),smooth=TRUE)
                e=Entry(self.canvas,textvariable=self.distance[self.reled[i]],width=3,bg="tomato")
                tmp1,tmp2=(c1[0]+c2[0])/2,(c1[1]+c2[1])/2
                e.place(x=((c1[0]+tmp1)/2),y=((c1[1]+tmp2)/2))
                self.entry_values[self.reled[i]]=e
            elif self.orien[i]==1 and (a[0] is not a[1]) and self.DIR_BIT==1:
                
                x1=self.canvas.create_line((c2[0],c2[1],c1[0],c1[1]),fill="lawn green",width=3,joinstyle=ROUND,arrow=LAST,capstyle=ROUND,arrowshape=(16,20,6),smooth=TRUE)
                e=Entry(self.canvas,textvariable=self.distance[self.reled[i]],width=3,bg="tomato")
                tmp1,tmp2=(c1[0]+c2[0])/2,(c1[1]+c2[1])/2
                e.place(x=((c2[0]+tmp1)/2),y=((c2[1]+tmp2)/2))
                self.entry_values[self.reled[i]]=e

            elif self.DIR_BIT==0:
                
                
                x1=self.canvas.create_line((c1[0],c1[1],c2[0],c2[1]),fill="lawn green",width=3,smooth=TRUE)
                e=Entry(self.canvas,textvariable=self.distance[self.reled[i]],width=3,bg="tomato")
                tmp1,tmp2=(c1[0]+c2[0])/2,(c1[1]+c2[1])/2
                e.place(x=tmp1,y=tmp2)
                self.entry_values[self.reled[i]]=e

            self.edge_placing[self.reled[i]]=x1

            
                
                

            
        self.node_placing[self.ind*2]=x
        self.node_placing[self.ind*2+1]=y
        
        self.nodes[self.ind]=s
        
        
                
        
        

    def NotINNodes2(self,tmp):
        for i in range(len(self.nodes)):
            temp=self.nodes[i]
            #print(temp)
            a=(0,0)
            if((tmp[0]<=temp[0]+15 and tmp[0]>=temp[0]-15) and(tmp[1]<=temp[1]+15 and tmp[1]>=temp[1]-15)):
                
                return 1
        return 0

    
        
        

    def INNodes(self,tmp):
        print(tmp)
        for i in range(len(self.nodes)):
            temp=self.nodes[i]
            print(temp)
            a=(0,0)
            if((tmp[0]<=temp[0]+15 and tmp[0]>=temp[0]-15) and(tmp[1]<=temp[1]+15 and tmp[1]>=temp[1]-15)):
                
                return i
        return -1
                

App()
root.mainloop()
