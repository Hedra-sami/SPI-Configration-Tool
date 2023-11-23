import tkinter as TK
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

import datetime
import os
#Generate Code
def Gen():

    code = "/***********************************************************\n"
    code += " * MSPI_Config.h\n *\n * Created on: "
    x  =  datetime.datetime.now() 
    code  +=  f"{x.strftime('%m/%d/%Y')}\n * Author: "
    x  =  os.getlogin()
    code +=  f"{x}\n"
    code += " * SWC:   SPI                                              \n"
    code += " * Layer: MCAL                                             \n"
    code += " **********************************************************/ \n\n\n"
    code += "#ifndef MSPI_CONFIG_H_\n#define MSPI_CONFIG_H_\n\n#define MSPI1_STATUS         "
    
    if   state.get()  ==  "Enable": code += "MSPI_ENABLE\n"
    elif state.get()  ==  "Disable": code += "MSPI_DISABLE\n"
        
    code += "\n#define MSPI1_CLOCK_MODE     "
    if   Clk.get()  ==  "Mode 0": code += "MSPI_MODE1\n"
    elif Clk.get()  ==  "Mode 1": code += "MSPI_MODE2\n"
    elif Clk.get()  ==  "Mode 2": code += "MSPI_MODE3\n"
    elif Clk.get()  ==  "Mode 3": code += "MSPI_MODE4\n"
        
    code += "\n#define MSPI1_MASTER_SLAVE   "
    if   Master_Slave.get()  ==  "Master": code += "MSPI_MASTER\n"
    elif Master_Slave.get()  ==  "Slave": code += "MSPI_SLAVE\n"
        
    code += "\n#define MSPI1_PRESCALLER     "
    if   PRESCALER.get()  ==  "DIVIDED_BY_2": code += "MSPI_FPCLK_DIVIDED_BY_2\n"
    elif PRESCALER.get()  ==  "DIVIDED_BY_4": code += "MSPI_FPCLK_DIVIDED_BY_4\n"
    elif PRESCALER.get()  ==  "DIVIDED_BY_8": code += "MSPI_FPCLK_DIVIDED_BY_8\n"
    elif PRESCALER.get()  ==  "DIVIDED_BY_16": code += "MSPI_FPCLK_DIVIDED_BY_16\n"
    elif PRESCALER.get()  ==  "DIVIDED_BY_32": code += "MSPI_FPCLK_DIVIDED_BY_32\n"
    elif PRESCALER.get()  ==  "DIVIDED_BY_64": code += "MSPI_FPCLK_DIVIDED_BY_64\n"
    elif PRESCALER.get()  ==  "DIVIDED_BY_128": code += "MSPI_FPCLK_DIVIDED_BY_128\n"
    elif PRESCALER.get()  ==  "DIVIDED_BY_256": code += "MSPI_FPCLK_DIVIDED_BY_256\n"
        
    code += "\n#define MSPI1_DATA_ORDER     "
    if   DATA_ORDER.get()  ==  "MSB_FIRST": code += "MSPI_MSB_FIRST\n"
    elif DATA_ORDER.get()  ==  "LSB_FIRST": code += "MSPI_LSB_FIRST\n"
        
    code += "\n#define MSPI1_SS_MANAGE      "
    if   SS_MANAGE.get()  ==  "HW_SLAVE_MANAGEMENT": code += "MSPI_HW_SLAVE_MANAGEMENT\n"
    elif SS_MANAGE.get()  ==  "SW_SLAVE_MANAGEMENT": code += "MSPI_SW_SLAVE_MANAGEMENT\n"
        
    code += "\n#define MSPI1_DATA_SIZE      "
    if   DATA_SIZE.get()  ==  "8BIT_DATA": code += "MSPI_8BIT_DATA\n"
    elif DATA_SIZE.get()  ==  "16BIT_DATA": code += "MSPI_16BIT_DATA\n"
        
    code += "\n#define MSPI1_TX_INT_STATUS  " 
    if   TX_INTERRUPT_STATE.get()  ==  "TX_INTERRUPT_ENABLE": code += "MSPI_INT_ENABLE\n"
    elif TX_INTERRUPT_STATE.get()  ==  "TX_INTERRUPT_DISABLE": code += "MSPI_INT_DISABLE\n"
        
    code += "\n#define MSPI1_RX_INT_STATUS  " 
    if   RX_INTERRUPT_STATE.get()  ==  "RX_INTERRUPT_ENABLE": code += "MSPI_INT_ENABLE\n"
    elif RX_INTERRUPT_STATE.get()  ==  "RX_INTERRUPT_DISABLE": code += "MSPI_INT_DISABLE\n"
        
    code += "\n#define MSPI_SS_PORT         " 
    if   SS_PORT.get()  ==  "GPIO_PORTA": code += "PORTA\n"
    elif SS_PORT.get()  ==  "GPIO_PORTB": code += "PORTB\n"
    elif SS_PORT.get()  ==  "GPIO_PORTC": code += "PORTC\n"
        
    code += "\n#define MSPI_SS_PIN          "
    x  =  ((MSPI1_SS_PIN.get()).upper()).strip()
    print(x)
    if   x  ==  "0": code  += "PIN0\n"
    elif x  ==  "1": code  += "PIN1\n"
    elif x  ==  "2": code  += "PIN2\n"
    elif x  ==  "3": code  += "PIN3\n"
    elif x  ==  "4": code  += "PIN4\n"
    elif x  ==  "5": code  += "PIN5\n"
    elif x  ==  "6": code  += "PIN6\n"
    elif x  ==  "7": code  += "PIN7\n"
    elif x  ==  "8": code  += "PIN8\n"
    elif x  ==  "9": code  += "PIN9\n"
    elif x  ==  "10": code += "PIN10\n"
    elif x  ==  "11": code += "PIN11\n"
    elif x  ==  "12": code += "PIN12\n"
    elif x  ==  "13": code += "PIN13\n"
    elif x  ==  "14": code += "PIN14\n"
    elif x  ==  "15": code += "PIN15\n"


    if (state.get()  ==  "" or Clk.get()  ==  "" 
                          or Master_Slave.get()  ==  "" 
                          or PRESCALER.get()  ==  "" 
                          or DATA_ORDER.get()  ==  "" 
                          or SS_MANAGE.get()  ==  "" 
                          or DATA_SIZE.get()  ==  "" 
                          or TX_INTERRUPT_STATE.get()  ==  "" 
                          or RX_INTERRUPT_STATE.get()  ==  "" 
                          or SS_PORT.get()  ==  "" 
                          or MSPI1_SS_PIN.get()  ==  ""): 
        return 0
    else:
    
        code += "\n\n#endif\n"
        file  =  open('MSPI_Config.h','w')
        file.write(code)
        print("File has been generated")
    



main_screen  =  TK.Tk()
main_screen.title("SPI Configuration")
main_screen.resizable(False, False)
main_screen.geometry("1000x800+20+20")
main_screen.configure(bg="#f1f1f1")


#MSPI1_STATE
MSPI1_STATE  =  TK.Label(
    main_screen,text = "MSPI1_STATUS",
    font = ("Times", 15, "bold"),
    fg = "black",
    bg = "#f1f1f1")
MSPI1_STATE.place(x = 20,y = 20)
state = TK.StringVar()
state_menu = ttk.OptionMenu(main_screen, state, "    --SELECT--    ", "Enable", "Disable")
state_menu['menu'].config(font = ('Times', 10), bg="white", fg="black")
state_menu.place(x=400,y=20)



#MSPI1_CLK_MODE
MSPI1_CLK_MODE  =  TK.Label(
    main_screen,text = "MSPI1 CLK_MODE",
    font = ("Times", 15, "bold"),
    fg = "black",
    bg = "#f1f1f1")
MSPI1_CLK_MODE.place(x = 20,y = 100)
Clk = TK.StringVar()
clk_menu = ttk.OptionMenu(main_screen, Clk, "    --SELECT--    ", "Mode 0", "Mode 1","Mode 2","Mode 3")
clk_menu['menu'].config(font = ('Times', 10), bg="white", fg="black")
clk_menu.place(x=400,y=100)





#MSPI1_MASTER_SLAVE

MSPI1_MASTER_SLAVE  =  TK.Label(
    main_screen,
    text = "MSPI1 MASTER SLAVE",
    font = ("Times", 15, "bold"),
    fg = "black",  
    bg = "#f1f1f1",

)
MSPI1_MASTER_SLAVE.place(x = 20,y = 180)
Master_Slave = TK.StringVar()
MS_menu = ttk.OptionMenu(main_screen, Master_Slave, "    --SELECT--    ", "Master", "Slave")
MS_menu['menu'].config(font = ('Times', 10), bg="white", fg="black")
MS_menu.place(x=400,y=180)

#MSPI1_PRESCALER


MSPI1_PRESCALER = TK.Label(main_screen,text="MSPI1 PRESCALER",font=("Times", 15, "bold"),fg="black",bg="#f1f1f1")
MSPI1_PRESCALER.place(x=20,y=250)
PRESCALER = TK.StringVar()
PRESCALER_option_menu = ttk.OptionMenu(main_screen, PRESCALER, "    --SELECT--    ", "DIVIDED_BY_2", "DIVIDED_BY_4", "DIVIDED_BY_8", "DIVIDED_BY_16", "DIVIDED_BY_32", "DIVIDED_BY_64", "DIVIDED_BY_128", "DIVIDED_BY_256")
PRESCALER_option_menu['menu'].config(font = ('Times', 10), bg="white", fg="black")
PRESCALER_option_menu.place(x=400,y=250)



#MSPI1_DATA_ORDER


MSPI1_DATA_ORDER = TK.Label(main_screen,text="MSPI1 DATA_ORDER",font=("Times", 15, "bold"),fg="black",bg="#f1f1f1")
MSPI1_DATA_ORDER.place(x=20,y=300)
DATA_ORDER = TK.StringVar()
DATA_ORDER_option_menu = ttk.OptionMenu(main_screen, DATA_ORDER, "    --SELECT--    ", "MSB_FIRST", "LSB_FIRST")
DATA_ORDER_option_menu['menu'].config(font = ('Times', 10), bg="white", fg="black")
DATA_ORDER_option_menu.place(x=400,y=300)


#MSPI1_SS_MANAGE


MSPI1_SS_MANAGE = TK.Label(main_screen,text="MSPI1 SS_MANAGE",font=("Times", 15, "bold"),fg="black",bg="#f1f1f1")
MSPI1_SS_MANAGE.place(x=20,y=350)
SS_MANAGE = TK.StringVar()
SS_MANAGE_option_menu = ttk.OptionMenu(main_screen, SS_MANAGE, "    --SELECT--    ", "HW_SLAVE_MANAGEMENT", "SW_SLAVE_MANAGEMENT")
SS_MANAGE_option_menu['menu'].config(font = ('Times', 10), bg="white", fg="black")
SS_MANAGE_option_menu.place(x=400,y=350)






#MSPI1_DATA_SIZE
MSPI1_DATA_SIZE = TK.Label(main_screen,text="MSPI1 DATA_SIZE",font=("Times", 15, "bold"),fg="black",bg="#f1f1f1")
MSPI1_DATA_SIZE.place(x=20,y=400)
DATA_SIZE = TK.StringVar()
DATA_SIZE_option_menu = ttk.OptionMenu(main_screen, DATA_SIZE, "    --SELECT--    ", "8BIT_DATA", "16BIT_DATA")
DATA_SIZE_option_menu['menu'].config(font = ('Times', 10), bg="white", fg="black")
DATA_SIZE_option_menu.place(x=400,y=400)



#MSPI1_TX_INTERRUPT_STATE

MSPI1_TX_INTERRUPT_STATE = TK.Label(main_screen,text="MSPI1 TX INTERRUPT STATE",font=("Times", 15, "bold"),fg="black",bg="#f1f1f1")
MSPI1_TX_INTERRUPT_STATE.place(x=20,y=450)
TX_INTERRUPT_STATE = TK.StringVar()
TX_INTERRUPT_STATE_menu = ttk.OptionMenu(main_screen, TX_INTERRUPT_STATE, "    --SELECT--    ", "TX_INTERRUPT_ENABLE", "TX_INTERRUPT_DISABLE")
TX_INTERRUPT_STATE_menu['menu'].config(font = ('Times', 10), bg="white", fg="black")
TX_INTERRUPT_STATE_menu.place(x=400,y=450)


#MSPI1_RX_INTERRUPT_STATE

MSPI1_RX_INTERRUPT_STATE = TK.Label(main_screen,text="MSPI1 RX INTERRUPT STATE",font=("Times", 15, "bold"),fg="black",bg="#f1f1f1")
MSPI1_RX_INTERRUPT_STATE.place(x=20,y=500)
RX_INTERRUPT_STATE = TK.StringVar()
RX_INTERRUPT_STATE_menu = ttk.OptionMenu(main_screen, RX_INTERRUPT_STATE, "    --SELECT--    ", "RX_INTERRUPT_ENABLE", "RX_INTERRUPT_DISABLE")
RX_INTERRUPT_STATE_menu['menu'].config(font = ('Times', 10), bg="white", fg="black")
RX_INTERRUPT_STATE_menu.place(x=400,y=500)


# MSPI1_SS_PORT Label

MSPI1_SS_PORT = TK.Label(main_screen,text="MSPI1 SS PORT",font=("Times", 15, "bold"),fg="black",bg="#f1f1f1")
MSPI1_SS_PORT.place(x=20,y=550)
SS_PORT = TK.StringVar()
SS_PORT_option_menu = ttk.OptionMenu(main_screen, SS_PORT, "    --SELECT--    ", "GPIO_PORTA", "GPIO_PORTB", "GPIO_PORTC")
SS_PORT_option_menu['menu'].config(font = ('Times', 10), bg="white", fg="black")
SS_PORT_option_menu.place(x=400,y=550)

# MSPI1_SS_PIN Entry

MSPI1_SS_PIN = TK.Label(main_screen,text="MSPI1 SS PIN", font=("Times", 15, "bold") ,fg="black",bg="#f1f1f1")
MSPI1_SS_PIN.place(x=20,y=600)
MSPI1_SS_PIN  =  TK.Entry(
    main_screen,
    width = 25,  
    font = ("Times", 16),  
    bg = "white",  
    fg = "black",  
)
MSPI1_SS_PIN.place(x = 400, y = 600)



#Generate Button
Generate  =  TK.Button(main_screen,text = "Generate",font = ('arial', 24, 'bold'),bg = "black", fg = "white",command = Gen)
Generate.place(x = 800,y = 650)






main_screen.mainloop()