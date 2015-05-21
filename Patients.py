import datetime #Imports the datetime module we will use to determine what day it is, and do calculations involving dates
from twilio.rest import TwilioRestClient #imports Twilio, the api we will use to send reminders in the form of texts
date = datetime.date.today() #stores the current date under 'date'
print "Today is " + ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"][date.weekday()] + ", " + ["January","Fabruary","March","April","May","June","July","August","September","October","November","December"][date.month] + ' ' + str(date.day) + ', ' + str(date.year) #Displays today's date in a more readable format
class PatientsImporter: 
    def __init__(self,file): #When we call this function later, 'file' will be Patients.txt
        self.patients = [] #Makes a list for us to add each patients data to
        file = open(file) #Opens Patients.txt
        unread_lines = True #Makes fail-safe for the upcoming while loop
        lines = list() #A list to temporarily store the data in Patients.txt, in case we need to edit it later
        while unread_lines: #Rinse repeat
            line = str(file.readline()).upper() #Set the current line of Patients.txt to a string
            line = line.split(',') #Makes line a list, by using every section separated by a comma as a new element in that list
            if len(line) == 1: #determines if the while loop is finished
                unread_lines = False 
                break #ends the loop
            line = map((lambda s: s.strip()), line) #removes trailing spaces from the data from the current line
            self.name = line[0]   #stores the data gathered under the following variables
            self.height = line[1]
            self.weight = line[2]
            self.age = line[3]
            self.last_appointment = [int(line[4]),int(line[5]),int(line[6])] #stores the date in the form of a list
            self.next_appointment = datetime.date(self.last_appointment[0]+(self.last_appointment[1]+5)/12,(self.last_appointment[1]+5)%12,self.last_appointment[2]) #calculates the date of the next appointment and puts it in datetime format, so we can easily determine how many days are left before the next appointment
            self.until_next_appointment = self.next_appointment - date #calculates time remaining before next appointment
            if self.until_next_appointment.days <= 0: #determines if an unrecorded appointment should have occured
                print self.name + "'s appointment was today. Please enter the new data from todays appointment." #if so, stores the new data from that that days appointment in the following variables
                self.height = raw_input("What is " + self.name + "'s height now?")
                self.weight = raw_input("What is " + self.name + "'s weight now?")
                self.age = raw_input("What is " + self.name + "'s age now?")
                lines.append(self.name.title() + ", " + self.height + ", " + self.weight + ", " + self.age + ", " + str(self.next_appointment.year) + ", " + str(self.next_appointment.month) + ", " + str(self.next_appointment.day) + "\n") #adds the new data for Patients.txt to the lines list
                self.last_appointment = [self.next_appointment.year, self.next_appointment.month, self.next_appointment.day] #resets appointment dates
                self.next_appointment = datetime.date(self.last_appointment[0]+(self.last_appointment[1]+5)/12,(self.last_appointment[1]+5)%12,self.last_appointment[2]) 
                self.until_next_appointment = self.next_appointment - date
                self.patients.append(Patient(self.name,self.height,self.weight,self.age,self.last_appointment,self.next_appointment,self.until_next_appointment)) #adds new data to a list we will later give to the Patient class
            else: #determines if there is no new data to record
                lines.append(self.name.title() + ", " + self.height + ", " + self.weight + ", " + self.age + ", " + str(self.last_appointment[0]) + ", " + str(self.last_appointment[1]) + ", " + str(self.last_appointment[2]) + "\n") #adds the current line in patients.txt to a list in case Patients.txt needs to be edited
                self.patients.append(Patient(self.name,self.height,self.weight,self.age,self.last_appointment,self.next_appointment,self.until_next_appointment)) #adds data to the list we will give to patients.txt
        file.close() #closes Patients.txt
        file = open(file,"w") #resets whatever line of patients.txt the program was on so our edits don't change anything we don't want them to, and opens it in a way that lets it edit the file
        file.writelines(lines) #makes any necessary edits to patients.txt
class Patient:
    def __init__(self, name, height, weight, age, last_appointment, next_appointment, until_next_appointment):  #takes data that will be given by the importer class and stores it in the following variables
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        self.last_appointment = last_appointment
        self.next_appointment = next_appointment
        self.until_next_appointment = until_next_appointment
    def remind_patients(self): 
        account_sid = "AC2527e5cd9318823eeae67082fc8f0cfb" #sets up twilio to send texts
        auth_token = "1756bdc8319de713187a53a552e3b2a6"
        client = TwilioRestClient(account_sid, auth_token)
        if self.until_next_appointment.days == 10: #checks to see if the program needs to send a 10 day reminder
            #message = client.messages.create(to="NaN",from_="+14253183498",body="Reminder: " + self.name + ", your appointment is in " + str(self.until_next_appointment) + " days!")
            return "Reminder: " + self.name + "'s appointment is in " + str(self.until_next_appointment.days) + " days!" #sends the necessary reminder
        if self.until_next_appointment.days == 1: #checks to see if the program needs to send a 'tomorrow' reminder
            #message = client.messages.create(to = "NaN",from_ = "+14253183498",body = "Reminder: " + self.name + ", your appointment is tomorrow!") 
            return "Reminder: " + self.name + "'s appointment is tomorrow!" #sends the necessary reminder
        if self.until_next_appointment.days == 0: #checks to see if the appointment is today
            #message = client.messages.create(to="NaN",from_="+14253183498",body="Reminder: " + self.name + ", your appointment is today!") 
            return 'Reminder: ' + self.name + "'s appointment is today!" #sends the necessary reminder
    def __str__(self): #Tells the class how I want it to display the data
        info = "Name: "+str(self.name) + '\n' #the \n marks the end of a line, which would work like hitting enter if you were typing it
        info += "Height: "+str(self.height) + '\n'
        info += "Weight: "+str(self.weight) + '\n'
        info += "Age: "+str(self.age) + '\n'
        info += "Last appointment: "+str(self.last_appointment[0])+'-'+str(self.last_appointment[1])+'-'+str(self.last_appointment[2]) + '\n'
        if self.until_next_appointment.days < 31: #If the appointment occurs in less than a month, displays the number of days until the appointment when displaying the appointments date
            info += "Upcoming appointment: "+str(self.next_appointment) + " in " + str(self.until_next_appointment.days) + " days."
        else:
            info += "Upcoming appointment: "+str(self.next_appointment) #if the appointment is more than a month away, prints the date normally
        return info #outputs the multi-line string containing all the data we need to explain
patients = PatientsImporter("Patients.txt").patients #stores each patients' data in a list
for i in patients: #iterates through that list
    print i #prints it out the way we told the program to when defining __str__() in the Patient class
    print i.remind_patients() #determines what texts to send, and sends them