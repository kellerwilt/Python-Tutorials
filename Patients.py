patient = open("Patients.txt")
import datetime
date = datetime.date.today()
print date
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
                        print 'Reminder: ' + name + "'s appointment is today!"
                    else:
                        print "Reminder: " + name + "'s appointment is tomorrow!"
                else:
                    print "Reminder: " + name + "'s appointment is in " + str(self.until_next_appointment.days) + " days!"
            else:
                print "Reminder: " + name + "'s appointment is in " + str(self.until_next_appointment.days) + " days!"
unread_lines = True
while(unread_lines):
    line = patient.readline().upper()
    if line == '':
        unread_lines = False
        break
    print line
    line=line.translate(None, ',')
    line=line.split()
    print line
    name = line[0]
    height = line[1]
    weight = line[2]
    age = line[3]
    last_appointment = [int(line[4]),int(line[5]),int(line[6])]
    if line[0] == 'GEORGE':
        george = Patients(name,height,weight,age,last_appointment,date)
    if line[0] == 'JACKSON':
        jackson = Patients(name,height,weight,age,last_appointment,date)
print george.name
print george.height
print george.weight
print george.age
print george.last_appointment
print george.next_appointment
print george.until_next_appointment.days
george.remind_patients()
#print jackson.name
#print jackson.height
#print jackson.weight
#print jackson.age
#print jackson.last_appointment
#print jackson.next_appointment
#print jackson.until_next_appointment.days