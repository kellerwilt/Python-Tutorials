patient = open("Patients.txt")
import datetime
from twilio.rest import TwilioRestClient
date = datetime.date.today()
print "Today is " + ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"][date.weekday()] + ", " + ["January","Fabruary","March","April","May","June","July","August","September","October","November","December"][date.month] + ' ' + str(date.day) + ', ' + str(date.year)
class PatientsImporter:
    def __init__(self,file):
        self.patients = []
        file = open(file)
        unread_lines = True
        while unread_lines:
            line = str(file.readline()).upper()
            line = line.split(',')
            if len(line) == 1:
                unread_lines = False
                break
            line = map((lambda s: s.strip()), line)
            self.name = line[0]
            self.height = line[1]
            self.weight = line[2]
            self.age = line[3]
            self.last_appointment = [int(line[4]),int(line[5]),int(line[6])]
            self.next_appointment = datetime.date(self.last_appointment[0]+(self.last_appointment[1]+5)/12,(self.last_appointment[1]+5)%12,self.last_appointment[2])
            self.until_next_appointment = self.next_appointment - date
            self.patients.append(Patient(self.name,self.height,self.weight,self.age,self.last_appointment,self.next_appointment,self.until_next_appointment))
class Patient:
    def __init__(self, name, height, weight, age, last_appointment, next_appointment, until_next_appointment):  
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        self.last_appointment = last_appointment
        self.next_appointment = next_appointment
        self.until_next_appointment = until_next_appointment
    def remind_patients(self):
        account_sid = "AC2527e5cd9318823eeae67082fc8f0cfb"
        auth_token = "1756bdc8319de713187a53a552e3b2a6"
        client = TwilioRestClient(account_sid, auth_token)
        if self.until_next_appointment.days < 10:
            if self.until_next_appointment.days < 2:
                if self.until_next_appointment.days < 1:
                    message = client.messages.create(to="+1testtesttestdontwantsendtext",from_="+14253183498",body="Reminder: " + self.name + ", your appointment is today!")
                    return 'Reminder: ' + self.name + "'s appointment is today!"
                else:
                    message = client.messages.create(to="+1testtesttestdontwantsendtext",from_="+14253183498",body="Reminder: " + self.name + ", your appointment is tomorrow!")
                    return "Reminder: " + self.name + "'s appointment is tomorrow!"
            else:
                message = client.messages.create(to="+1testtesttestdontwantsendtext",from_="+14253183498",body="Reminder: " + self.name + ", your appointment is in " + str(self.until_next_appointment) + " days!")
                return "Reminder: " + self.name + "'s appointment is in " + str(self.until_next_appointment.days) + " days!"
    def __str__(self):
        info = "Name: "+str(self.name) + '\n'
        info += "Height: "+str(self.height) + '\n'
        info += "Weight: "+str(self.weight) + '\n'
        info += "Age: "+str(self.age) + '\n'
        info += "Last appointment: "+str(self.last_appointment[0])+'-'+str(self.last_appointment[1])+'-'+str(self.last_appointment[2]) + '\n'
        if self.until_next_appointment.days < 31:
            info += "Upcoming appointment: "+str(self.next_appointment) + " in " + str(self.until_next_appointment.days) + " days."
        else:
            info += "Upcoming appointment: "+str(self.next_appointment)
        return info
patients = PatientsImporter("Patients.txt").patients
for i in patients:
    print i
    print i.remind_patients()