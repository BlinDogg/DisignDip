from tkinter import *
import sys
from time import sleep
from simulation_reborn import go



class Zal(Tk):


    def __init__(self):
        Tk.__init__(self)
        a = list()
        self.a = a
        self.geometry('800x250')
        self.overrideredirect(True) #ДОБАВИТЬ КРЕСТИК
        self.attributes("-topmost",True)
        self.resizable(False, True)
        self.title('ZalupaGovna')
        self.set_ui()

    def set_ui(self):
        self.first_ui()


    def first_ui(self):
        ArrRate = IntVar()
        NumNodes = IntVar()
        Flag1 = IntVar()
        Flag2 = IntVar()

        self.Exit()

        self.label1_1 = Label(self, text="Simulation parameters", font='Arial 18')
        self.label1_1.place(relx=.03, rely=.0)

        self.label1_2 = Label(self, text="Arrival rate", font='Arial 14')
        self.label1_2.place(relx=.03, rely=.20)

        self.label1_3 = Label(self, text="Numbers of Nodes", font='Arial 14')
        self.label1_3.place(relx=.03, rely=.40)

        self.entry1_1 = Entry(self, textvariable=ArrRate, font='Arial 14')
        self.entry1_1.delete(first=0, last=END)
        self.entry1_1.insert(END, '1')  # ПОЗВОЛЯЕТ ВВОДИТЬ ЗНАЧЕНИЯ ПО УМОЛЧАНИЮ
        self.entry1_1.place(relx=.25, rely=.20)

        self.entry1_2 = Entry(self, textvariable=NumNodes, font='Arial 14')
        self.entry1_2.delete(first=0, last=END)
        self.entry1_2.insert(END, '4')
        self.entry1_2.place(relx=.25, rely=.40)

        self.flag1 = Checkbutton(self, text="All Nodes have same departure rates", variable=Flag1, font='Arial 13')
        self.flag1.place(relx=.05, rely=.60)
        self.flag1.select()

        self.flag2 = Checkbutton(self, text="All Nodes have same queue length", variable=Flag2, font='Arial 13')
        self.flag2.place(relx=.45, rely=.60)
        self.flag2.select()

        self.next_button1 = Button(self, text="Next", command=lambda: self.NextWin(Flag1, Flag2, ArrRate, NumNodes), padx=18, pady=5)
        self.next_button1.place(relx=.90, rely=.85, anchor="c")



    def AppExit(self):
        self.destroy()
        sys.exit()

    def NextWin(self, Flag1, Flag2, ArrRate, NumNodes):
        self.Flag1 = Flag1
        self.Flag2 = Flag2
        self.ArrRate = ArrRate
        self.NumNodes = NumNodes

        if Flag1.get() == 1:
            FlagBul1 = True
        else:
            FlagBul1 = False
        if Flag2.get() == 1:
            FlagBul2 = True
        else:
            FlagBul2 = False
        try:
            ArrRate.get()
        except:
            self.clear()
            self.first_ui()
            self.labelExcept1 = Label(self, text="Arrival Rate must be a number", font='Arial 12', fg='red')
            self.labelExcept1.place(x=430, y=50)
        try:
            NumNodes.get()
        except:
            self.clear()
            self.first_ui()
            self.labelExcept1 = Label(self, text="Number of Nodes must be a integer", font='Arial 12', fg='red')
            self.labelExcept1.place(x=430, y=100)
        ArrRateInt = ArrRate.get()
        NumNodesInt = NumNodes.get()
        if ArrRateInt <= 0:
            self.clear()
            self.first_ui()
            labelExcept2 = Label(self, text="Arrival Rate must be a positive", font='Arial 12', fg='red')
            labelExcept2.place(x=430, y=50)
        elif NumNodesInt <= 0:
            self.clear()
            self.first_ui()
            labelExcept2 = Label(self, text="Number of Nodes must be a positive", font='Arial 12', fg='red')
            labelExcept2.place(x=430, y=100)
        else:
            self.a.append(ArrRateInt)
            self.a.append(NumNodesInt)
            self.a.append(FlagBul1)
            self.a.append(FlagBul2)
            self.clear()
            self.second_ui()
            self.check_grey()

    def check_grey(self):
        if self.a[2] == True and self.a[3] == True:
            for i in range(self.Nodes):
                pos = i * 25 + 130
                self.entry = Entry(self, font='Arial 14', background='grey', state=DISABLED)
                self.entry.delete(first=0, last=END)
                self.entry.insert(END, '')
                self.entry.place(relx=.15, y=pos)
                self.entry0 = Entry(self, font='Arial 14', background='grey', state=DISABLED)
                self.entry0.delete(first=0, last=END)
                self.entry0.insert(END, '')
                self.entry0.place(relx=.43, y=pos)

        if self.a[2] == True and self.a[3] == False:
            for i in range(self.Nodes):
                pos = i * 25 + 130
                self.entry = Entry(self, font='Arial 14', background='grey', state=DISABLED)
                self.entry.delete(first=0, last=END)
                self.entry.insert(END, '')
                self.entry.place(relx=.15, y=pos)
            self.entry2_2 = Entry(self, font='Arial 14', background='grey', state=DISABLED)
            self.entry2_2.delete(first=0, last=END)
            self.entry2_2.insert(END, '')
            self.entry2_2.place(x=280, y=60)

        if self.a[3] == True and self.a[2] == False:
            for i in range(self.Nodes):
                pos = i * 25 + 130
                self.entry0 = Entry(self, font='Arial 14', background='grey', state=DISABLED)
                self.entry0.delete(first=0, last=END)
                self.entry0.insert(END, '')
                self.entry0.place(relx=.43, y=pos)
            self.entry2_1 = Entry(self, font='Arial 14', background='grey', state=DISABLED)
            self.entry2_1.delete(first=0, last=END)
            self.entry2_1.insert(END, '')
            self.entry2_1.place(x=280, y=30)

        if self.a[2] == False and self.a[3] == False:
            self.entry2_1 = Entry(self, font='Arial 14', background='grey', state=DISABLED)
            self.entry2_1.delete(first=0, last=END)
            self.entry2_1.insert(END, '')
            self.entry2_1.place(x=280, y=30)
            self.entry2_2 = Entry(self, font='Arial 14', background='grey', state=DISABLED)
            self.entry2_2.delete(first=0, last=END)
            self.entry2_2.insert(END, '')
            self.entry2_2.place(x=280, y=60)


    def second_ui(self):
        self.BulkRate = IntVar()
        self.BulkMax = IntVar()
        self.dick=dict()
        self.deck=dict()
        self.Exit()

        self.label2_1 = Label(self, text="Set Node Parametrs", font='Arial 18')
        self.label2_1.place(x=15, y=0)

        self.label2_2 = Label(self, text="Bulk Departure Rate", font='Arial 14')
        self.label2_2.place(x=25, y=30)

        self.label2_3 = Label(self, text="Bulk Max Queue Length", font='Arial 14')
        self.label2_3.place(x=25, y=60)

        self.entry2_1 = Entry(self, textvariable=self.BulkRate, font='Arial 14')
        self.entry2_1.delete(first=0, last=END)
        self.entry2_1.insert(END, '1')  # ПОЗВОЛЯЕТ ВВОДИТЬ ЗНАЧЕНИЯ ПО УМОЛЧАНИЮ
        self.entry2_1.place(x=280, y=30)

        self.entry2_2 = Entry(self, textvariable=self.BulkMax, font='Arial 14')
        self.entry2_2.delete(first=0, last=END)
        self.entry2_2.insert(END, '4')
        self.entry2_2.place(x=280, y=60)

        self.label2_4 = Label(self, text="Departure Rate", font='Arial 14')
        self.label2_4.place(x=150, y=95)

        self.label2_5 = Label(self, text="Max Queue Length", font='Arial 14')
        self.label2_5.place(x=380, y=95)

        self.Nodes = self.a[1]
        for i in range(self.Nodes):
            self.dick.update({i: IntVar()})
            self.deck.update({i: IntVar()})

        self.geometry(f'800x{self.Nodes*25+180}')
        for i in range(self.Nodes):

            pos=i*25+130
            self.pos=pos
            Label(self, text=f'Node {i+1}', font='Arial 14').place(x=30, y=pos)
            self.entry = Entry(self, textvariable=self.dick.get(i), font='Arial 14')
            self.entry.delete(first=0, last=END)
            self.entry.insert(END, '1')
            self.entry.place(relx=.15, y=pos)

            self.entry0 = Entry(self, textvariable=self.deck.get(i), font='Arial 14')
            self.entry0.delete(first=0, last=END)
            self.entry0.insert(END, '4')
            self.entry0.place(relx=.43, y=pos)


        self.next_button2 = Button(self, text="Dynamic", command=lambda: self.Dynamic_ui_check(),
                                   padx=18, pady=5)
        self.next_button2.place(relx=.80, y=self.pos, anchor="c")

        self.next_button3 = Button(self, text="   Static   ", command=lambda: self.Static_ui_check(),
                                   padx=18, pady=5)
        self.next_button3.place(relx=.92, y=self.pos, anchor="c")
        self.back_button1 = Button(self, text="Back", command=lambda: self.back_1(),
                                   padx=30, pady= 5)
        self.back_button1.place(relx=.86, y=self.pos+40, anchor="c")

    def back_1(self):
        self.geometry('800x250')
        self.clear()
        self.set_ui()
        self.entry1_1.delete(first=0, last=END)
        self.entry1_1.insert(END, self.a[0])
        self.entry1_2.delete(first=0, last=END)
        self.entry1_2.insert(END, self.a[1])
        if self.a[2]==False:
            self.flag1.deselect()
        if self.a[3]==False:
            self.flag2.deselect()
        self.a.clear()






    def Dynamic_ui_check(self):
        self.dickF = dict()
        self.deckF = dict()
        BulkMax = self.BulkMax
        BulkRate = self.BulkRate
        q = 0
        try:
            BulkRate.get()
        except:
            self.clear()
            self.NextWin(self.Flag1, self.Flag2, self.ArrRate, self.NumNodes)
            self.labelExcept3 = Label(self, text="Bulk Departure Rate must be a integer", font='Arial 12', fg='red')
            self.labelExcept3.place(x=530, y=30)
        try:
            BulkMax.get()
        except:
            self.clear()
            self.NextWin(self.Flag1, self.Flag2, self.ArrRate, self.NumNodes)
            self.labelExcept3 = Label(self, text="Max Queue Length must be a integer", font='Arial 12', fg='red')
            self.labelExcept3.place(x=530, y=60)
        self.BulkRateF = BulkRate.get()
        self.BulkMaxF = BulkMax.get()
        if self.BulkRateF <= 0:
            self.clear()
            self.NextWin(self.Flag1, self.Flag2, self.ArrRate, self.NumNodes)
            labelExcept5 = Label(self, text="Bulk Departure Rate must be a positive", font='Arial 12', fg='red')
            labelExcept5.place(x=530, y=30)
        elif self.BulkMaxF <= 0:
            self.clear()
            self.NextWin(self.Flag1, self.Flag2, self.ArrRate, self.NumNodes)
            labelExcept5 = Label(self, text="Max Queue Length must be a positive", font='Arial 12', fg='red')
            labelExcept5.place(x=530, y=60)
        else:
            for i in range(self.Nodes):
                pos = i * 25 + 130
                dickInt = self.dick.get(i)
                deckInt = self.deck.get(i)
                try:
                    deckInt.get()
                except:
                    self.clear()
                    self.NextWin(self.Flag1, self.Flag2, self.ArrRate, self.NumNodes)
                    self.labelExcept3 = Label(self, text="<-----Max Queue Length \nmust be a integer", font='Arial 12',
                                              fg='red')
                    self.labelExcept3.place(relx=.72, y=pos)
                try:
                    dickInt.get()
                except:
                    self.clear()
                    self.NextWin(self.Flag1, self.Flag2, self.ArrRate, self.NumNodes)
                    self.labelExcept3 = Label(self, text="<-----Departure Rate \nmust be a number", font='Arial 12',
                                              fg='red')
                    self.labelExcept3.place(relx=.72, y=pos)
                self.dickF.update({i: dickInt.get()})
                self.deckF.update({i: deckInt.get()})

                if deckInt.get() <= 0:
                    self.clear()
                    self.NextWin(self.Flag1, self.Flag2, self.ArrRate, self.NumNodes)
                    labelExcept4 = Label(self, text="<-----Max Queue Length \nmust be a positive", font='Arial 12',
                                         fg='red')
                    labelExcept4.place(relx=.72, y=pos)
                elif dickInt.get() <= 0:
                    self.clear()
                    self.NextWin(self.Flag1, self.Flag2, self.ArrRate, self.NumNodes)
                    labelExcept4 = Label(self, text="<-----Departure Rate \nmust be a positive", font='Arial 12',
                                         fg='red')
                    labelExcept4.place(relx=.72, y=pos)
                else:
                    q += 1
                    if q == self.Nodes:
                        self.Dynamic_ui()



    def Dynamic_ui(self):
        self.isdynamik = True
        self.clear()
        self.Exit()
        self.back_button2 = Button(self, text="Back", command=lambda: self.back_2(),
                                   padx=30, pady=5)
        self.back_button2.place(relx=.75, rely=.85, anchor="c")
        self.DropWin = IntVar()
        self.DThreshold = DoubleVar()
        self.DWindow = IntVar()
        self.DSize = IntVar()

        self.geometry('800x250')
        self.label3_1 = Label(self, text="Simulation parameters", font='Arial 18')
        self.label3_1.place(relx=.03, rely=.0)

        self.label3_2 = Label(self, text="Drop Window", font='Arial 14')
        self.label3_2.place(relx=.03, rely=.20)

        self.label3_3 = Label(self, text="Discrepancy Thershold", font='Arial 14')
        self.label3_3.place(relx=.03, rely=.40)

        self.label3_4 = Label(self, text="Discrepancy Window", font='Arial 14')
        self.label3_4.place(relx=.03, rely=.60)

        self.label3_5 = Label(self, text="Stationary Data Size", font='Arial 14')
        self.label3_5.place(relx=.03, rely=.80)

        self.entry3_1 = Entry(self, textvariable=self.DropWin, font='Arial 14')
        self.entry3_1.delete(first=0, last=END)
        self.entry3_1.insert(END, '30')  # ПОЗВОЛЯЕТ ВВОДИТЬ ЗНАЧЕНИЯ ПО УМОЛЧАНИЮ
        self.entry3_1.place(relx=.35, rely=.20)

        self.entry3_2 = Entry(self, textvariable=self.DThreshold, font='Arial 14')
        self.entry3_2.delete(first=0, last=END)
        self.entry3_2.insert(END, '0.01')
        self.entry3_2.place(relx=.35, rely=.40)

        self.entry3_3 = Entry(self, textvariable=self.DWindow, font='Arial 14')
        self.entry3_3.delete(first=0, last=END)
        self.entry3_3.insert(END, '2000')
        self.entry3_3.place(relx=.35, rely=.60)

        self.entry3_4 = Entry(self, textvariable=self.DSize, font='Arial 14')
        self.entry3_4.delete(first=0, last=END)
        self.entry3_4.insert(END, '5000')
        self.entry3_4.place(relx=.35, rely=.80)

        self.next_button_dn = Button(self, text="Start Simulation", command=lambda: self.Dynamic_simulation_ui(),
                                   padx=18, pady=5)
        self.next_button_dn.place(relx=.92, rely=.85, anchor="c")



    def Static_ui_check(self):
        self.dickF = dict()
        self.deckF = dict()
        BulkMax = self.BulkMax
        BulkRate = self.BulkRate
        q = 0
        try:
            BulkRate.get()
        except:
            self.clear()
            self.NextWin(self.Flag1, self.Flag2, self.ArrRate, self.NumNodes)
            self.labelExcept3 = Label(self, text="Bulk Departure Rate must be a integer", font='Arial 12', fg='red')
            self.labelExcept3.place(x=530, y=30)
        try:
            BulkMax.get()
        except:
            self.clear()
            self.NextWin(self.Flag1, self.Flag2, self.ArrRate, self.NumNodes)
            self.labelExcept3 = Label(self, text="Max Queue Length must be a integer", font='Arial 12', fg='red')
            self.labelExcept3.place(x=530, y=60)
        self.BulkRateF = BulkRate.get()
        self.BulkMaxF = BulkMax.get()

        if self.BulkRateF <= 0:
            self.clear()
            self.NextWin(self.Flag1, self.Flag2, self.ArrRate, self.NumNodes)
            labelExcept5 = Label(self, text="Bulk Departure Rate must be a positive", font='Arial 12', fg='red')
            labelExcept5.place(x=530, y=30)
        elif self.BulkMaxF <= 0:
            self.clear()
            self.NextWin(self.Flag1, self.Flag2, self.ArrRate, self.NumNodes)
            labelExcept5 = Label(self, text="Max Queue Length must be a positive", font='Arial 12', fg='red')
            labelExcept5.place(x=530, y=60)
        else:
            for i in range(self.Nodes):
                pos = i * 25 + 130
                dickInt = self.dick.get(i)
                deckInt = self.deck.get(i)
                try:
                    deckInt.get()
                except:
                    self.clear()
                    self.NextWin(self.Flag1, self.Flag2, self.ArrRate, self.NumNodes)
                    self.labelExcept3 = Label(self, text="<-----Max Queue Length \nmust be a integer", font='Arial 12', fg='red')
                    self.labelExcept3.place(relx=.72, y=pos)
                try:
                    dickInt.get()
                except:
                    self.clear()
                    self.NextWin(self.Flag1, self.Flag2, self.ArrRate, self.NumNodes)
                    self.labelExcept3 = Label(self, text="<-----Departure Rate \nmust be a number", font='Arial 12', fg='red')
                    self.labelExcept3.place(relx=.72, y=pos)
                self.dickF.update({i: dickInt.get()})
                self.deckF.update({i: deckInt.get()})

                if deckInt.get() <= 0:
                    self.clear()
                    self.NextWin(self.Flag1, self.Flag2, self.ArrRate, self.NumNodes)
                    labelExcept4 = Label(self, text="<-----Max Queue Length \nmust be a positive", font='Arial 12', fg='red')
                    labelExcept4.place(relx=.72, y=pos)
                elif dickInt.get() <= 0:
                    self.clear()
                    self.NextWin(self.Flag1, self.Flag2, self.ArrRate, self.NumNodes)
                    labelExcept4 = Label(self, text="<-----Departure Rate \nmust be a positive", font='Arial 12', fg='red')
                    labelExcept4.place(relx=.72, y=pos)
                else:
                    q+=1
                    if q == self.Nodes:
                        self.Static_ui()


    def Static_ui(self):
        self.isdynamik = False
        self.clear()
        self.Exit()
        self.back_button2 = Button(self, text="Back", command=lambda: self.back_2(),
                                   padx=30, pady=5)
        self.back_button2.place(relx=.75, rely=.85, anchor="c")
        self.DropWin = IntVar()
        self.Sign = IntVar()

        self.geometry('800x250')
        self.label3_1 = Label(self, text="Simulation parameters", font='Arial 18')
        self.label3_1.place(relx=.03, rely=.0)

        self.label3_2 = Label(self, text="Drop Window", font='Arial 14')
        self.label3_2.place(relx=.03, rely=.20)

        self.label3_3 = Label(self, text="Numbers of Signals", font='Arial 14')
        self.label3_3.place(relx=.03, rely=.40)

        self.entry3_1 = Entry(self, textvariable=self.DropWin, font='Arial 14')
        self.entry3_1.delete(first=0, last=END)
        self.entry3_1.insert(END, '30')  # ПОЗВОЛЯЕТ ВВОДИТЬ ЗНАЧЕНИЯ ПО УМОЛЧАНИЮ
        self.entry3_1.place(relx=.35, rely=.20)

        self.entry3_2 = Entry(self, textvariable=self.Sign, font='Arial 14')
        self.entry3_2.delete(first=0, last=END)
        self.entry3_2.insert(END, '5000')
        self.entry3_2.place(relx=.35, rely=.40)

        self.next_button_st = Button(self, text="Start Simulation", command=lambda: self.Static_simulation_ui(),
                                   padx=18, pady=5)
        self.next_button_st.place(relx=.92, rely=.85, anchor="c")


    def back_2(self):
        self.clear()
        self.NextWin(self.Flag1, self.Flag2, self.ArrRate, self.NumNodes)
        self.entry2_1.delete(first=0, last=END)
        self.entry2_1.insert(END, self.BulkRateF)
        self.entry2_2.delete(first=0, last=END)
        self.entry2_2.insert(END, self.BulkMaxF)
        for i in range(self.Nodes):
            pos = i * 25 + 130
            self.entry = Entry(self, textvariable=self.dick.get(i), font='Arial 14')
            self.entry.delete(first=0, last=END)
            self.entry.insert(END, self.dickF.get(i))
            self.entry.place(relx=.15, y=pos)

            self.entry0 = Entry(self, textvariable=self.deck.get(i), font='Arial 14')
            self.entry0.delete(first=0, last=END)
            self.entry0.insert(END, self.deckF.get(i))
            self.entry0.place(relx=.43, y=pos)
        self.check_grey()



    def Static_simulation_ui(self):  #Check
        DropWin = self.DropWin
        Sign = self.Sign

        try:
            DropWin.get()
        except:
            self.clear()
            self.Static_ui_check()
            self.labelExcept6 = Label(self, text="Drop Window must be a integer", font='Arial 12', fg='red')
            self.labelExcept6.place(relx=.65, rely=.20)
        try:
            Sign.get()
        except:
            self.clear()
            self.Static_ui_check()
            self.labelExcept7 = Label(self, text="Number of Signals must be a integer", font='Arial 12', fg='red')
            self.labelExcept7.place(relx=.65, rely=.40)

        self.DropWinF = DropWin.get()
        self.SignF = Sign.get()

        if self.DropWinF <= 0:
            self.clear()
            self.Static_ui_check()
            labelExcept5 = Label(self, text="Drop Window must be a positive", font='Arial 12', fg='red')
            labelExcept5.place(relx=.65, rely=.20)
        elif self.SignF <= 0:
            self.clear()
            self.Static_ui_check()
            labelExcept5 = Label(self, text="Number of Signals must be a positive", font='Arial 12', fg='red')
            labelExcept5.place(relx=.65, rely=.40)

        else:
            self.clear()
            self.Comp()



    def Dynamic_simulation_ui(self):
        DropWin = self.DropWin
        DThreshold = self.DThreshold
        DWindow = self.DWindow
        DSize = self.DSize

        try:
            DropWin.get()
        except:
            self.clear()
            self.Dynamic_ui_check()
            self.labelExcept6 = Label(self, text="Drop Window must be a integer", font='Arial 12', fg='red')
            self.labelExcept6.place(relx=.65, rely=.20)
        try:
            DThreshold.get()
        except:
            self.clear()
            self.Dynamic_ui_check()
            self.labelExcept7 = Label(self, text="Number of Signals must be a integer", font='Arial 12', fg='red')
            self.labelExcept7.place(relx=.65, rely=.40)
        try:
            DWindow.get()
        except:
            self.clear()
            self.Dynamic_ui_check()
            self.labelExcept7 = Label(self, text="Number of Signals must be a integer", font='Arial 12', fg='red')
            self.labelExcept7.place(relx=.65, rely=.60)

        try:
            DSize.get()
        except:
            self.clear()
            self.Dynamic_ui_check()
            self.labelExcept8 = Label(self, text="Stationary Data Size must be a integer", font='Arial 12', fg='red')
            self.labelExcept8.place(relx=.35, rely=.90)

        self.DropWinF = DropWin.get()
        self.DThresholdF = DThreshold.get()
        self.DWindowF = DWindow.get()
        self.DSizeF = DSize.get()

        if self.DropWinF <= 0:
            self.clear()
            self.Dynamic_ui_check()
            labelExcept5 = Label(self, text="Drop Window must be a positive", font='Arial 12', fg='red')
            labelExcept5.place(relx=.65, rely=.20)
        elif self.DWindowF <= 0:
            self.clear()
            self.Dynamic_ui_check()
            labelExcept5 = Label(self, text="Discrepancy Window must be a positive", font='Arial 12', fg='red')
            labelExcept5.place(relx=.65, rely=.60)
        elif self.DThresholdF <= 0:
            self.clear()
            self.Dynamic_ui_check()
            labelExcept5 = Label(self, text="Discrepancy Threshold must be a positive", font='Arial 12', fg='red')
            labelExcept5.place(relx=.65, rely=.40)
        elif self.DSizeF <= 0:
            self.clear()
            self.Dynamic_ui_check()
            labelExcept5 = Label(self, text="Stationary Data Size must be a positive", font='Arial 12', fg='red')
            labelExcept5.place(relx=.35, rely=.90)

        else:
            self.Comp()

    def Comp(self):
        if self.Flag1 == True:
            self.DepRate = [self.BulkRateF]*self.NumNodes
        else:
            self.DepRate = []
            a = len(self.dickF.keys())
            for i in range(a):
                self.DepRate.append(self.dickF.get(i))
        if self.Flag2 == True:
            self.MaxQueue = [self.BulkMaxF]*self.NumNodes
        else:
            a = len(self.deckF.keys())
            self.MaxQueue = []
            for i in range(a):
                self.MaxQueue.append(self.deckF.get(i))
        self.GoGoGo()



    def GoGoGo(self):
        self.clear()
        self.geometry('800x250')
        self.update()
        if self.isdynamik == True:
            go(lambd=self.ArrRate.get(), mus=self.DepRate, queue_lenghts = self.MaxQueue, drop_window = self.DropWinF, isdynamic = \
                    True, discrepancy = self.DThresholdF, dynamic_window = self.DWindowF, \
                    dynamic_after_stationary_number_of_samples = self.DSizeF, UI=self)
        else:
            go(lambd=self.ArrRate.get(), mus=self.DepRate, queue_lenghts=self.MaxQueue, drop_window=self.DropWinF,
               isdynamic=False, number_of_samples = self.SignF, UI=self)



    def UI_ST(self, Actual_Progress):
        self.clear()
        self.geometry('800x250')
        self.overrideredirect(False)
        self.update()

        self.mainLabel = Label(self, text='Simulation is in Progress', font='Arial 24')
        self.mainLabel.place(x = 50, y = 25)

        self.preProg = Label(self, text='Progress:', font='Arial 18')
        self.preProg.place(x = 50, y = 130)
        self.ProgLabal = Label(self, text=str(Actual_Progress)+'%', font='Arial 18')
        self.ProgLabal.place(x = 220, y = 130)
        self.update_idletasks()

    def UI_DM(self,stationary_list_per_node, iterator):
        self.clear()
        self.geometry(f'800x{self.Nodes * 25 + 140}')
        self.overrideredirect(False)
        self.update()
        self.mainLabel = Label(self, text='Simulation is in Progress', font='Arial 24')
        self.mainLabel.place(x=30, y=20)
        self.not_very_main_Label = Label(self, text='Events detected: '+str(iterator-1), font='Arial 14')
        self.not_very_main_Label.place(x = 30, y = 75)

        for i in range(len(stationary_list_per_node)):
            Bool=stationary_list_per_node[i]
            if Bool == True:
                color='green'
            else:
                color = 'red'
            pos=i*25+100
            Label(self, text=f'Discrepancy Node {i+1}:', font='Arial 14').place(x=30, y=pos)
            Label(self, text=str(Bool), font='Arial 14', fg=str(color)).place(x=320, y=pos)

        self.update_idletasks()


    def Finaly(self, iterator, simulation_duration, folder_path):
        self.clear()
        self.geometry('600x250')
        self.overrideredirect(True)
        self.Exit()
        self.But.place(rely=0, relx=0.964)
        self.update()
        self.Label_Fin1 = Label(self, text = 'Simulation Finished', font='Arial 24').place(x=30, y=20)
        self.Label_Fin1_5 = Label(self, text='Simulation finished successfully', font='Arial 14').place(x=30, y=80)
        self.Label_Fin2 = Label(self, text="Number of iterations: " + str(iterator),
                                font='Arial 14').place(x=30, y=120)
        self.Label_Fin3 = Label(self, text="Simulation duration: " + str(simulation_duration) + " seconds",
                                font='Arial 14').place(x=30, y=160)
        self.Label_Fin4 = Label(self, text='Results are saved in '+str(folder_path)+' folder', font='Arial 14').place(x=30, y=200)



    def Exit(self):
        self.But = Button(self, text='x', command=lambda: self.AppExit(), font='Arial 14')
        self.But.place(rely=0, relx=0.969)

    def clear(self):
        for i in self.winfo_children():
            i.destroy()


root = Zal()
root.mainloop()


