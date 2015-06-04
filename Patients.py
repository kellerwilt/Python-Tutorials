import datetime 
from twilio.rest import TwilioRestClient 
today = datetime.date.today()
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
months = ["January", "Fabruary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print "Today is " + weekdays[today.weekday()] + ", " + months[today.month] + ' ' + str(today.day) + ', ' + str(today.year) 
class PatientsImporter: 
    def __init__(self, data): 
        self.patients = [] 
        file = open(data)
        unread_lines = True 
        lines = list() 
        while unread_lines: 
            line = file.readline().upper()
            line = line.split(',') 
            if len(line) == 1: 
                unread_lines = False 
                break 
            line = map((lambda s: s.strip()), line) 
            self.name = line[0]    
            self.height = line[1]
            self.weight = line[2]
            self.age = line[3]
            self.last_appointment = datetime.date(int(line[4]), int(line[5]), int(line[6]))
            self.next_appointment = self.last_appointment.replace(month = (self.last_appointment.month + 5) % 12)
            self.until_next_appointment = self.next_appointment - today 
            if self.until_next_appointment.days <= 0: 
                print self.name + "'s appointment was today. Please enter the new data from todays appointment." 
                self.height = raw_input("What is " + self.name + "'s height now?")
                self.weight = raw_input("What is " + self.name + "'s weight now?")
                self.age = raw_input("What is " + self.name + "'s age now?")
                lines.append(self.name.title() + ", " + self.height + ", " + self.weight + ", " + self.age + ", " + str(today.year) + ", " + str(today.month) + ", " + str(today.day) + "\n") 
                self.last_appointment = self.next_appointment
                self.next_appointment = self.last_appointment.replace(month = (self.last_appointment.month + 5) % 12, year = self.last_appointment.year + (self.last_appointment.month + 5) / 12)
                self.until_next_appointment = self.next_appointment - today
                self.patients.append(Patient(self.name, self.height, self.weight, self.age, self.last_appointment, self.next_appointment, self.until_next_appointment)) 
            else: 
                lines.append(self.name.title() + ", " + self.height + ", " + self.weight + ", " + self.age + ", " + str(self.last_appointment.year) + ", " + str(self.last_appointment.month) + ", " + str(self.last_appointment.day) + "\n") 
                self.patients.append(Patient(self.name, self.height, self.weight, self.age, self.last_appointment, self.next_appointment, self.until_next_appointment)) 
        file.close()
        file = open(data, "w")
        file.writelines(lines) 
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
        if self.until_next_appointment.days == 10: 
            #message = client.messages.create(to = "NaN", from_ = "+14253183498", body = "Reminder: " + self.name + ", your appointment is in " + str(self.until_next_appointment) + " days!")
            return "Reminder: " + self.name + "'s appointment is in " + str(self.until_next_appointment.days) + " days!" 
        if self.until_next_appointment.days == 1: 
            #message = client.messages.create(to = "NaN", from_ = "+14253183498", body = "Reminder: " + self.name + ", your appointment is tomorrow!") 
            return "Reminder: " + self.name + "'s appointment is tomorrow!" 
        if self.until_next_appointment.days == 0: 
            #message = client.messages.create(to = "NaN", from_ = "+14253183498", body = "Reminder: " + self.name + ", your appointment is today!") 
            return 'Reminder: ' + self.name + "'s appointment is today!" 
    def __str__(self): 
        info = "Name: " + str(self.name).title() + '\n'
        info += "Height: " + str(self.height) + '\n'
        info += "Weight: " + str(self.weight) + '\n'
        info += "Age: " + str(self.age) + '\n'
        info += "Last appointment: " + str(self.last_appointment.year) + '-' + str(self.last_appointment.month) + '-' + str(self.last_appointment.day) + '\n'
        if self.until_next_appointment.days < 31: 
            info += "Upcoming appointment: " + str(self.next_appointment) + " in " + str(self.until_next_appointment.days) + " days."
        else:
            info += "Upcoming appointment: " + str(self.next_appointment) 
        return info
patients = PatientsImporter("Patients.txt").patients 
for i in patients: 
    print i 
    print i.remind_patients() 