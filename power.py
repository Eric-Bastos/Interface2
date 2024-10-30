import customtkinter as ctk 
import os

#--------Funções---------

def shutdown():
    os.system('shutdown -s')
def restart():
    os.system('shutdown /r /t 0')
def logoff():
    os.system('shutdown -l')


#--------Funções---------

ctk.set_appearance_mode('dark')

janela= ctk.CTk()

janela.maxsize(300,400)
janela.minsize(300,400)
janela.title('Power Patch V1.0💣')
janela.iconbitmap('nuclear_boom_bomb_explosion_war_icon_219265.ico')

ctk.CTkLabel(janela,text='Power Patch V1.0',
             font=('verdana',28,'bold'),
             text_color='yellow').pack(pady=10)
desligar=ctk.CTkButton(janela,
                       text='Desligar',
                       width=250,
                       height=20,
                       fg_color='yellow',
                       text_color='black',
                       font=('verdana',18,'bold'),
                       hover_color='gold',
                       cursor='pirate',
                       command=shutdown)
desligar.pack(pady=30)
reniciar=ctk.CTkButton(janela,
                       text='Reniciar',
                       width=250,
                       height=20,
                       fg_color='yellow',
                       text_color='black',
                       font=('verdana',18,'bold'),
                       hover_color='gold',
                       cursor='heart',
                       command= restart)
reniciar.pack(pady=30)
bloquear=ctk.CTkButton(janela,
                       text='Bloquear',
                       width=250,
                       height=20,
                       fg_color='yellow',
                       text_color='black',
                       font=('verdana',18,'bold'),
                       hover_color='gold',
                       cursor='spraycan',
                       command=logoff)
bloquear.pack(pady=30)



janela.mainloop()