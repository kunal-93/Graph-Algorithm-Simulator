from tkinter import *
from tkinter.filedialog import *
from tkinter.tix import *
from tkinter import messagebox
import os,struct,pickle,gzip


root=Tk()
root.state("zoomed")
#root.config(cursor="wait")
INF=9999999999999
NIL=-9999999999999

def quit():
    root.quit()


                                                     #Menu Functions
                                                            #File

    

class App(object):
    
    def __init__(self):
        
        foot=StringVar()
        head=StringVar()
        foot.set('@ KD AND KVNT')
        foot_label=Label(root,fg="black",textvariable=foot)
        foot_label.place(x=0,y=663,height=30,width=1030)
        self.tt=None


        menubar=Menu(root)
        filemenu=Menu(menubar,tearoff=0)
        filemenu.add_command(label="New",command=self.NEW,accelerator="Ctrl + N")
        filemenu.add_command(label="Open...",command=self.OPEN,accelerator="Ctrl + O")
        filemenu.add_command(label="Save",command=self.SAVE,accelerator="Ctrl + S ")
        filemenu.add_command(label="Save As ",command=self.SAVEON,accelerator="Ctrl + SHIFT + S")
        filemenu.add_command(label="Print ",command='',accelerator="Ctrl + P")
        filemenu.add_command(label="Exit",command=self.EXIT,accelerator="Alt +F4 ")
        menubar.add_cascade(label="File",menu=filemenu)

        editmenu=Menu(menubar,tearoff=0)
        editmenu.add_command(label="Undo",command='',accelerator="Ctrl + Z")
        editmenu.add_command(label="Redo",command='',accelerator="Ctrl + Y")
        editmenu.add_command(label="Cut",command='',accelerator="Ctrl + X")
        editmenu.add_command(label="Copy",command='',accelerator="Ctrl + C")
        editmenu.add_command(label="Paste",command='',accelerator="ctrl + V")
        editmenu.add_command(label="Delete",command='',accelerator="Del")
        #menubar.add_cascade(label="Edit",menu=editmenu)

        runmenu=Menu(menubar,tearoff=0)
        runmenu.add_command(label="Run Algo",command=self.dist_entry,accelerator="F5")
        menubar.add_cascade(label="Run",menu=runmenu)

        helpmenu=Menu(menubar,tearoff=0)
        helpmenu.add_command(label="module Help",command=self.help)
        helpmenu.add_command(label="About Algo",command=self.openalgo)
        menubar.add_cascade(label="Help",menu=helpmenu)

        
        root.configure(menu=menubar)


        self.statusbar=Label(root,relief=SUNKEN,bd=2,bg="white")
        self.statusbar.place(x=0,y=640,width=1030,height=25)

        b=tkinter.tix.Balloon(root,statusbar=self.statusbar)

               # graphFrame  for canvas
        global graphframe
        self.graphframe=Frame(root,relief=SUNKEN,bd=4)

        self.toolframe=Frame(root,relief=RAISED,bd=3,height=300,width=40,bg="white")
        self.toolframe.place(x=3,y=0)
        
        self.graphframe.grid(row=0,column=0,padx=44)
        self.canvas=Canvas(self.graphframe,bg="white",height=626,width=968)
        
        self.vscrollbar=Scrollbar(self.graphframe)
        #self.vscrollbar.pack(side=RIGHT,fill=Y)
        self.vscrollbar.config( command = self.canvas.yview )

        self.hscrollbar=Scrollbar(self.graphframe,orient=HORIZONTAL)
        #self.hscrollbar.pack(side=BOTTOM,fill=X)
        self.hscrollbar.config( command = self.canvas.xview )
        self.canvas.config(yscrollcommand=self.vscrollbar.set,xscrollcommand=self.hscrollbar.set)
        self.canvas.pack(fill=BOTH,expand=True)


        
        global undotool,redotool

        
        new=PhotoImage(file="new.gif",width=32,height=28)
        newtool=Button(self.toolframe,height=24,width=23,bd=0,image=new,bg="white",command=self.NEW,relief=FLAT)
        newtool.new=new
        newtool.place(x=4,y=5)

        b.bind_widget(newtool,statusmsg="Start a New Project")
        
        
        grid=PhotoImage(file="grid.gif",width=28,height=28)
        self.gridtool=Button(self.toolframe,height=23,width=23,bd=2,image=grid,bg="white",relief=SUNKEN,command=self.grid)
        self.gridtool.grid=grid
        self.gridtool.place(x=3,y=110)

        b.bind_widget(self.gridtool,statusmsg='Grid On/Off')

        play=PhotoImage(file="play.gif",width=35,height=35)
        playtool=Button(self.toolframe,height=30,width=30,bd=0,image=play,bg="white",relief=SUNKEN,command=self.dist_entry)
        playtool.play=play
        playtool.place(x=0,y=145)

        b.bind_widget(playtool,statusmsg='Run Algorithm  ,  [(Optional) Enter source and destination to check distance and path between any two vertices ]')


        undoo=PhotoImage(file="undo.gif",width=33,height=33)
        undotool=Button(self.toolframe,height=25,width=25,bd=0,image=undoo,relief=SUNKEN,command=self.undo,bg="white")
        undotool.undoo=undoo
        undotool.place(x=3,y=185)

        redo=PhotoImage(file="redo.gif",width=33,height=33)
        redotool=Button(self.toolframe,height=25,width=25,bd=0,image=redo,relief=SUNKEN,command='',bg="white")
        redotool.redo=redo
        #redotool.place(x=3,y=220)

        reset=tkinter.PhotoImage(file="reset.gif",width=35,height=35)
        resettool=tkinter.Button(self.toolframe,height=30,width=30,bd=0,image=reset,bg="white",relief=SUNKEN,command=self.RESET)
        resettool.reset=reset
        resettool.place(x=0,y=220)

        b.bind_widget(resettool,statusmsg="Reset Current Window ")

        save=tkinter.PhotoImage(file="save.gif",width=35,height=40)
        savetool=tkinter.Button(self.toolframe,height=25,width=25,bd=0,image=save,bg="white",relief=SUNKEN,command=self.SAVE)
        savetool.save=save
        savetool.place(x=4,y=73)

        b.bind_widget(savetool,statusmsg='Save current File')

        opent=tkinter.PhotoImage(file="open.gif",width=33,height=30)
        opentool=tkinter.Button(self.toolframe,height=20,width=32,bd=0,image=opent,bg="white",relief=SUNKEN,command=self.OPEN)
        opentool.opent=opent
        opentool.place(x=0,y=40)

        b.bind_widget(opentool,statusmsg='Open an existing File')

        global movtool
        movt=tkinter.PhotoImage(file="mov.gif",width=30,height=30)
        movtool=tkinter.Button(self.toolframe,height=30,width=27,bd=2,image=movt,bg="white",relief=FLAT,command=self.movnode)
        movtool.movt=movt
        movtool.place(x=0,y=257)

        b.bind_widget(movtool,statusmsg='Displace/move any node')  


        #global frame,frame3
        frame=Frame(root,bg="grey",bd=5,relief=RAISED)
        frame.place(x=1030,y=0,height=960,width=335)
                                                        #explaination Frame
        exframe=Frame(frame,bg="white",bd=2,relief=SUNKEN).place(x=0,y=0,width=325,height=230)
        exlabel=Label(frame,bg="purple",fg="white",text="Brief Explaination").place(x=0,y=0,height=30,width=325)
        desc=" Floyd-Warshall algorithm is a graph\n analysis algorithm for finding shortest paths in a weighted graph with positive or negative edge weights (but with no\n negative cycles) and also for finding\n transitive closure of a relation R\n\n A single execution of the algorithm\n will find the lengths (summed weights)  of the shortest paths between all pairs of vertices, though it does not return  details of the paths themselves."
        brief=Text(frame,relief=SUNKEN,bg="white",fg="black")
        brief.place(x=0,y=30,height=200,width=324)
        brief.insert(INSERT,desc)
        brief.config(state=DISABLED)
        
                                                        #frame 1
        frame1=Frame(frame,bg="white",bd=2,relief=SUNKEN)
        frame1.place(x=0,y=230,height=150,width=325)
        label1=Label(frame1,text="Graph Construction",relief=RAISED,bg="purple",fg="white")
        label1.place(x=0,y=0,width=325,height=30)
                                                        #Nodes
        label_node=Label(frame1,text="Nodes ",relief=RAISED,bg="grey",fg="black",bd=2)
        label_node.place(x=0,y=30,width=325,height=20)

        global set_nodes,del_nodes,clear_nodes
        set_nodes=Button(frame1,text="Set",command=self.nodeset,fg="Black",bd=2,relief=RAISED,bg="white")
        set_nodes.place(x=20,y=57,height=25,width=50)

        b.bind_widget(set_nodes, balloonmsg='Set Nodes',statusmsg='Start  Setting Nodes of the Graph')

        del_nodes=Button(frame1,text="Del",command=self.delnodes,fg="Black",bd=2,relief=RAISED,bg="white")
        del_nodes.place(x=140,y=57,height=25,width=50)

        b.bind_widget(del_nodes, balloonmsg='Delete previous Node ',statusmsg='Delete Last Node from the Graph')
        

        clear_nodes=Button(frame1,text="Clear All",command=self.clearnodes,fg="Black",bd=2,relief=RAISED,bg="white")
        clear_nodes.place(x=250,y=57,height=25,width=55)

        b.bind_widget(clear_nodes, balloonmsg='Delete all Nodes',statusmsg='Delete all Nodes from the Graph')
                                                        #Edges
        label_edge=Label(frame1,text="Edges ",relief=RAISED,bg="grey",fg="black",bd=2)
        label_edge.place(x=0,y=88,width=325,height=20)

        global set_edge,clear_edge,del_edge,event
        set_edge=Button(frame1,text="Set",fg="Black",bd=2,relief=RAISED,command=self.edgeset,bg="white")
        set_edge.place(x=20,y=113,height=25,width=50)

        b.bind_widget(set_edge, balloonmsg='Set Edges',statusmsg='Start  Setting  Edges of the Graph')


        del_edge=Button(frame1,text="Del",command=self.deledge,fg="Black",bd=2,relief=RAISED,bg="white")
        del_edge.place(x=140,y=113,height=25,width=50)

        b.bind_widget(del_edge, balloonmsg='Delete previous Edge',statusmsg='Delete  Last Edge from the Graph')


        clear_edge=Button(frame1,text="Clear All",command=self.clearedges,fg="Black",bd=2,relief=RAISED,bg="white")
        clear_edge.place(x=250,y=113,height=25,width=55)

        b.bind_widget(clear_edge, balloonmsg='Delete all Edges',statusmsg='Delete all Edges from the Graph')


                                                       #frame 2
        global frame2,sol_switch,run
        frame2=Frame(frame,bg="white",bd=2,relief=SUNKEN)
        frame2.place(x=0,y=380,width=325,height=290)
        label2=Label(frame2,relief=RAISED,text="Check Algorithm Results",bg="purple",fg="white")
        label2.place(x=0,y=0,width=325,height=30)

        run=Button(frame2,bd=2,fg="Black",relief=RAISED,text="Run Algorithm",bg="white",command=self.dist_entry)
        run.place(x=40,y=79,width=100,height=25)

        sol_switch=Button(frame2,bd=2,fg="Black",text="Detailed Solution",bg="white",command=self.show_sol,state=DISABLED,relief=FLAT)
        sol_switch.place(x=190,y=79,width=100,height=25)

        b.bind_widget(run, balloonmsg='Proceed to Algorithm ',statusmsg='Run Algorithm  ,  [(Optional) Enter source and destination to check distance and path between any two vertices ]')

        b.bind_widget(sol_switch,balloonmsg='Open In-Depth Solution',statusmsg='Opens a Text file containing Step-wise Floyd Warshall Solution for the current graph') 

        label_entry=Label(frame2,text="RUN",relief=RAISED,bg="grey",fg="black").place(x=0,y=30,width=325,height=20)



        label_check=Label(frame2,text="Shortest Path",relief=RAISED,bg="grey",fg="black")
        label_check.place(x=0,y=105,width=325,height=20)

        self.src=StringVar()
        self.des=StringVar()
        label_src=Label(frame2,text="    Source Node                             Destination Node",fg="black",anchor=W,bd=2,relief=RAISED).place(x=0,y=50,width=325,height=25)
        Entry(frame2,bd=3,textvariable=self.src).place(x=100,y=50,height=23,width=40)

        Entry(frame2,bd=3,textvariable=self.des).place(x=280,y=50,height=23,width=40)

                

                                                        #frame 3
        frame3=Frame(frame,bg="white",bd=2,relief=SUNKEN)
        frame3.place(x=0,y=610,width=325,height=103)
        label3=Label(frame3,text=" Options ",relief=RAISED,bg="purple",fg="white")
        label3.place(x=0,y=0,width=325,height=30)

        help_button=Button(frame3,text="Help",fg="Black",relief=RAISED,bg="white",command=self.help)
        help_button.place(x=20,y=35,width=50,height=30)
        b.bind_widget(help_button,statusmsg='Need Help ? Click Me !!')

        reset_button=Button(frame3,text="Reset",fg="Black",relief=RAISED,bg="white",command=self.RESET)
        reset_button.place(x=135,y=35,width=50,height=30)
        b.bind_widget(reset_button,statusmsg='Reset Current Window')

        about_button=Button(frame3,text="About Algo",fg="Black",relief=RAISED,bg="white",command=self.openalgo)
        about_button.place(x=240,y=35,width=70,height=30)
        b.bind_widget(about_button,statusmsg='Know more about Floyd-Warshall Algorithm')

        

        self.startx=None
        self.starty=None

        self.msg=StringVar()
        self.trace=Message(self.statusbar,textvariable=self.msg,anchor=W,bg="white",bd=0,relief=SUNKEN)

        self.canvas.bind('<Motion>',self.track)
        self.canvas.bind('<Leave>',self.track1)
        self.trace.pack(side=RIGHT)
        root.protocol("WM_DELETE_WINDOW", self.EXIT)

        self.initials()

        for x in range(30,1000,30):
                m,n=self.canvas.create_line(x,0,x,650,fill="gray"),self.canvas.create_line(0,x,1000,x,fill="gray")
                self.gridlines.append(m)
                self.gridlines.append(n)
                #self.canvas.tag_lower(n)
                #self.canvas.tag_lower(m)

    def settitle(self):
        if(self.tt==None):
            root.title("*Floyd Warshall Algorithm - Untitled.alg")
        else:
            root.title('*'+(str)(self.tt))


    def grid(self):
        if(self.gr==0):
            self.gridtool.configure(relief=SUNKEN)
            self.gr=1
            for x in range(len(self.gridlines)):
                y=self.gridlines[x]
                self.canvas.itemconfig(y,fill="grey")
            
            
        elif(self.gr==1):
            self.gr=0
            self.gridtool.configure(relief=FLAT)
            for x in range(len(self.gridlines)):
                y=self.gridlines[x]
                self.canvas.itemconfig(y,fill="white")
            


    def binds(self):
        self.canvas.bind_all('<F5>',self.dist_entry)
        self.canvas.bind_all('<Control-o>',self.OPEN)
        self.canvas.bind_all('<Control-O>',self.OPEN)
        self.canvas.bind_all('<Control-S>',self.SAVE)
        self.canvas.bind_all('<Control-s>',self.SAVE)
        self.canvas.bind_all('<Control-N>',self.NEW)
        self.canvas.bind_all('<Control-n>',self.NEW)
        self.canvas.bind_all('<Control-Shift-S>',self.SAVEON)
        self.canvas.bind_all('<Control-Shift-s>',self.SAVEON)
        #self.canvas.bind_all('<control

                                         #END of MAIN WINDOW DESIGN



                                                         #Functions


    def track(self,event):
        self.trace.configure(width=100,bd=3)
        self.msg.set("X : %s Y : %s "%(event.x,event.y))

    def track1(self,event):
        self.msg.set(" ")
        self.trace.configure(width=0,bd=0)


    def initials(self):
        self.undocheck=[]
        self.gridlines=[]
        self.settitle()
        self.binds()
        self.gr=1
        self.one=0
        self.edge_no=0
        self.flag2=0
        self.putback=0
        self.kcopy=0
        self.flag=0
        self.Nflag=0
        self.Eflag=0
        self.cnt=0
        self.edge_counter=0
        self.node_counter=0
        self.edge_nodes=[0]*10000
        self.mat_node=[[0 for x in range(1000)]for y in range(1000)]
        self.linedel=[]
        self.nodes=[]
        self.nodes_pos=[]
        self.count_entries=[]
        self.dis=[]
        self.edge=[]
        self.edges=[]
        self.edge_pos=[]
        self.undo_on=0
        self.redo_on=0
        self.mat_update=[0]*10000
        self.node_placing=[]
        self.ent_val=[]
        self.c=0
        self.k=0
        self.filename1=None
        self.checker=0
        self.coloredge=[]
        self.file_opt = options = {}
        options['defaultextension'] = '.alg'
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'myfile.txt'
        options['parent'] = root
        options['title'] = 'This is a title'
        self.checker1=0
        self.drawcheck=0
        self.undo_redo()
        self.saveas=0
        self.snodenum=-1
        self.Mflag=0

    def addnode(self,event):
        g=0
        pos=(event.x,event.y)
        for i in range(len(self.nodes_pos)):
            check=self.nodes_pos[i]   
            if(abs((pos[0]-check[0])**2-(pos[1]-check[1])**2)<1350):
                g=1
                break
        if(not g and self.Nflag==1 and pos[0]>10 and pos[1]>10 and pos[0]<958 and pos[1]<615):
            pos=(event.x,event.y)
            self.nodes_pos.append(pos)
            x=self.canvas.create_oval(pos[0]-15,pos[1]-15,pos[0]+15,pos[1]+15,fill="violet red",outline="grey",width=2)
            self.canvas.tag_raise(x)
            self.nodes.append(x)
            y=self.canvas.create_text(pos[0],pos[1],text=len(self.nodes),fill="black",activefill="green",font=8)
            self.node_placing.append(y)       
            self.node_counter=self.node_counter+1
            self.undocheck.append('N')
            self.undo_redo()
            if(self.tt!=None):
                self.tt=self.tt
                root.title('*'+self.tt)            


         
    
    def nodeset(self):
        self.canvas.configure(cursor="plus")
        self.Nflag=1
        self.Eflag=0
        self.Mflag=0

        if(self.Nflag==1):
            self.canvas.configure(cursor="plus")
        elif(self.Eflag==1):
            self.canvas.configure(cursor="arrow")
        elif(self.Mflag==1):
            self.canvas.configure(cursor="hand2")

        movtool.configure(relief=FLAT)
        set_edge.configure(bg="white")
        set_nodes.configure(bg="green")
        sol_switch.configure(state=DISABLED,bg="white",fg="black")

        self.canvas.bind('<1>',self.addnode)
        try:
            self.path_text.place_forget()
        except:
            pass

    
    def drawedge(self,event):
        self.drawcheck=1
        if(self.startx!=None and self.Eflag==1 and self.checker==1):
            pos=(event.x,event.y)
            self.canvas.coords(self.k,(self.startx,self.starty,pos[0],pos[1]))
            self.checker1=1
        

    def checkedge(self,event):
        self.drawcheck=0
        self.checker=0
        pos=(event.x,event.y)
        for i in range(len(self.nodes_pos)):
            check=self.nodes_pos[i]
            
            if(abs((pos[0]-check[0])**2-(pos[1]-check[1])**2)<50):
                self.startx=pos[0]
                self.starty=pos[1]
                self.k=self.canvas.create_line(0,0,0,0,fill="coral",width=2)
                self.canvas.tag_lower(self.k)
                self.checker=1
                break                        
                
            
    def onrelease(self,event):
        
        
        if(self.Eflag==1 and self.drawcheck==1):
            self.flag=0
            p=0
            g=0
            pos=(event.x,event.y)

            for i in range(len(self.nodes_pos)):
                check=self.nodes_pos[i]
            
                if(int(abs((pos[0]-check[0])**2-(pos[1]-check[1])**2))<50 and self.checker1==1):
                    self.flag=1
                    break

            if(self.flag==0 and self.checker==1 and self.checker1==1):
                self.canvas.coords(self.k,(0,0,0,0))
                self.checker1=0
              

            if(self.flag==1 and self.checker1==1):
                for x in range(len(self.nodes_pos)):
                    check=self.nodes_pos[x]
            
                    if(abs((self.startx-check[0])**2-(self.starty-check[1])**2)<50):
                        p=1
                        break
                if(self.mat_node[x+1][i+1]>0 and self.checker==1 and self.checker1==1):
                    self.canvas.coords(self.k,(0,0,0,0))
                    self.checker1=0
                    if(x==i):
                        messagebox.showwarning(message="Can't create edge on same node",title="Caution")
                    else:
                        messagebox.showwarning(message="Multiple edges not possible",title="Caution")
                    g=1
            
                elif(self.mat_node[x+1][i+1]==0 and x==i):
                    messagebox.showwarning(message="Can't create edge on same node",title="Caution")
                
                elif(g==0 and p==1 and self.checker1==1 and self.checker1==1):
                    #print(self.edge_counter)
                    self.edge_counter=self.edge_counter+1
                    z=self.edge_counter
                    #print(z,x,i)
                    self.mat_node[x+1][i+1]=self.mat_node[i+1][x+1]=z
                    self.edge_nodes[z*2]=i+1
                    self.edge_nodes[z*2-1]=x+1
                    self.edge.append(z)
                        #print(self.k)
                    self.edge_pos.append(self.k)
                        #print(self.edge_pos[0])
                    self.dist=StringVar()
                    self.dis.append(self.dist)
                    #print(len(self.dis),self.cnt)
                    e=Entry(self.canvas,width=3,textvariable=self.dis[self.cnt],bg="tomato")
                    e.place(x=(self.startx+event.x)/2,y=(self.starty+event.y)/2)
                    self.ent_val.append(e)
                    self.count_entries.append(e)
                    self.cnt=self.cnt+1
                    self.edges.append(pos)
                    self.undocheck.append('E')
                    if(self.tt!=None):
                        self.tt=self.tt
                        root.title('*'+self.tt)
                                                
            

    def edgeset(self):

        sol_switch.configure(state=DISABLED,bg="white",fg="black")
        try:
            self.path_text.place_forget()
        except:
            pass
        movtool.configure(relief=FLAT)
        self.Eflag=1
        self.Nflag=0
        self.Mflag=0
        
        if(self.Nflag==1):
            self.canvas.configure(cursor="plus")
        elif(self.Eflag==1):
            self.canvas.configure(cursor="arrow")
        elif(self.Mflag==1):
            self.canvas.configure(cursor="hand2")
            
        set_nodes.configure(bg="white")
        set_edge.configure(bg="green")
        self.canvas.bind('<Button-1>',self.checkedge)
        self.canvas.bind('<B1-Motion>',self.drawedge)
        self.canvas.bind('<ButtonRelease-1>',self.onrelease)

    def checknode(self,event):
        pos=(event.x,event.y)
        for i in range(len(self.nodes_pos)):
            check=self.nodes_pos[i]
            
            if(abs((pos[0]-check[0])**2-(pos[1]-check[1])**2)<50):
                self.snodenum=i
                break
    def shiftnode(self,event):
        arr=[]
        arr1=[]
        if(self.snodenum is not -1):
            mov=self.nodes[self.snodenum]
            movtxt=self.node_placing[self.snodenum]
            x=len(self.nodes)
            for k in range(1,x+1):
                n=self.mat_node[self.snodenum+1][k]
                if(n>0):
                    arr.append(n-1)
                    arr1.append(k-1)            

            pos=(event.x,event.y)
            self.canvas.coords(mov,(pos[0]-15,pos[1]-15,pos[0]+15,pos[1]+15))
            self.canvas.coords(movtxt,(pos[0],pos[1]))
            for k in range(len(arr)):
                prevpos=self.nodes_pos[arr1[k]]
                emov=self.edge_pos[arr[k]]
                enmov=self.count_entries[arr[k]]
                self.canvas.coords(emov,(prevpos[0],prevpos[1],pos[0],pos[1]))
                enmov.place_forget()
                enmov.place(x=(prevpos[0]+pos[0])/2,y=(prevpos[1]+pos[1])/2)
                    
            
    def relnode(self,event):
        if(self.snodenum is not -1):
            pos=(event.x,event.y)
            self.nodes_pos[self.snodenum]=pos
            self.snodenum=-1      
        

    def movnode(self):
        self.canvas.configure(cursor="hand2")
        movtool.configure(relief=SUNKEN)
        set_edge.configure(bg="white")
        set_nodes.configure(bg="white")
        self.Eflag=0
        self.Nflag=0
        self.canvas.bind('<Button-1>',self.checknode)
        self.canvas.bind('<B1-Motion>',self.shiftnode)
        self.canvas.bind('<ButtonRelease-1>',self.relnode)

    def matclear(self):
        z=len(self.nodes)
        for i in range(z+1):
                for j in range(z+1):
                    self.mat_node[i][j]=0


    def del_ass_edges(self,k):
        
        edge_to_del=k
        pos=len(self.undocheck)
        dec=pos-1
        self.edge_counter=self.edge_counter-1
        x=len(self.edge_pos)
        if(x>0):
            self.count_entries[edge_to_del-1].place_forget()            
            self.canvas.coords(self.edge_pos[k-1],(0,0,0,0))
            while(1 and dec >0):
                if(self.undocheck[dec]=='E'):
                    self.undocheck.pop(dec)
                    self.count_entries[k-1]
                    break
                dec=dec-1
            


    def delnodes(self):
        sol_switch.configure(state=DISABLED,bg="white",fg="black")
        try:
            self.path_text.place_forget()
        except:
            pass

        if(self.Nflag==1):
            self.canvas.configure(cursor="plus")
        elif(self.Eflag==1):
            self.canvas.configure(cursor="arrow")
        elif(self.Mflag==1):
            self.canvas.configure(cursor="hand2")

        c=0
        node_to_del=0
        check=0
        flag=0
        update=0
        updatex=0
        updatey=0
        pos=0
        pos1=0
        
        if(len(self.nodes)==0):
            messagebox.showwarning(message='No Node to Delete',title='Caution')
        else:
            
            

            #self.Nflag=0
            #self.Eflag=0
            
            y=len(self.edge)
            x=len(self.nodes_pos)

                        
            node_to_del=x
            for k in range(1,x+1):
                check=self.mat_node[node_to_del][k]
                if(check>0):
                    self.mat_update[check]=1       

            for k in range(1,y+1):
                if(self.mat_update[k]>0):
                    flag=1
                    self.mat_update[k]=0
                    self.del_ass_edges(k)
                    for m in range(1,x+1):
                        for n in range(1,x+1):
                            if(flag==1):
                                if(self.mat_node[m][n]>0 and self.mat_node[m][n]==k):
                                    self.mat_node[m][n]=0
                                    
                else:
                    update=update+1
                    if(flag==1):
                        self.count_entries[update-1]=self.count_entries[k-1]
                        self.edge_pos[update-1]=self.edge_pos[k-1]
                        
                        for m in range(1,x+1):
                            for n in range(1,x+1):
                                if(self.mat_node[m][n]==k):
                                    self.mat_node[m][n]=update
                                    self.edge_nodes[update*2-1]=m
                                    self.edge_nodes[update*2]=n
                                  
                                    
            while(self.edge_counter<y):
                self.edge.pop()
                self.edge_pos.pop()
                y=y-1
                self.count_entries.pop()
                self.cnt=self.cnt-1
                self.dis.pop()


            l1=len(self.node_placing)
            l=len(self.nodes_pos)

            dec=len(self.undocheck)-1
            while(1 and dec > 0):
                if(self.undocheck[dec]=='N'):
                    self.undocheck.pop(dec)
                    break
                dec=dec-1           
            if(l>0):
                self.canvas.delete(self.node_placing[l1-1])
                self.node_placing=self.node_placing[:-1]
                self.canvas.delete(self.nodes[l-1])
                self.nodes.pop()
                self.nodes_pos.pop()
                x=x-1
            if(self.tt!=None):
                root.title('*'+self.tt)
                
            if(x==0):
                self.undo_redo()
                

    def clearnodes(self):
        try:
            self.path_text.place_forget()
        except:
            pass
        if(len(self.nodes)==0):
            messagebox.showwarning(message='No Node to Clear',title='Caution')
        elif len(self.node_placing)>0:
            if (messagebox.askyesno(message='Are you sure you want to Clear all the Nodes?' ,icon='question' ,title='Verify')):
                App()


    def deledge(self):
        sol_switch.configure(state=DISABLED,bg="white",fg="black")

        try:
            self.path_text.place_forget()
        except:
            pass

        if(self.Nflag==1):
            self.canvas.configure(cursor="plus")
        elif(self.Eflag==1):
            self.canvas.configure(cursor="arrow")
        elif(self.Mflag==1):
            self.canvas.configure(cursor="hand2")

        #self.Eflag=0
        #self.Nflag=0

        if(len(self.edge)==0):
            messagebox.showwarning(message='No Edge to Delete',title='Caution')
        else:
            z=self.edge_counter
            
            
            if(z>0):
                self.kcopy=self.edge_pos[len(self.edge_pos)-1]
                self.canvas.coords(self.kcopy,(0,0,0,0))
                self.edge_counter=self.edge_counter-1
        
                i=self.edge_nodes[z*2-1]
                j=self.edge_nodes[z*2]
                self.mat_node[i][j]=0
                self.mat_node[j][i]=0
                dec=len(self.undocheck)-1
                while(1 and dec >0):
                    if(self.undocheck[dec]=='E'):
                        self.undocheck.pop(dec)
                        break
                    dec=dec-1  
                       
                self.edge_pos.pop()
                self.edge.pop()
                self.dis.pop()
                k=len(self.count_entries)

                self.count_entries[k-1].place_forget()
                self.count_entries.pop()
                self.cnt=self.cnt-1
                if(self.tt!=None):
                    root.title('*'+self.tt)


                

    def clearedges(self):
        sol_switch.configure(state=DISABLED,bg="white",fg="black")

        try:
            self.path_text.place_forget()
        except:
            pass
        if(self.Nflag==1):
            self.canvas.configure(cursor="plus")
        elif(self.Eflag==1):
            self.canvas.configure(cursor="arrow")
        elif(self.Mflag==1):
            self.canvas.configure(cursor="hand2")

        #self.Eflag=0
        #self.Eflag=0
        if(len(self.edge)==0):
            messagebox.showwarning(message='No Edge to Clear',title='Caution')

        elif (messagebox.askyesno(message='Are you sure you want to Clear all the Edges?' ,icon='question' ,title='Verify')):
            z=len(self.nodes)           
            
            while(len(self.edge)>0):
                clear_edge.configure(bg="Dark green",fg="white")
                self.kcopy=self.edge_pos[len(self.edge_pos)-1]
                self.canvas.coords(self.kcopy,(0,0,0,0))
                self.edge_counter=self.edge_counter-1
                self.count_entries[len(self.count_entries)-1].place_forget()
                self.count_entries.pop()
                self.cnt=self.cnt-1
                self.dis.pop()
                self.edge.pop()
                self.edge_pos.pop()
                clear_edge.configure(bg="white",fg="black")
            dec=len(self.undocheck)-1
            while(1 and dec >0):
                if(self.undocheck[dec]=='E'):
                    self.undocheck.pop(dec)
                dec=dec-1
            
            self.matclear()
            if(self.tt!=None):
                root.title('*'+self.tt)
       

    def dist_entry(self,event=0):
        y=len(self.coloredge)
        for i in range(y-1,-1,-1):
            self.canvas.itemconfig(self.coloredge[i],fill="coral")
            self.coloredge.pop()
        
        try:
            self.path_text.place_forget()
        except:
            pass
        x=len(self.nodes)
        if(x==0):
            messagebox.showwarning(message="Please Draw a Graph before Run",title="Caution")
            return
        if(x==1):
            messagebox.showwarning(message="Only single node is present in the Graph.Can't proceed further",title="Caution")
            return
        else:
            if(self.tt!=None):
                root.title('*'+self.tt)
            self.mat_graph=[[0 for i in range(x)]for j in range(x)]
            flag=0
        
            for i in range(1,x+1):
                for j in range(1,x+1):
                    if(self.mat_node[i][j]!=0 and i!=j):
                        entry=self.mat_node[i][j]                 
                        en=self.dis[entry-1]
                        inp=en.get()
                        try:
                            val=int(inp)
                            
                        except ValueError:
                            messagebox.showwarning(message="One or more Invalid Distance Entries",title="Caution")
                            for m in range(x):
                                for n in range(x):
                                    self.mat_graph[m][n]=0
                            flag=1
                            break
                            
                        self.mat_graph[i-1][j-1]=val
                        self.mat_graph[j-1][i-1]=val
                    if(i!=j and self.mat_node[i][j]==0):
                        self.mat_graph[i-1][j-1]=self.mat_graph[j-1][i-1]=INF
                if(flag==1):
                    break
            if(flag==0):
                self.floyd_warshall()

    def floyd_warshall(self):
        global frame2
        changes=[]
        ind=0
        x=len(self.nodes)
        x1=x
        w=0
        self.trace_path=[]
        self.warshall_sol=[[0 for i in range(x)]for j in range(x)]
        self.pie=[[0 for i in range(x)]for j in range(x)]
        self.path=[[NIL for i in range(x)]for j in range(x)]
        flag=0
        new_destiny=0
        chF=0

        self.sol_file=open("solution.txt","w")
        head="\t\t\t\t\t\tFloyd Warshall Solution for the Current Graph \n\n"
        self.sol_file.write(head)
        put="  The Input Graph (in matrix form ) is :\n \n \t "
        self.sol_file.write(put)
        for r in range(x):
            for s in range(x):
                if(self.mat_graph[r][s]==INF or r==s):
                    self.next_mat=NIL
                if(self.mat_graph[r][s]==INF):
                    self.sol_file.write("INF")
                else:
                    self.sol_file.write(str(self.mat_graph[r][s]))
                self.sol_file.write(" ")
            self.sol_file.write("\n \n \t ")

        put="\n \n Applying Floyd Warshall Algorithm : \n \n \t \n"
        self.sol_file.write(put)
        self.sol_file.write(" STEP %s : \n \t W(%s)  =   "%(str(w+1),str(w)))

        x2=1
        f=0
        for i in range(x):
            for j in range(x):
                self.warshall_sol[i][j]=self.mat_graph[i][j]
                self.path[i][j]=j
                if(self.mat_graph[i][j]==INF):
                    self.sol_file.write("INF")
                else:
                    self.sol_file.write(str(self.mat_graph[i][j]))
                self.sol_file.write(" ")
            if(x2>0):
                while(x1>0):
                    self.sol_file.write("     ")
                    x1=x1-1
                x1=x
                self.sol_file.write("Pi(%s) = "%(str(w)))
                x2=0
                f=1
                
            while(x1>0 and f==0):
                self.sol_file.write("       ")
                x1=x1-1
            x1=x
            f=0
            for k in range(x):
                if(self.mat_graph[i][k]==INF or i==k):
                    self.pie[i][k]=NIL
                    self.sol_file.write("NIL")
                if(self.mat_graph[i][k]<INF and i!=k):
                    self.pie[i][k]=i
                    self.sol_file.write(str(i))
                self.sol_file.write(" ")
            
                    
            self.sol_file.write("\n \n \t \t   ")
        w=w+1               
        x1=x
        x2=1
        f=0
        for k in range(x):
            self.sol_file.write("\n \n STEP %s : \n \t W(%s)  =   "%(str(w+1),str(w)))
            x2=1
            for i in range(x):
                for j in range(x):
                    if(self.warshall_sol[i][k]+self.warshall_sol[k][j]<self.warshall_sol[i][j]):
                        changes.append(i)
                        changes.append(j)
                        if(self.warshall_sol[i][j]==INF):
                            changes.append("INF")
                        else:
                            changes.append(self.warshall_sol[i][j])
                        self.warshall_sol[i][j]=self.warshall_sol[i][k]+self.warshall_sol[k][j]
                        changes.append(self.warshall_sol[i][j])
                        self.path[i][j]=self.path[i][k]
                        
                    if(self.warshall_sol[i][j]==INF):
                        self.sol_file.write("INF")
                    else:
                        self.sol_file.write(str(self.warshall_sol[i][j]))
                    self.sol_file.write(" ")
                if(x2>0):
                    while(x1>0):
                        self.sol_file.write("     ")
                        x1=x1-1
                    x1=x
                    self.sol_file.write("Pi(%s) = "%(str(w)))
                    x2=0
                    f=1
                while(x1>0 and f==0):
                    self.sol_file.write("       ")
                    x1=x1-1
                x1=x
                f=0
                for p in range(x):
                    if(self.warshall_sol[i][p]>self.warshall_sol[i][k]+self.warshall_sol[k][p]):
                        self.pie[i][p]=self.pie[k][p]
                    if(self.pie[i][p]==NIL):
                        self.sol_file.write("NIL")
                    else:
                        self.sol_file.write(str(self.pie[i][p]))
                    self.sol_file.write(" ")
                self.sol_file.write("\n \n \t \t   ")
                        
            self.sol_file.write("\n \n \t \t   ")
            w=w+1
            if(w>1):
                if(len(changes)>0 and w-1<len(self.nodes)):
                    self.sol_file.write("\n Changes occured from  W(%s) to W(%s)  : "%(str(w-2),str(w-1)))
                    while(ind<len(changes)):
                        self.sol_file.write("\n i = %s   j = %s   Replace = %s --> %s \n"%(str(changes[ind]),str(changes[ind+1]),str(changes[ind+2]),str(changes[ind+3])))
                        ind=ind+4
                else:
                    self.sol_file.write("\n No change occured from W(%s) to W(%s) \n"%(str(w-2),str(w-1)))
                
        try:
            val=self.src
            s=val.get()
            source=int(s)
            val=self.des
            d=val.get()
            destiny=int(d)
            new_destiny=destiny
            if(source<1 or source>x or destiny<1 or destiny>x):
                messagebox.showwarning(message="Source/Destination is out of range",title="Caution")
                flag=1
        except ValueError:
            #messagebox.showwarning(message="Source/Destination is Invalid",title="Caution")
            flag=1
            
        

        
                            
        global frame2
        if(flag==0):
            dis=self.warshall_sol[source-1][destiny-1]
            cal_dis=StringVar()
            if(dis==INF):
                cal_dis.set("  INFINITY ")
            else:
                cal_dis.set(" %s "%(dis))
            
            
            Label(frame2,text="  Shortest Path Distance : ",bd=2,relief=RAISED,anchor=W).place(x=0,y=124,width=325,height=25)
            self.calc_dis=Label(frame2,textvariable=cal_dis,bd=3,relief=SUNKEN,bg="white",anchor=W).place(x=150,y=124,width=170,height=23)
            txt_frame=Frame(frame2,relief=SUNKEN,bg="white",bd=2)
            txt_frame.place(x=0,y=149,height=80,width=325)
            scr=Scrollbar(txt_frame)
            self.path_text=Text(txt_frame,bg="cyan",yscrollcommand=scr.set)
            self.path_text.pack(side=LEFT,fill="both",expand=True)
            scr.config(command=self.path_text.yview)
            scr.pack(side=RIGHT,fill=Y,expand=False)
            if(dis!=INF):
                self.output_path(source-1,destiny-1)
                file=open("tmp.txt","w")
                file.write(" Shortest Path is:\n  ")
                self.sol_file.write("\n   Shortest Distance from Node %s to Node %s  :  %s   \n"%(str(source),str(destiny),str(dis)))
                self.sol_file.write("\n   Shortest Path is from Node %s to Node %s :   "%(str(source),str(destiny)))
                for i in range(len(self.trace_path)):
                    file.write(str(self.trace_path[i]))
                    self.sol_file.write(str(self.trace_path[i]))
                    if(i!=len(self.trace_path)-1):
                        file.write(" --> ")
                        self.sol_file.write(" --> ")
                file.close()
                file=open("tmp.txt","r")
                text=file.read()
                self.path_text.insert(END,text)
                self.path_text.config(state=DISABLED)
                file.close()
                if(len(self.edge)>0):
                    if(source<destiny):
                        self.color_path(source,destiny)
                    elif(source>destiny):
                        self.color_path(destiny,source)
                                    
            if(dis==INF):
                self.path_text.insert(END,"No Path Exists")
                self.path_text.config(state=DISABLED)
                self.sol_file.write("\n   Shortest Distance from Node %s to Node %s  :  %s   \n"%(str(source),str(destiny),str(dis)))
                self.sol_file.write("\n Thus No Path Exists  \n\n")
                self.sol_file.close()

        self.sol_file.close()
        sol_switch.configure(state=NORMAL,bg="green",fg="black",relief=RAISED)
        
                

            
    def print_sol(self):
        flag=0
        x=len(self.nodes)

        for i in range(x):
            for j in range(x):
                if(self.warshall_sol[i][j]==INF):
                    print(" INF ",sep=' ',end=' ')
                else:
                    print(self.warshall_sol[i][j],sep=' ',end=' ')
            print('\n')

        
            
    def output_path(self,i,j):
        if(self.path[i][j]==NIL):
            return
        self.trace_path.append(i+1)
        while(i!=j):
            i=self.path[i][j]
            self.trace_path.append(i+1)
        return self.trace_path
            

    def color_path(self,source,destiny):
        y=len(self.trace_path)
        z=len(self.edge_pos)
        for i in range(y-1):
            x=self.mat_node[self.trace_path[i]][self.trace_path[i+1]]
            self.coloredge.append(self.edge_pos[x-1])
            self.canvas.itemconfig(self.edge_pos[x-1],fill="green")
        
    def show_sol(self):
        self.new_win=Tk()
        self.new_win.geometry("600x600")
        self.new_win.title("Detailed Solution")
        self.new_win.resizable(1,0)
        frame=Frame(self.new_win,height=545,width=105,bd=4,relief=SUNKEN)
        frame.place(y=7)
        frame.pack(fill=X,expand=True)
        frame.pack_propagate(0)
        Button(self.new_win,text="Close",command=self.new_win.destroy).place(x=280,y=572)
        Button(self.new_win,text="Save As..",command=self.save).place(x=100,y=572)
        t=Text(frame,bg="white",wrap=NONE)
        vscrollbar=Scrollbar(frame)
        vscrollbar.pack(side=RIGHT,fill=Y)
        vscrollbar.config( command = t.yview )

        hscrollbar=Scrollbar(frame,orient=HORIZONTAL)
        hscrollbar.pack(side=BOTTOM,fill=X)
        hscrollbar.config( command = t.xview )
        t.config(yscrollcommand=vscrollbar.set,xscrollcommand=hscrollbar.set)
        t.pack(fill=BOTH,expand=True)
        fin=open("solution.txt","r")
        
        txt=fin.read()
        t.insert(END,txt)
        t.config(state=DISABLED)


    def help(self):
        self.win2=Tk()
        self.win2.title("Help")
        self.win2.geometry("600x560")
        self.win2.resizable(0,0)
        self.win2.attributes("-toolwindow",1)
        Label(self.win2,text="Setting Nodes",bg="white").place(x=20,y=5)
        node="For making nodes in the graph,first click on 'Set' under Nodes in the 'Graph Construction' Tab.\
\n\n    ** Then click anywhere in the graph to set Nodes.\
\n    ** Del button delete the latest added node in the graph.\
\n    ** Clear All button removes all the nodes and their associated           edges from the graph and makes graph empty."
        t=Text(self.win2,bg="white",width=70,height=8)
        t.pack(pady=35)
        t.insert(END,node)
        t.config(state=DISABLED)
        edge="For making edges in the graph,first click on 'Set' under Edges in the 'Graph Construction' Tab.\
\n\n    ** Then click on the first Nodes and drag it to  another node to         create an edge between two nodes.\
\n    ** Del button delete the latest added edge in the graph.\
\n    ** Clear All button removes all the edges from the graph."
        Label(self.win2,text="Setting Edges",bg="white").place(x=20,y=175)
        t1=Text(self.win2,bg="white",width=70,height=8)
        t1.pack(pady=5)
        t1.insert(END,edge)
        t1.config(state=DISABLED)
        run="'Run Algorithm' Button runs the algorithm and shows the result.\
\n______________________________(OPTIONAL)______________________________\
\n    ** To check path and Distance between Two nodes provide source           node and desination node in the respective entry box."
        Label(self.win2,text="Run Algorithm",bg="white").place(x=20,y=345)
        t1=Text(self.win2,bg="white",width=70,height=4)
        t1.pack(pady=27)
        t1.insert(END,run)
        t1.config(state=DISABLED)
        chk="'Check solution' button gives the detailed solution of the graph that   can be saved in a file."
        Label(self.win2,text="Check Solution",bg="white").place(x=20,y=445)
        t1=Text(self.win2,bg="white",width=70,height=4)
        t1.pack(pady=5)
        t1.insert(END,chk)
        t1.config(state=DISABLED)


                                        #utility functions



    def undo_redo(self):
        if(len(self.undocheck)<=1):
            undotool.configure(state=DISABLED)
            self.undo_on=0
        else:
            undotool.configure(state=NORMAL)



    def undo(self):
        
        dec=len(self.undocheck)-1
        if(dec >=0):
            if(self.undocheck[dec]=='E'):
                self.deledge()
            elif(self.undocheck[dec]=='N'):
                self.delnodes()
        else:
            self.undo_redo()

    def save(self):
        filename=StringVar()
        if filename.set (filedialog.asksaveasfilename(defaultextension = ".txt", filetypes=[("Text File", ".txt")])):
            s=filename.get()
            fin=open("solution.txt","r")
        
            txt=fin.read()
            fout=open(s,"w")
            fout.write(txt)

    

    def askopenfile(self):
        return filedialog.askopenfile(mode="r",**self.file_opt)

    def openalgo(self):
        from os import startfile
        startfile("about.txt")      
        
    def exitfun(self):
        self.exit()

    def NEW(self,event=0):
        
        if len(self.nodes)==0:
            App()
        else:
            s=messagebox.askyesnocancel(message='Do you want to save your current work?' ,icon='question' ,title='New..')
            if s==None:
                pass
            elif s==False:
                App()
            elif s==True:
                self.SAVE()
                App()

    def SAVEON(self,event=0):
        self.saveas=1
        self.SAVE()

    def SAVE(self,event=0):
        if len(self.nodes)==0:
            messagebox.showinfo("Warning","The Graph is empty. First draw a graph ,then save the file.")
        else:
            self.save2()

    def save2(self):
        
        if self.one==1:
            self.s=self.filename
        else:
            if(self.filename1==None or self.saveas==1):
                self.saveas=0
                self.filename1=StringVar()
                self.filename1.set("NULL")
                self.filename1.set(filedialog.asksaveasfilename(defaultextension = ".alg", filetypes=[("Algorithm Files", ".alg")]))
                self.s=self.filename1.get()
                self.tt="Floyd Warshall Algorithm : "+ self.s
            root.title(self.tt)


        '''
        filename=StringVar()
        if filename.set (filedialog.asksaveasfilename(defaultextension = ".txt", filetypes=[("Text File", ".txt")])):
            s=filename.get()
            '''
        '''
        try:
            fout=open(s,"wb")
            endl='\n'
            mul=[]
            for i in range(len(self.nodes)):
                x=list(self.nodes[i])
                a=int(x[0]/127)
                mul.append(a)
                x[0]=x[0]%127
                b=int(x[1]/127)
                mul.append(b)
                x[1]=x[1]%127
            
                fout.write(struct.pack('2b',*x))
        
            fout.write(endl.encode('ascii'))
            p=str(len(mul))+'b'
            fout.write(struct.pack(p,*mul))
        
            fout.write(endl.encode('ascii'))
            mul=[]
            for i in range(len(self.edge_pos)):
                x=list(self.edge_pos[i])
            
                fout.write(struct.pack('2b',*x))
        
             
            fout.write(endl.encode('ascii'))
            val=[]
            
            for i in range(len(self.edges)):
                y=self.dis[i]
                input=y.get()
                if(len(input)==0):
                    val.append(0)
                else:
                    try:
                        x=int(input)
                        val.append(x)
                    except:
                        messagebox.showinfo("Warning","Unable to save file.There is some invalid distance.")
        
            l1=len(val)
            p=str(l1)+'b'
            fout.write(struct.pack(p,*val))
            
            
            fout.close()
        except:
            messagebox.showinfo("Warning","File not saved.")
        '''
        endl='\n'
        mul=[]
        xwrite=[]
        finalwrite=[]
        for i in range(len(self.nodes_pos)):
            x=list(self.nodes_pos[i])
            a=int(x[0]/127)
            mul.append(a)
            x[0]=x[0]%127
            if(x[0]==10):
                x[0]=x[0]+1
            elif(x[0]==13):
                x[0]=x[0]-1
                
            b=int(x[1]/127)
            mul.append(b)
            x[1]=x[1]%127
            if(x[1]==10):
                x[1]=x[1]+1
            elif(x[1]==13):
                x[1]=x[1]-1
            xwrite.append(x[0])
            xwrite.append(x[1])
        
        finalwrite.append(xwrite)
        p=str(len(mul))+'b'
        finalwrite.append(mul)
        mul=[]
        cnt1=0
        end=len(self.edge_pos)
        if self.edge_nodes[1]>0 and self.edge_nodes[2]>0 and end>0:
            for i in range(1,len(self.edge_pos)*2+1):
                cnt1=cnt1+1
                x=self.edge_nodes[1:end*2+1]
            for j in range(len(x)):
                if x[j]==10:
                    x[j]=126
                elif x[j]==13:
                    x[j]=125
            #print(x)
            p=str(len(x))+'b'
        finalwrite.append(x)
        val=[]
        for i in range(len(self.count_entries)):
            y=self.dis[i]
            input=y.get()
            if(len(input)==0):
                val.append(0)
            else:
                try:
                    x=int(input)
                    if(x==10):
                        val.append(-1)
                    elif(x==13):
                        val.append(253)
                    else:
                        val.append(x)
                except:
                    messagebox.showinfo("Warning","Unable to save file.There is some invalid distance.")
        l1=len(val)
        p=str(l1)+'l'
        finalwrite.append(val)
        '''for i in range(len(finalwrite)):
                x=finalwrite[i]
                for row in range(len(x)):
                    bytes = bytearray(cobs(delta_rows[row].getByte_List()))
                    fout.write(bytes)
                fout.write(endl.encode('ascii'))
                
                '''
        fout=open(self.s,'wb')
        print(len(finalwrite))
        print(finalwrite)
        
        for i in range(len(finalwrite)):
            p=str(len(finalwrite[i]))+'B'
            print(p)
            fout.write(struct.pack(p,*finalwrite[i]))
            fout.write(endl.encode('ascii'))
        p=str(len(finalwrite[3]))+'l'           
        fout.close()

    def ClearCan(self):
        if len(self.edge_pos)>0:
            for i in range(len(self.edge_pos)):
                self.canvas.delete(self.edge_pos[i])
                self.count_entries[i].place_forget()
            self.edge_pos=[]
            self.count_entries=[]
            self.dis=[]
            self.edge=[]
            self.cnt=0
            self.node_counter=0
            self.edge_counter=0
            
            self.matclear()
        l=len(self.node_placing)
            
        if l>0:
            while True:
                if l==0:
                    break
                else:
                    self.canvas.delete(self.node_placing[l-1])
                    self.node_placing=self.node_placing[:-1]
                    self.canvas.delete(self.nodes[l-1])
                    self.nodes.pop()
                    self.nodes_pos.pop()
                    self.node_counter=self.node_counter-1
                    l=l-1
        self.initials()




    def OPEN(self,event=0):
        if len(self.nodes)==0:
            self.Open2()        
        else:
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
        dia=filename.set(filedialog.askopenfilename(defaultextension = ".alg", filetypes=[("Algorithm Files", ".alg")]))
        
        self.s=filename.get()
        s=self.s

        
        if '.alg' in s:
            self.ClearCan()
            self.filename1=s
            
            self.open1(s)
            
            

            
        else:
            self.initials()
            if dia is not None:
                messagebox.showinfo("Warning","Not a supported file.")

    def open1(self,s):
        
        cnt=0
        self.filename=s
        self.tt="Floyd Warshall Algorithm : "+s
        if(self.tt!=None):
            root.title('*'+self.tt)
        fin=open(s,'rb')
        values=[]
        values=fin.read().splitlines()
        '''for l in fin:
                
                l.split()
                if l:
                    l=[int(i) for i in l]
                    cnt=cnt+1
                    #print(l)
                    if cnt==3:
                        l=l[:-2]
                    if cnt is not 4:
                        l=l[:-1]
                    print(l)
                    values.append(l)
                    '''        
        f1,f2,f3=0,0,0
        n,e,u,m,e1=0,0,[],[],[]
        try:
            n=values[0]
            m=values[1]
            f1=1
        except:
            messagebox.showinfo("Message","The file is empty.")

        try:
            if len(values[2])>0: 
                e1=values[2]   
        except:
            pass
        
        tmpn,tmpm=[],[]
        for x in range(len(n)):
            tmpn.append(n[x])
        for x in range(len(m)):
            tmpm.append(m[x])
        n,m=tmpn,tmpm
        e=[]
        #print(n,m)
        for i in range(len(e1)):
            print(e1[i])
            if(e1[i]==126):
                e.append(10)
            if(e1[i]==125):
                e.append(13)
            else:
                e.append(e1[i])
        if len(e)>0:
            f2=1
        #print(e1)
        d1=[]
        try:
            u=values[3]
            print(u)
            for i in range(len(u)):
                if u[i]==255:
                    d1.append(10)
                elif u[i]==253:
                    d1.append(13)
                else:  
                    d1.append(u[i])
            f3=1
        except:
            pass
        #print(d1)
        self.d=[]
        self.mul=[]
        k=0
        while True:
            if k==len(d1) or k >len(d1)+1:
                break
            else:
                self.d.append(d1[k]%256)
                self.mul.append(int(d1[k]/256))  
                k=k+1
        #print(self.d,self.mul)
        '''print(len(d))
        for i in range(len(d)):
            print(d[i],sep=' ',end=' ')
        print('\n')
        '''
        
        '''ind=0
        for i in range(len(d1)):
            if(d1[i]>0):
                #print("y")
                d.append(d1[i])
                ind=ind+1
                '''
        
        '''try:
            if len(values[3])>0:
                d=values[3]
                f3=1
        except:
            pass
            '''
        '''for i in range(len(d)):
            print(d[i],sep=' ',end=' ')
        print(d)
        '''
        
        flag=0
        if f1==1:
            c1=0
            '''try:
                while True:
                    if c1==len(n):
                        break
                    else:
                
                        a=((n[c1]+(m[c1]*127)),(n[c1+1]+(m[c1+1]*127)))
                
                        self.nodes_pos.append(a)
                        c1=c1+2
            
            
                
                for i in range(len(self.nodes_pos)):
                    s=self.nodes_pos[i]
                    x=self.canvas.create_oval((s[0]-15,s[1]-15,s[0]+15,s[1]+15),fill="violet red",width=2,outline="gray",tag='bubbles')
                    y=self.canvas.create_text(s[0],s[1],font=6,text=self.i+1,activefill="green",fill="white")
            
                    self.nodes.append(x)
                    
                    self.node_placing.append(y)
                    self.node_counter=self.node_counter+1
                    self.mat= [[0 for _ in range(self.i)] for _ in range(self.i)]
            
                
            
                
            except:
                messagebox.showinfo("Message","File cannot be opened.The file may be corrupted.")
                flag=1
                
                App()
                
            '''
            postore=[]
            while True:
                if c1==len(n):
                    break
                else:
                    a=((n[c1]+(m[c1]*127)),(n[c1+1]+(m[c1+1]*127)))
                    postore.append(a)
                    c1=c1+2

            for i in range(len(postore)):
                s=postore[i]
                self.undocheck.append('N')
                x=self.canvas.create_oval((s[0]-15,s[1]-15,s[0]+15,s[1]+15),fill="violet red",width=2,outline="grey")
                y=self.canvas.create_text(s[0],s[1],font=8,text=len(self.nodes)+1,activefill="green",fill="black")
                self.nodes.append(x)
                self.nodes_pos.append(s) 
                self.node_placing.append(y)
                self.node_counter=self.node_counter+1
            if f2==1 and flag==0:
                self.op2(e,s,f3)
            
                
    def op1(self,n):
        print("op1")
        

    def op2(self,edg,nf,f3):
        c2=0
        flag=0
        self.edge_nodes[0]=0
        c2=c2+1
        '''try:
            while True:
                if c2==len(e):
                    break
                else:
                    a=e[c2]
                    self.edge_nodes.append(a)
                    c2=c2+1
            for i in range(1,len(self.edge_nodes)*2+1):
                s1,s2=self.edge_nodes[i],self.edge_nodes[i+1]
                c1,c2=self.nodes[s1],self.nodes[s2]
                x=self.canvas.create_line((c1[0],c1[1],c2[0],c2[1]),fill="lawn green",width=3)
                
                self.edge_placing.append(x)
                self.str_e=StringVar()
                self.dis.append(self.str_e)
                self.cnt=self.cnt+1
                #self.flag10=0
                e=Entry(self.canvas,textvariable=self.dis[self.cnt],width=3,bg="tomato")
                tmp1,tmp2=(c1[0]+c2[0])/2,(c1[1]+c2[1])/2
                e.place(x=((c1[0]+tmp1)/2),y=((c1[1]+tmp2)/2))
                #print(c1,c2)
                self.count_entries.append(e)
                self.cnt=self.cnt+1
                #self.count=self.count+1
        except:
                messagebox.showinfo("Message","File cannot be opened.The file may be corrupted.")
                flag=1
                App()
                '''
        while True:
            if c2==len(edg)+1:
                break
            else:
                a=edg[c2-1]
                self.edge_nodes[c2]=a
                c2=c2+1

        
        q=1       
        l1=int(len(edg)/2)
        for i in range(l1):
            self.undocheck.append('E')
            self.edge_counter=self.edge_counter+1
            z=self.edge_counter
            s1,s2=self.edge_nodes[q],self.edge_nodes[q+1]
            c1,c2=self.nodes_pos[s1-1],self.nodes_pos[s2-1]
            self.mat_node[s1][s2]=self.mat_node[s2][s1]=z
            x=self.canvas.create_line((c1[0],c1[1],c2[0],c2[1]),fill="coral",width=2)
            self.canvas.tag_lower(x)
            self.edge_pos.append(x)
            self.str_e=StringVar()
            self.dis.append(self.str_e)
            self.edge.append(x)       
            e=Entry(self.canvas,textvariable=self.dis[self.cnt],width=3,bg="tomato")
            tmp1,tmp2=(c1[0]+c2[0])/2,(c1[1]+c2[1])/2
            e.place(x=tmp1,y=tmp2)    
            self.count_entries.append(e)
            self.cnt=self.cnt+1
            q=q+2

            '''self.edge_counter=self.edge_counter+1
                        z=self.edge_counter
                        #print(z,x,i)
                        self.mat_node[x+1][i+1]=self.mat_node[i+1][x+1]=z
                        self.edge_nodes[z*2]=i+1
                        self.edge_nodes[z*2-1]=x+1
                        self.edge.append(z)
                        #print(self.k)
                        self.edge_pos.append(self.k)
                        #print(self.edge_pos[0])
                        self.dist=StringVar()
                        self.dis.append(self.dist)
                        e=Entry(self.canvas,width=3,textvariable=self.dis[self.cnt],bg="tomato")
                        e.place(x=(self.startx+event.x)/2,y=(self.starty+event.y)/2)
                        self.ent_val.append(e)
                        self.count_entries.append(e)
                        self.cnt=self.cnt+1
                        self.edges.append(pos)
                        '''       
        if flag==0 and f3==1:
            self.op3(nf,edg)
        
            
                

    def op3(self,nf,edg):
        self.undo_redo()
        l1=int(len(edg)/2)
        self.cnt=0
        k=0
        for i in range(l1):
            y=(self.mul[i]*256)+(self.d[i])
            if self.d[i]==0:
                k=k+1
            else:
                self.count_entries[k].insert(END,y)
                k=k+1
            self.cnt=self.cnt+1  
           
    def arraycheck(self):
        for i in range(10):
            print(self.marked_node[i])

    def matcheck(self):
        for i in range(10):
            for j in range(10):
                print(self.mat_node[i][j])

    def RESET(self):
        if (messagebox.askyesno(message='Are you sure you want to Reset?' ,icon='question' ,title='Verify')):
            App()
    def EXIT(self):
        if (messagebox.askyesno(message='Are you sure you want to Exit?' ,icon='question' ,title='Verify')):
            root.destroy()
              
App()
root.mainloop()
 

