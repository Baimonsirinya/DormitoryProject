from tkinter import *
import csv

lst_numroom = ['100','101','102','103','104','105','106','107','108','109']
lst_name=['Jee','Baimon','Folk','Pookpik','Plai','Ooy','Oli','Bank','Lemon','New']
room_rate = 5000



lst_add = []


def number():
    global lst_numroom
    roomnum = str(myinput.get())
    if roomnum in lst_numroom:
        number = lst_numroom.index(roomnum)
        display.set("Your room number is {}\nYour Name : {}".format(roomnum,lst_name[number]))
    else:
        display.set("Please Try again")
        

def unit():
    def Cal():
        try:
            def calunit(unitelect,unitwater):      # พารามิเตอร์
                electric = unitelect * 7
                if unitwater <= 1:
                    water = unitwater * 50
                else:
                    water = unitwater * 20
                total_price = room_rate + water + electric
                return electric,water,total_price
            
            inputelec = eval(ent_elec.get())
            inputwater = eval(ent_water.get())
            loc_nr = lst_numroom.index(myinput.get())
            unit_elect,unit_water,sumunittotal = calunit(inputelec,inputwater)
            display2.set('Room rate = {} THB\nElectric = {:0.2f} THB\nWater = {:0.2f} THB\nTotal price = {} THB'.format(room_rate,unit_elect,unit_water,sumunittotal))
            lst_add.append(str(lst_numroom[loc_nr]))
            lst_add.append(str(unit_elect))
            lst_add.append(str(unit_water))
            lst_add.append(str(room_rate))
            filepath = 'DormitoryProgram.csv'
            with open(filepath,'a',encoding ='utf-8') as outfile:
                writer = csv.writer(outfile,lineterminator ='\n')
                writer.writerow(lst_add)
            lst_add.clear()
            mywin2.destroy()
        except Exception as e:
            print(e)
            mywin2.destroy()

    mywin2 = Tk()
    mywin2.title('Dormitory Calprogram')
    mywin2.minsize(400,200)
    mywin2.configure(background='#D3D3D3')
    lb_elec = Label(mywin2, text = 'Enter your electrical units',font = 'Helvetica 13 bold ',fg='#B22222',bg='#D3D3D3').grid(sticky=W,column=0,pady=10,padx =20,row=2,rowspan=2)
    ent_elec = Entry(mywin2,width=20)
    ent_elec.grid(column=1,pady=10,row=2,rowspan=2)
    lb_water = Label(mywin2, text = 'Enter your water units',font = 'Helvetica 13 bold ',fg='#B22222',bg='#D3D3D3').grid(row=4,sticky=W,column=0,pady=10,padx =20,rowspan=4)
    ent_water = Entry(mywin2,width=20)
    ent_water.grid(row=4,column=1,pady=10,rowspan=4)
    btOK = Button(mywin2,text='Next',command = Cal,width=10).grid(row=8,column=0,pady=60)
    btCancel = Button(mywin2,text = 'Cancel',command = mywin2.destroy,width=10).grid(row=8,column=1,pady=60)
    lbl2 = Label(mywin,textvariable = display2).grid(row=7,column=0,pady=20)
    mywin2.mainloop()


def finish():
    try:
        lst_write=['Sum Total']
        lst_write_net=['Net Total']
        filepath = 'DormitoryProgram.csv'
        with open(filepath,'r',encoding ='utf-8') as infile:
            read = csv.reader(infile)
            mylist = list(read)
        sum_elect = 0
        for loop in mylist:
            sum_elect += eval(loop[1])
        sum_water=0
        for loop in mylist:
            sum_water += eval(loop[2])
        sum_rr=0
        for loop in mylist:
            sum_rr += eval(loop[3])

        net_total = sum_elect + sum_water + sum_rr
        lst_write.append(sum_elect)
        lst_write.append(sum_water)
        lst_write.append(sum_rr)
        lst_write_net.append(net_total)
        filepath = 'DormitoryProgram.csv'
        with open(filepath,'a',encoding ='utf-8')as outfile:
            writer = csv.writer(outfile,lineterminator ='\n')
            writer.writerow(lst_write)
            writer.writerow(lst_write_net)
            
        mywin.destroy()
    except Exception as e:
        print('def finish',e)
        
    

if __name__== '__main__':
    mywin = Tk()
    mywin.title('Dormitory program')
    mywin.minsize(50,50)
    
    filepath = 'DormitoryProgram.csv'
    with open(filepath,'w',encoding ='utf-8')as outfile:
        writer = csv.writer(outfile,lineterminator ='\n')

    display2 = StringVar()
    myinput = StringVar()
    display = StringVar()

    
    lb = Label(mywin,text = 'Welcome to dormitory calculation program',font = 'Helvetica 13 bold ',fg ='#BA55D3').grid(padx=70,pady=5)
    lb_2 = Label(mywin,text = 'Please Enter your number room',font = 'Helvetica 13 bold',fg='#B22222').grid(row=2,padx=70,pady=5)
    
    ent_1 = Entry(mywin,textvariable = myinput,width=30).grid(row=3,padx=70,pady=5)
    


    bt_OK = Button(mywin,text = 'OK',command = number,width=15).grid(row=5,column=0,pady=5)
    btunits = Button(mywin,text = 'Calculation',command = unit,width=15,bg='#FFD700').grid(sticky=W,row=9,column=0,rowspan=9,pady=20,padx=50)
    bt_csv = Button(mywin,text = 'Finish',command = finish,width=15).grid(sticky=E,row=9,rowspan=9,pady=20,padx=50)
    lbl = Label(mywin,textvariable = display,font = 'Helvetica 10').grid(row=6,column=0,pady=20)
    mywin.mainloop()
