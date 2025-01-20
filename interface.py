import tkinter as tk
import os
from PIL import Image, ImageTk

global image_tk

#canvas.create_windows

def creation_frame_boutton_fen1(fen1):
    """creation de ma frame pour mettre mes bouttons"""
    fr1=tk.Frame(fen1)
    return fr1

def creation_frame_boutton_fen2(fen1):
    """creation de ma frame pour mettre mes bouttons"""
    fr1=tk.Frame(fen1,bg="blue")
    return fr1

def button_quitter():
    bt_quitter=tk.Button(fr1,text="Quitter",command=exit)
    bt_quitter.pack(side="bottom")

def regle():
    """fonction qui a pour but d'ouvrir le fichier pdf"""
    os.system("evince engarde-regles.pdf")

def afficher_image():
    global image_tk
    # Charger l'image depuis le fichier (remplacez "chemin" par le chemin réel)
    chemin_image = "en_garde.jpg"
    image = Image.open(chemin_image)

    # Convertir l'image en format Tkinter PhotoImage
    image_tk = ImageTk.PhotoImage(image)

    # Afficher l'image sur le canevas
    canevas.create_image(0, 0, anchor=tk.NW, image=image_tk)

def mode_basique():
    """fonction permettant de mettre les règles en mode basique"""
    pass
def mode_classique():
    """permet de mettre le jeu en mode classique"""
    pass

def afficher_choix_nom(fen1,fr1):
    lab=tk.Label(fr1,text="JOUEUR1")
    lab.pack(side="top")
    e=tk.Entry(fr1,bd=5)
    e.pack(side="top")
    lab=tk.Label(fr1,text="JOUEUR2")
    lab.pack(side="top")
    e=tk.Entry(fr1,bd=5)
    e.pack(side="top")

def refresh(fen1,fr1,fr_X):
    """cette fonction me refresh l'ancien page après avoir cliqué sur jouer"""
    fr1.pack_forget()
    fr2=creation_frame_boutton_fen1(fen1)
    v=tk.StringVar()
    v.set("basique")#initialisation

    fr_X.pack_forget()
    afficher_choix_nom(fen1,fr2)
    lab1=tk.Label(fr2,text="CHOIX DU MODE")
    R1=tk.Radiobutton(fr2,text="basique",variable=v,value="basique",command=lambda:mode_basique(),bg="red")
    R2=tk.Radiobutton(fr2,text="classique",variable=v,value="classique",command=lambda:mode_classique(),bg="green")
    fr2.pack(side="top",fill=tk.Y)
    lab1.pack(side="top",pady=20)
    R1.pack(side="top")
    R2.pack(side="top")


    #button Quitter
    fr2=creation_frame_boutton_fen2(fen1)
    bt_quitter=tk.Button(fr2,text="Quitter",command=exit)
    fr2.pack(side="right",fill=tk.Y)
    bt_quitter.pack(side="bottom")

def boutton(fen1,fr1,canevas):
    """creation de button"""
    #forget pour oublier les wijets
    #creation du boutton jouer

    fr1.pack(side="top",expand=True,fill=tk.Y)#je pack ma frame pour mettre mes buttons dedans
    bt_jouer=tk.Button(fr1,text="Jouer",height=5,width=30,command=lambda:refresh(fen1,fr1,fr_X))
    canevas.create_window(50,50,window=bt_jouer)
    #bt_para=tk.Button(fr1,text="Paramètre",height=5,width=30,command=lambda:mode_basique())
    bt_aide=tk.Button(fr1,text="Aide",height=5,width=30,command=mode_basique)
    bt_regle=tk.Button(fr1,text="Regle",height=5,width=30,command=regle)
    canevas.pack()
    #bt_jouer.pack(side="top")
    #bt_para.pack(side="top")
    bt_aide.pack(side="top",pady=20)
    bt_regle.pack(side="top",pady=20)
    button_quitter()
    #CdM.pack()

if __name__=="__main__":

    fen1=tk.Tk()
    #fen1=tk.Toplevel(root)
    fen1.title("EN GARDE")
    fen1.geometry("500x500")
    fr_X=tk.Frame(fen1,bg="black")
    fr_X.pack(side="top",expand=True,fill=tk.X)
    l=tk.Label(fr_X,text="JEU DE L'ESCRIME")
    l.pack(side="top")
    fr1=creation_frame_boutton_fen1(fen1)
    canevas = tk.Canvas(fr1, width=400, height=400)
    afficher_image()
    #canevas.pack()

    boutton(fen1,fr1,canevas)
fen1.mainloop()
