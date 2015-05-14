patient = open("Patients.txt")
import datetime
date = datetime.date.today()
print "Today is " + ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"][date.weekday()] + ", " + ["January","Fabruary","March","April","May","June","July","August","September","October","November","December"][date.month] + ' ' + str(date.day) + ', ' + str(date.year)
class Patients:
    def __init__(self, name, height, weight, age, last_appointment,date):
        self.name = name
        self.height=height
        self.weight = weight
        self.age = age
        self.last_appointment = datetime.date(last_appointment[0],last_appointment[1],last_appointment[2])
        self.next_appointment = datetime.date(last_appointment[0]+(last_appointment[1]+5)/12,(last_appointment[1]+5)%12,last_appointment[2])
        self.until_next_appointment = self.next_appointment - date
    def remind_patients(self):
        if self.until_next_appointment.days < 10:
            if self.until_next_appointment.days < 5:
                if self.until_next_appointment.days < 2:
                    if self.until_next_appointment.days < 1:
                        print 'Reminder: ' + self.name + "'s appointment is today!"
                    else:
                        print "Reminder: " + self.name + "'s appointment is tomorrow!"
                else:
                    print "Reminder: " + self.name + "'s appointment is in " + str(self.until_next_appointment.days) + " days!"
            else:
                print "Reminder: " + self.name + "'s appointment is in " + str(self.until_next_appointment.days) + " days!"
    def info(self):
        print "Name: "+str(self.name)
        print "Height: "+str(self.height)
        print "Weight: "+str(self.weight)
        print "Age: "+str(self.age)
        print "Last appointment: "+str(self.last_appointment)
        if self.until_next_appointment.days < 31:
            print "Upcoming appointment: "+str(self.next_appointment) + " in " + str(self.until_next_appointment.days) + " days."
        else:
            print "Upcoming appointment: "+str(self.next_appointment)
unread_lines = True
while(unread_lines):
    line = patient.readline().upper()
    if line == '':
        unread_lines = False
        break
    line=line.translate(None, ',')
    line=line.split()
    name = line[0]
    height = line[1]
    weight = line[2]
    age = line[3]
    last_appointment = [int(line[4]),int(line[5]),int(line[6])]
    if line[0] == 'GEORGE':
        george = Patients(name,height,weight,age,last_appointment,date)
    if line[0] == 'JACKSON':
        jackson = Patients(name,height,weight,age,last_appointment,date)
    if line[0] == 'JIM':
        jim = Patients(name,height,weight,age,last_appointment,date)
    if line[0] == 'CHUCK':
        chuck = Patients(name,height,weight,age,last_appointment,date)
    if line[0] == 'COREY':
        corey = Patients(name,height,weight,age,last_appointment,date)
george.info()
george.remind_patients()
jackson.info()
jackson.remind_patients()
jim.info()
jim.remind_patients()
chuck.info()
chuck.remind_patients()
corey.info
corey.remind_patients()