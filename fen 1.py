import tkinter 
import tkinter.messagebox
#creation de notre fenetre 
root = tkinter.Tk ()  
root.title("Gumii&Rajae's Tic-Tac-Toe")
root.geometry("500x500")
root.resizable(width=False,height=False)
screen_width = root.winfo_screenwidth()
screen_height =root.winfo_screenheight()
# centrer la fenetre 
x = (screen_width // 2) - (500// 2)
y = (screen_height // 2) - (500// 2)
root.geometry(f"+{x}+{y}")
root.config(background="white")
root.iconbitmap("C:/Users/user/Downloads/WhatsApp Image 2023-02-09 at 22.46.35.ico")#changer l'icone de la fenetre
#creation de la premiere page 
wlcmtxt=tkinter.Label(text="WELCOME TO OUR GAME !",font=("Verdana",20),bg="white",fg="black") 
wlcmtxt.pack(expand="YES")
#l'ajout de l'image 
img = tkinter.Canvas(root, width=400, height=200)
im = tkinter.PhotoImage(file="C:\\Users\\ThinkPad\\Desktop\\ancien\\01\\WhatsApp Image 2024-03-07 à 12.53.59_e3070d09.jpg")
im = im.subsample(3)#l'image est reduite de 1/3   
img.create_image(0, 0, anchor='nw', image=im)
img.pack(expand=True)
#creation du bouton qui nous va permet de commencer le jeux 
strt=tkinter.Button(text="LET'S START",font=("Times",15),bg="#39B5E0",fg="black", width=15, height=2,command=lambda:new(root))
strt.pack(expand=True)
#creation d'une nouvelle fenetre 
def new(root):
   root.withdraw()   
   root1 = tkinter.Toplevel()
   root1.geometry("500x500")
   root1.resizable(width=False,height=False)
   screen_width = root1.winfo_screenwidth()
   screen_height =root1.winfo_screenheight()
   x = (screen_width // 2) - (500// 2)
   y = (screen_height // 2) - (500// 2)
   root1.geometry(f"+{x}+{y}")
   root1.config(background="white")
   root1.iconbitmap("C:/Users/user/Downloads/WhatsApp Image 2023-02-09 at 22.46.35.ico")
   txt=tkinter.Label(root1,text="LET'S GO !\n Choose one of them ",font=("Verdana",15),bg="white",fg="black")
   txt.pack(expand=True)
   #creation de deux boutons pour choisir avec qui on joue 
   butweb = tkinter.Button(root1, text="Play with me", font=("Times", 15), bg="#39B5E0", fg="black",command=lambda:play_web(root1))
   butweb.pack(expand=True)
   butfr = tkinter.Button(root1, text="Play with your friend", font=("Times", 15), bg="#39B5E0", fg="black",command=lambda:play_fr(root1))
   butfr.pack(expand=True)
   txtt=tkinter.Label(root1,text="good luck 😊",font=("Serif",15),bg="white",fg="black")
   txtt.pack(expand=True)
   root1.mainloop()
#deux variables qu'on va utiliser pour les clicks  
clicked=True 
c=0  
#fonction et nouvelle fenetre responsable au jeux avec l'ami
def play_fr(root1):
    global root2 ,restart
    root1.withdraw()
    root2 = tkinter.Toplevel()
    root2.geometry("530x500")
    root2.resizable(width=False,height=False)
    screen_width = root2.winfo_screenwidth()
    screen_height =root2.winfo_screenheight()
    x = (screen_width // 2) - (530// 2)
    y = (screen_height // 2) - (500// 2)
    root2.geometry(f"+{x}+{y}")
    root2.config(background="white")
    root2.iconbitmap("C:/Users/user/Downloads/WhatsApp Image 2023-02-09 at 22.46.35.ico")
    txt=tkinter.Label(root2,text="Player 1:",bg="white",fg="black",font=("Helvetica",15))
    txt1=tkinter.Entry(root2)#le joueur 1 va entrer son non ici
    txtt=tkinter.Label(root2,text="Player 2:",bg="white",fg="black",font=("Helvetica",15))
    txtt1=tkinter.Entry(root2)#le joueur 1 va entrer son non ici
    #creation des boutons 
    bouton1=tkinter.Button(root2,text=" ",font=("Helvetica",20),height=3,width=9,bg="#39B5E0",fg="black",command=lambda:b_click(bouton1))
    bouton2=tkinter.Button(root2,text=" ",font=("Helvetica",20),height=3,width=9,bg="#39B5E0",fg="black",command=lambda:b_click(bouton2))
    bouton3=tkinter.Button(root2,text=" ",font=("Helvetica",20),height=3,width=9,bg="#39B5E0",fg="black",command=lambda:b_click(bouton3))
    bouton4=tkinter.Button(root2,text=" ",font=("Helvetica",20),height=3,width=9,bg="#39B5E0",fg="black",command=lambda:b_click(bouton4))
    bouton5=tkinter.Button(root2,text=" ",font=("Helvetica",20),height=3,width=9,bg="#39B5E0",fg="black",command=lambda:b_click(bouton5))
    bouton6=tkinter.Button(root2,text=" ",font=("Helvetica",20),height=3,width=9,bg="#39B5E0",fg="black",command=lambda:b_click(bouton6))
    bouton7=tkinter.Button(root2,text=" ",font=("Helvetica",20),height=3,width=9,bg="#39B5E0",fg="black",command=lambda:b_click(bouton7))
    bouton8=tkinter.Button(root2,text=" ",font=("Helvetica",20),height=3,width=9,bg="#39B5E0",fg="black",command=lambda:b_click(bouton8))
    bouton9=tkinter.Button(root2,text=" ",font=("Helvetica",20),height=3,width=9,bg="#39B5E0",fg="black",command=lambda:b_click(bouton9))
    #l'affichage des textes
    txt.grid(row=4,column=1,sticky="n")
    txt1.grid(row=4,column=2,sticky="n")
    txtt.grid(row=5,column=1,sticky="n")
    txtt1.grid(row=5,column=2,sticky="n")
    #l'affichage des boutons 
    bouton1.grid(row=6,column=1)
    bouton2.grid(row=6,column=2)
    bouton3.grid(row=6,column=3)
    bouton4.grid(row=7,column=1)
    bouton5.grid(row=7,column=2)
    bouton6.grid(row=7,column=3)
    bouton7.grid(row=8,column=1)
    bouton8.grid(row=8,column=2)
    bouton9.grid(row=8,column=3)
    # centrer tout cela dans la fenetre
    root2.grid_rowconfigure(0, weight=1)
    root2.grid_columnconfigure(0, weight=1)
    root2.grid_rowconfigure(9, weight=1)
    root2.grid_columnconfigure(4, weight=1)
    #creation des deux boutons responsables au rejouer et retourner 
    restart=tkinter.Button(root2, text=chr(8635), font=("Times", 15), bg="white", fg="black",command=lambda:R())
    restart.grid(row=12,column=3 ,sticky="se")
    ret=tkinter.Button(root2, text="<", font=("Times", 15), bg="white", fg="black",command=lambda:res())
    ret.grid(row=3,column=0,sticky="n")
    tkinter.messagebox.showinfo( "Gumii&Rajae's Tic-Tac-Toe",message="PAY ATTENTION ! the player 1 in the game is who will play with X and the player 2 is who will play with O and for the first game X will start; so the one who wants X write his name first!")
    #fonction qui permet de laisser les boutons ne soient pas cliquables et ne répond à aucune interaction de l'utilisateur
    def disable_all_buttons():
        bouton1.config(state=tkinter.DISABLED)
        bouton2.config(state=tkinter.DISABLED)
        bouton3.config(state=tkinter.DISABLED)
        bouton4.config(state=tkinter.DISABLED)
        bouton5.config(state=tkinter.DISABLED)
        bouton6.config(state=tkinter.DISABLED)
        bouton7.config(state=tkinter.DISABLED)
        bouton8.config(state=tkinter.DISABLED)
        bouton9.config(state=tkinter.DISABLED) 
    #fonction qui va preciser le gagnant
    def win():
        global winner 
        winner =False
        #les cas de gagne pour X 
        if bouton1["text"]=="X" and bouton2["text"]=="X" and bouton3["text"]=="X" :
            bouton1.config(bg="blue",fg="white")
            bouton2.config(bg="blue",fg="white")
            bouton3.config(bg="blue",fg="white")
    # quand la condition est vraie ces boutons vont etre de couleur blue et leur contenu avec le blanc et c'est la meme chose pour les autres
            winner=True
            tkinter.messagebox.showinfo( "Gumii&Rajae's Tic-Tac-Toe",message=(txt1.get(),"won"))
    #ce message va etre affiche apres que le joueur gagne dans chaque cas realisé
            disable_all_buttons()
        elif bouton4["text"]=="X" and bouton5["text"]=="X" and bouton6["text"]=="X" :
            bouton4.config(bg="blue",fg="white")
            bouton5.config(bg="blue",fg="white")
            bouton6.config(bg="blue",fg="white")
            winner=True
            tkinter.messagebox.showinfo( "Gumii&Rajae's Tic-Tac-Toe",message=(txt1.get(),"won"))
            disable_all_buttons()
        elif bouton7["text"]=="X" and bouton8["text"]=="X" and bouton9["text"]=="X" :
            bouton7.config(bg="blue",fg="white")
            bouton8.config(bg="blue",fg="white")
            bouton9.config(bg="blue",fg="white")
            winner=True
            tkinter.messagebox.showinfo( "Gumii&Rajae's Tic-Tac-Toe",message=(txt1.get(),"won"))
            disable_all_buttons()
        elif bouton1["text"]=="X" and bouton4["text"]=="X" and bouton7["text"]=="X" :
            bouton1.config(bg="blue",fg="white")
            bouton4.config(bg="blue",fg="white")
            bouton7.config(bg="blue",fg="white")
            winner=True
            tkinter.messagebox.showinfo( "Gumii&Rajae's Tic-Tac-Toe",message=(txt1.get(),"won"))
            disable_all_buttons()
        elif bouton2["text"]=="X" and bouton5["text"]=="X" and bouton8["text"]=="X" :
            bouton2.config(bg="blue",fg="white")
            bouton5.config(bg="blue",fg="white")
            bouton8.config(bg="blue",fg="white")
            winner=True
            tkinter.messagebox.showinfo( "Gumii&Rajae's Tic-Tac-Toe",message=(txt1.get(),"won"))
            disable_all_buttons()
        elif bouton3["text"]=="X" and bouton6["text"]=="X" and bouton9["text"]=="X" :
            bouton3.config(bg="blue",fg="white")
            bouton6.config(bg="blue",fg="white")
            bouton9.config(bg="blue",fg="white")
            winner=True
            tkinter.messagebox.showinfo( "Gumii&Rajae's Tic-Tac-Toe",message=(txt1.get(),"won"))
            disable_all_buttons()
        elif bouton1["text"]=="X" and bouton5["text"]=="X" and bouton9["text"]=="X" :
            bouton1.config(bg="blue",fg="white")
            bouton5.config(bg="blue",fg="white")
            bouton9.config(bg="blue",fg="white")
            winner=True
            tkinter.messagebox.showinfo( "Gumii&Rajae's Tic-Tac-Toe",message=(txt1.get(),"won"))
            disable_all_buttons()
        elif bouton3["text"]=="X" and bouton5["text"]=="X" and bouton7["text"]=="X" :
            bouton3.config(bg="blue",fg="white")
            bouton5.config(bg="blue",fg="white")
            bouton7.config(bg="blue",fg="white")
            winner=True
            tkinter.messagebox.showinfo( "Gumii&Rajae's Tic-Tac-Toe",message=(txt1.get(),"won"))
            disable_all_buttons()
        #les cas de gagne pour O     
        elif bouton1["text"]=="O" and bouton2["text"]=="O" and bouton3["text"]=="O" :
            bouton1.config(bg="black",fg="white")
            bouton2.config(bg="black",fg="white")
            bouton3.config(bg="black",fg="white")
    # quand la condition est vraie ces boutons vont etre de couleur noir et leur contenu avec le blanc et c'est la meme chose pour les autres
            winner=True
            tkinter.messagebox.showinfo( "Gumii&Rajae's Tic-Tac-Toe",message=(txtt1.get(),"won"))
            #ce message va etre affiche apres que le joueur gagne dans chaque cas realisé
            disable_all_buttons()
        elif bouton4["text"]=="O" and bouton5["text"]=="O" and bouton6["text"]=="O" :
            bouton4.config(bg="black",fg="white")
            bouton5.config(bg="black",fg="white")
            bouton6.config(bg="black",fg="white")
            winner=True
            tkinter.messagebox.showinfo( "Gumii&Rajae's Tic-Tac-Toe",message=(txtt1.get(),"won"))
            disable_all_buttons()
        elif bouton7["text"]=="O" and bouton8["text"]=="O" and bouton9["text"]=="O" :
            bouton7.config(bg="black",fg="white")
            bouton8.config(bg="black",fg="white")
            bouton9.config(bg="black",fg="white")
            winner=True
            tkinter.messagebox.showinfo( "Gumii&Rajae's Tic-Tac-Toe",message=(txtt1.get(),"won"))
            disable_all_buttons()
        elif bouton1["text"]=="O" and bouton4["text"]=="O" and bouton7["text"]=="O" :
            bouton1.config(bg="black",fg="white")
            bouton4.config(bg="black",fg="white")
            bouton7.config(bg="black",fg="white")
            winner=True
            tkinter.messagebox.showinfo( "Gumii&Rajae's Tic-Tac-Toe",message=(txtt1.get(),"won"))
            disable_all_buttons()
        elif bouton2["text"]=="O" and bouton5["text"]=="O" and bouton8["text"]=="O" :
            bouton2.config(bg="black",fg="white")
            bouton5.config(bg="black",fg="white")
            bouton8.config(bg="black",fg="white")
            winner=True
            tkinter.messagebox.showinfo( "Gumii&Rajae's Tic-Tac-Toe",message=(txtt1.get(),"won"))
            disable_all_buttons()
        elif bouton3["text"]=="O" and bouton6["text"]=="O" and bouton9["text"]=="O" :
            bouton3.config(bg="black",fg="white")
            bouton6.config(bg="black",fg="white")
            bouton9.config(bg="black",fg="white")
            winner=True
            tkinter.messagebox.showinfo( "Gumii&Rajae's Tic-Tac-Toe",message=(txtt1.get(),"won"))
            disable_all_buttons()
        elif bouton1["text"]=="O" and bouton5["text"]=="O" and bouton9["text"]=="O" :
            bouton1.config(bg="black",fg="white")
            bouton5.config(bg="black",fg="white")
            bouton9.config(bg="black",fg="white")
            winner=True
            tkinter.messagebox.showinfo( "Gumii&Rajae's Tic-Tac-Toe",message=(txtt1.get(),"won"))
            disable_all_buttons()
        elif bouton3["text"]=="O" and bouton5["text"]=="O" and bouton7["text"]=="O" :
            bouton3.config(bg="black",fg="white")
            bouton5.config(bg="black",fg="white")
            bouton7.config(bg="black",fg="white")
            winner=True
            tkinter.messagebox.showinfo( "Gumii&Rajae's Tic-Tac-Toe",message=(txtt1.get(),"won"))
            disable_all_buttons() 
    #fonction responsable au cas d'egalite
    def nowin():
            if c==9 and winner == False :
                bouton1.config(bg="black",fg="white")
                bouton2.config(bg="black",fg="white")
                bouton3.config(bg="black",fg="white")
                bouton4.config(bg="black",fg="white")
                bouton5.config(bg="black",fg="white")
                bouton6.config(bg="black",fg="white")
                bouton7.config(bg="black",fg="white")
                bouton8.config(bg="black",fg="white")
                bouton9.config(bg="black",fg="white")
                tkinter.messagebox.showinfo("Gumii&Rajae's Tic-Tac-Toe",message=(txt1.get(),"&",txtt1.get(),"have tied"))
    #fonction responsable au clique
    def b_click(b):
        global clicked,c,i
        if b["text"]==' ' and clicked == True :
            b["text"]= "X"
            clicked=False
            for i in range(9):
              c=c+1  
              if win():
                pass
              else:
                if nowin():
                    pass         
              break                 
        elif b["text"]==' ' and clicked == False :
             b["text"]= "O"
             clicked=True
             for i in range(9):
              c+=1
              if win():
                pass
              else:
                if nowin():
                    pass
              break
             
        else : 
            tkinter.messagebox.showerror("Gumii&Rajae's Tic-Tac-Toe","this box has already selected! select another") 
    root2.mainloop()
#fonction pour rejouer   
def R():
      global c
      c=0
      play_fr(root2)
#fonction pour retourner a l'autre fenetre 
def res() :
      new(root2)
#fonction et nouvelle fenetre responsable au jeux avec la machine
def play_web(root1):
    global root3
    root1.withdraw()
    root3 = tkinter.Toplevel()
    root3.geometry("500x500")
    root3.resizable(width=False,height=False)
    screen_width = root1.winfo_screenwidth()
    screen_height =root1.winfo_screenheight()
    x = (screen_width // 2) - (500// 2)
    y = (screen_height // 2) - (500// 2)
    root3.geometry(f"+{x}+{y}")
    root3.config(background="white")
    root3.iconbitmap("C:/Users/user/Downloads/WhatsApp Image 2023-02-09 at 22.46.35.ico")
    #creation des boutons responsables au rejouer et retourner a l'autre fenetre
    restart=tkinter.Button(root3, text=chr(8635), font=("Times", 15), bg="white", fg="black",command=lambda:Re())
    restart.grid(row=9,column=2 ,sticky="se")
    res=tkinter.Button(root3, text="<", font=("Times", 15), bg="white", fg="black",command=lambda:res())
    res.grid(row=9,column=0,sticky="sw")
    #fonction pour retourner 
    def res() :
        new(root3)
    #creation des boutons 
    board = ["", "", "", "", "", "", "", "", ""]
    #liste des cas possibles pour gagner
    winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    #variable pour les deplacements du joueur
    global current_player 
    current_player = "X"
    #creation d'une fonction responsable au gagnants
    def check_winner():
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
                return True
        return False
    import random
    #fonction responsable au deplacements de l'ordinateur
    def computer_move():
        global current_player
        if current_player == "O":
            # on vérifie si l’ordinateur peut gagner dans le prochain mouvement
            for combo in winning_combinations:
                if board[combo[0]] == board[combo[1]] == "O" and board[combo[2]] == "":
                    board[combo[2]] = "O"
                    buttons[combo[2]].config(text="O")
                    current_player = "X"
                    return

                elif board[combo[1]] == board[combo[2]] == "O" and board[combo[0]] == "":
                    board[combo[0]] = "O"
                    buttons[combo[0]].config(text="O")
                    current_player = "X"
                    return

                elif board[combo[0]] == board[combo[2]] == "O" and board[combo[1]] == "":
                    board[combo[1]] = "O"
                    buttons[combo[1]].config(text="O")
                    current_player = "X"
                    return

            # on vérifie si le joueur peut gagner dans le prochain mouvement
            for combo in winning_combinations:
                if board[combo[0]] == board[combo[1]] == "X" and board[combo[2]] == "":
                    board[combo[2]] = "O"
                    buttons[combo[2]].config(text="O")
                    current_player = "X"
                    return

                elif board[combo[1]] == board[combo[2]] == "X" and board[combo[0]] == "":
                    board[combo[0]] = "O"
                    buttons[combo[0]].config(text="O")
                    current_player = "X"
                    return

                elif board[combo[0]] == board[combo[2]] == "X" and board[combo[1]] == "":
                    board[combo[1]] = "O"
                    buttons[combo[1]].config(text="O")
                    current_player = "X"
                    return
            # Sinon, choisissez une cellule vide aléatoire pour faire un mouvement
            while True:
                computer_choice = random.randint(0, 8)
                if board[computer_choice] == "":
                    board[computer_choice] = "O"
                    buttons[computer_choice].config(text="O")
                    current_player = "X"
                    break
    # une fonction pour gérer les clics de bouton
    def button_click(index):
        global current_player
        if board[index] == "":
            board[index] = current_player
            buttons[index].config(text=current_player)
            if check_winner():
                tkinter.messagebox.showinfo("Gumii&Rajae's Tic-Tac-Toe", "you won!")
                disable_buttons()
            elif "" not in board:
                tkinter.messagebox.showinfo("Gumii&Rajae's Tic-Tac-Toe", "No winner ! You have tied !")
                disable_buttons()
            else:
                current_player = "O"
                computer_move()
                if check_winner():
                    tkinter.messagebox.showinfo("Gumii&Rajae's Tic-Tac-Toe", "Computer won!")
                    disable_buttons()   
    #fonction qui permet de laisser les boutons ne soient pas cliquables et ne répond à aucune interaction de l'utilisateur
    def disable_buttons():
        for button in buttons:
          button.config(state="disabled")

    # les boutons 
    buttons = []
    for i in range(9):
        button = tkinter.Button(root3, text="", font=("Helvetica",20), width=8, height=3 ,bg="#39B5E0" ,command=lambda index=i: button_click(index))
        button.grid(row=i//3, column=i%3,sticky="nsew")
        buttons.append(button)
    # les centrer dans la fenetre
    root3.grid_rowconfigure(0, weight=1)
    root3.grid_columnconfigure(0, weight=1)  
    root3.grid_rowconfigure(1, weight=1)
    root3.grid_columnconfigure(1, weight=1)
    root3.grid_rowconfigure(2, weight=1)
    root3.grid_columnconfigure(2, weight=1)
    #fonction pour rejouer 
    def Re():
      play_web(root3)
    root3.mainloop()

    
root.mainloop ()# pour afficher notre fenetre 
