# Python Tutorial
These are some file IO and OO examples. 


[Patients.py](https://github.com/kellerwilt/Python-Tutorials/blob/master/Patients.py) contains an importer class that interacts with [Patients.txt](https://github.com/kellerwilt/Python-Tutorials/blob/master/Patients.txt) to retrieve the data for each patient. Lets start with the file we're reading the data from. `Patients.txt` has one line for every patient, containing several pieces of data for that patient, separated by commas, in the following format.


Patient Name | Height | Weight | age | Date of Last Appointment
:-: | :-: | :-: | :-: | :-:
_(first name)_ | _(inches)_ | _(pounds)_ | _(years)_ | _(yyyy,mm,dd)_
George,  | 72, | 187, | 38, | 2015, 05, 28
Jackson, | 73, | 210, | 35, | 2015, 03, 18
Jim, | 72, | 190, | 34, | 2015, 01, 30
Chuck, | 69, | 180, | 29, | 2015, 02, 24
Corey, | 68, | 230, | 31, | 2014, 04, 03

Lets start with displaying the date, before we analyze and display all of our data.
We will need the `datetime` module to find todays date, and do any calculations involving time.
`datetime.today()` is a function of the `datetime` module, that returns the current date:  

```Python
>>> from datetime import datetime

>>> today = datetime.today()

>>> today

datetime.datetime(2015, 5, 26, 8, 58, 29, 899000)
```
You can see, that it doesn't return `2015, 5, 26, 8, 55, 59, 205000`, or `May 26th, 2015`, and if you check the type, it's actually in datetime's own format. 

```Python
>>> type(today)

<type 'datetime.datetime'>
```

I wanted the program to display the date in a sentence, so in order to make it look nice, I can use the attributes of the variable we have assigned to the current date. 
```Python
>>> today.weekday()
1
>>> today.day
26
>>> today.year
2015
>>> today.weekday()
1
>>> today.month
5
```

As you can see `today.weekday()` doesn't return `'Tuesday'` and `today.month` doesn't return `'May'` months/weekdays, and get an element from that list using the data from `today.month` or `today.weekday` (we subtract one because start counting at 0).
```Python
>>> weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
>>> weekdays[today.weekday() - 1]
"Tuesday"

>>> months = ["January", "Fabruary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
>>> months[today.month - 1]
"May"
```
we can put together a string that displays the date the way a human would by doing something like this
```Python
print "Today is " + weekdays[today.weekday() - 1] + ", " + months[today.month - 1] + 
' ' + str(today.day) + ', ' + str(today.year)
```

which returns `Today is Tuesday, June 26, 2015 `

Next, the program, `Patients.py` contains 2 classes, `PatientsImporter` and `Patient`. 

The `PatientsImporter` class reads through each line, and puts the data in a more readable format. It then figures out when the next appointment should be based on when the previous one was (appointments occur every 5 months), and determines how many days remain until the next appointment. If an appointment was scheduled for the current day, it updates patients.txt with the data from that days appointment, and resets the last appointment's date. Then the importer gives all this data to the Patients class.

The `Patient` class displays everything to the user. If the next appointment is in less than a month, it displays the number of days until the next appointment. The `Patient` class also sends out texts to remind patients of upcoming appointments (code for texts are currently commented so I don't text someone every time I test the program). It sends texts 10 days before, on the day before, and on the day of the appointment.

Now let's go over how all this works.

Before anything else, we need to open `Patients.txt`. The syntax for this is `open(file, mode, buffering)`. The `file` argument is a string containing the file's address. The next argument, `mode`, determines what you are able to do with the file (read, write, etc.). By default it opens in read, which is all we need for now, so we can just make a variable, file, and set `file = open("Patients.txt")`.

To start reading the file, we will want to get each line into a string. We can do this using the `readline()` attribute on `file`. `.readline()` returns a line of the file in the form of a string. Every time you call this function, it moves to the next line, meaning that calling `file.readline()` once, would return the first line of `file`, but calling it a second time would return the second line. So, we can just make a while loop and set `line = file.readline()` at the beginning of the the loop, to iterate through it line by line.

Now that we have the data for the first patient, we can start picking it apart and taking what we need. Most of this can be done for us using the `split()` function. Calling `split()` on a string, will turn it into a list containing all the different pieces separated by a given string (space by default), so `"thing1 thing2 thing3".split()` would return `["thing1", "thing2", "thing3"]`. All we have to do is call `line.split(',')`, and then set different variables to their corresponding elements in the list we get.

We can make our own datetime object in the format mentioned before, by setting a varible to `datetime.date(year, month, day)`. So to make the variable `last_appointment`, we declare it equal to `calling datetime.date()` on the appropriate elements of the list we made earlier with `line.split()`. Now We need to find when the next appointment should be, and how many days are left until then. 

To find the date of the next appointment, we need is to add 5 months to the date of the last appointment. Using the `.replace()` function from datetime, we can replace different values, without going through the whole process of making a datetime object again. We can use modulo to keep the month between 1 and 12. Python rounding down when working with integers can help us by changing the year when necessary. When we add `(last_appointment.month + 5) / 12` to the year, if the month plus 5 is less than 12, then deviding it by 12 will be less than one, and will be rounded down to 0, but if the result is more than 12, we end up changing the year by one.

```Python
next_appointment = last_appointment.replace(month = last_appointment.month + 5 % 12, 
year = last_appointment.year + (last_appointment.month + 5) / 12)
```

Now all that's left is to find how many days are left until the next appointment. Using the default python library, this would be very difficult. We would have to setup something that tracks the number of days in each month, tracks which months would go by from appointment to appointment. Datetime however, can add and subtract dates quite easily, so simply by finding the current date, subtracted from the next appointment, and the attribute `.days` will give us what we need; 

```Python
until_next_appointment = (next_appointment - today).days
```

To organize all this information, we can make a list, and every time the program finishes gathering all the data for a patient, it adds it to the list as a Patient object. All our Patient class does here, is take all the data, and put it in a more presentable form. We need the Patients class to all the data as arguments:
```Python
class Patient:
    def __init__(self, name, height, weight, age, last_appointment, next_appointment, 
    until_next_appointment):
        self.name
        self.height
        self.weight
        self.age
        self.last_appointment
        self.next_appointment
        self.until_next_appointment
```
Then, back in the `PatientsImporter` class, we add an instance of `Patient` to our `patients` list:
```Python
patients.append(Patient(self.name, self.height, self.weight, self.age, 
self.last_appointment, self.next_appointment, self.until_next_appointment))
```
If you tried printing an instance of Patient, you would realize it doesn't exactly give you anything helpful. By default it should return something along the lines of `<__main__.Patient instance at 0x7fe5405dc050>`. To fix this, we can tell the computer what we want it to do when we call `print` on an instance of our class by defining '__str__()'
```
def __str__(self): 
        info = "Name: "+str(self.name).title() + '\n'
        info += "Height: "+str(self.height) + '\n'
        info += "Weight: "+str(self.weight) + '\n'
        info += "Age: "+str(self.age) + '\n'
        info += "Last appointment: " + str(self.last_appointment.year) + '-' + str(self.last_appointment.month) + '-' + str(self.last_appointment.day) + '\n'
        if self.until_next_appointment.days < 31: 
            info += "Upcoming appointment: " + str(self.next_appointment) + " in " + str(self.until_next_appointment.days) + " days."
        else:
            info += "Upcoming appointment: " + str(self.next_appointment) 
        return info
```
The reason there is a `'\n'` added to `info` every time we plug in a new variable, is `'\n'`, when put in a string, signifies the end of a line. Using `'\n'` we make info a multi-line string that we can return at the end.
Now, printing out an instance of `Patient` would return something like this
```
Name: Corey
Height: 68
Weight: 230
Age: 31
Last appointment: 2015-4-3
Upcoming appointment: 2015-09-03
```
Finally, we go through the list and print the data, and give any necessary reminders using a for loop


```Python
patients = PatientImporter("Patients.txt")
for i in patients:
    print i
    i.remind_patients()
```

All together, here's a summary of what the how the code works.

```Python
import datetime 
```
Imports the datetime module we will use to determine what day it is, and do calculations involving dates
___
```Python
from twilio.rest import TwilioRestClient 
```
imports Twilio, which is the api we will use to send reminders in the form of texts
___
```Python
date = datetime.date.today() 
```
stores the current date under 'date'
___
```Python
print "Today is " + ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][date.weekday()] + ", " + ["January", "Fabruary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][date.month] + ' ' + str(date.day) + ', ' + str(date.year) 
```
Displays today's date in a more readable format
___
```Python
class PatientsImporter: 
    def __init__(self, file): 
```
When we call this function later, 'file' will be Patients.txt
___
```Python
        self.patients = [] 
```
Makes a list for us to add each patients data to
___
```Python
        file = open(file) 
```
Opens Patients.txt
___
```Python
        unread_lines = True 
```
Makes a fail-safe for the upcoming while loop
___
```Python
        lines = list() 
```
Creates a list to temporarily store the data in Patients.txt, in case we need to edit it later
___
```Python
        while unread_lines: 
```
Rinse repeat
___
```Python
            line = str(file.readline()).upper() 
```
Set the current line of Patients.txt to a string
___
```Python
            line = line.split(',') 
```
Makes line a list, by using every section separated by a comma as a new element in that list
___
```Python
            if len(line) == 1: 
```
determines if the while loop is finished
___
```Python
                unread_lines = False 
                break 
```
ends the loop
___
```Python
            line = map((lambda s: s.strip()), line) 
```
removes trailing spaces from the data from the current line
___
```Python
            self.name = line[0]   
```
stores the data gathered under the following variables
___
```Python
            self.height = line[1]
            self.weight = line[2]
            self.age = line[3]
            self.last_appointment = [int(line[4]), int(line[5]), int(line[6])] 
```
stores the date in the form of a list
___
```Python
            self.next_appointment = datetime.date(self.last_appointment[0] + (self.last_appointment[1] + 5) / 12, (self.last_appointment[1] + 5) % 12, self.last_appointment[2]) 
```
calculates the date of the next appointment and puts it in datetime format, so we can easily determine how many days are left before the next appointment
___
```Python
            self.until_next_appointment = self.next_appointment - date
```
calculates time remaining before next appointment
___
```Python
            if self.until_next_appointment.days <= 0: 
```
determines if an unrecorded appointment should has occured
___
```Python
                print self.name + "'s appointment was today. Please enter the new data from todays appointment." 
```
if so, stores the new data from that that days appointment in the following variables
___
```Python
                self.height = raw_input("What is " + self.name + "'s height now?")
                self.weight = raw_input("What is " + self.name + "'s weight now?")
                self.age = raw_input("What is " + self.name + "'s age now?")
                lines.append(self.name.title() + ", " + self.height + ", " + self.weight + ", " + self.age + ", " + str(self.next_appointment.year) + ", " + str(self.next_appointment.month) + ", " + str(self.next_appointment.day) + "\n") 
```
adds the new data for Patients.txt to the lines list
___
```Python
                self.last_appointment = [self.next_appointment.year, self.next_appointment.month, self.next_appointment.day]
```
resets appointment dates
___
```Python
                self.next_appointment = datetime.date(self.last_appointment[0] + (self.last_appointment[1] + 5) / 12, (self.last_appointment[1] + 5) % 12, self.last_appointment[2]) 
                self.until_next_appointment = self.next_appointment - date
                self.patients.append(Patient(self.name, self.height, self.weight, self.age, self.last_appointment, self.next_appointment, self.until_next_appointment)) 
```
adds new data to a list we will later give to the Patient class
___
```Python
            else: 
```
determines if there is no new data to record
___
```Python
                lines.append(self.name.title() + ", " + self.height + ", " + self.weight + ", " + self.age + ", " + str(self.last_appointment[0]) + ", " + str(self.last_appointment[1]) + ", " + str(self.last_appointment[2]) + "\n") 
```
adds the current line in patients.txt to a list in case Patients.txt needs to be edited
___
```Python                
self.patients.append(Patient(self.name, self.height, self.weight, self.age, self.last_appointment, self.next_appointment, self.until_next_appointment)) 
```
adds data to the list we will give to patients.txt
___
```Python
        file.close() 
```
closes Patients.txt
___
```Python
        file = open(file, "w")
```
resets whatever line of patients.txt the program was on so our edits don't change anything we don't want them to, and opens it in a way that lets it edit the file
___
```Python
        file.writelines(lines) 
```
makes any necessary edits to patients.txt
___
```Python
class Patient:
    def __init__(self, name, height, weight, age, last_appointment, next_appointment, until_next_appointment):  
```
takes data that will be given by the importer class and stores it in the following variables
___
```Python
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        self.last_appointment = last_appointment
        self.next_appointment = next_appointment
        self.until_next_appointment = until_next_appointment
    def remind_patients(self): 
        account_sid = "AC2527e5cd9318823eeae67082fc8f0cfb" 
```
sets up twilio to send texts
___
```Python
        auth_token = "1756bdc8319de713187a53a552e3b2a6"
        client = TwilioRestClient(account_sid, auth_token)
        if self.until_next_appointment.days == 10: 
```
checks to see if the program needs to send a 10 day reminder
___
```Python
            message = client.messages.create(to = "+123456789", from_ = "+123456789", body = "Reminder: " + self.name + ", your appointment is in " + str(self.until_next_appointment) + " days!")
            return "Reminder: " + self.name + "'s appointment is in " + str(self.until_next_appointment.days) + " days!" 
```
sends the necessary reminder
___
```Python
        if self.until_next_appointment.days == 1: 
```
checks to see if the program needs to send a 'tomorrow' reminder
___
```Python
            message = client.messages.create(to = "+123456789", from_ = "+123456789", body = "Reminder: " + self.name + ", your appointment is tomorrow!") 
            return "Reminder: " + self.name + "'s appointment is tomorrow!" 
```
sends the necessary reminder
___
```Python
        if self.until_next_appointment.days == 0:
```
checks to see if the appointment is today
___
```Python
            message = client.messages.create(to = "+123456789", from_ = "+123456789", body = "Reminder: " + self.name + ", your appointment is today!") 
            return 'Reminder: ' + self.name + "'s appointment is today!" 
```
sends the necessary reminder
___
```Python
    def __str__(self): 
```
Tells the class how I want it to display the data when an instance of the class is `printed`
___
```Python
        info = "Name: " + str(self.name) + '\n' 
```
the `\n` marks the end of a line, which would work like hitting enter if you were typing it
___
```Python
        info += "Height: " + str(self.height) + '\n'
        info += "Weight: " + str(self.weight) + '\n'
        info += "Age: " + str(self.age) + '\n'
        info += "Last appointment: " + str(self.last_appointment[0]) + '-' + str(self.last_appointment[1]) + '-' + str(self.last_appointment[2]) + '\n'
        if self.until_next_appointment.days < 31: 
```
If the appointment occurs in less than a month, displays the number of days until the appointment when displaying the appointments date
___
```Python
            info += "Upcoming appointment: "+str(self.next_appointment) + " in " + str(self.until_next_appointment.days) + " days."
        else:
            info += "Upcoming appointment: "+str(self.next_appointment) 
```
if the appointment is more than a month away, prints the date normally
___
```Python
        return info 
```
outputs the multi-line string containing all the data we need to explain
___
```Python
patients = PatientsImporter("Patients.txt").patients 
```
stores the data for each patient in a list
___
```Python
for i in patients: 
```
iterates through that list
___
```Python
    print i 
```
prints it out the way we told the program to when defining `__str__()` in the Patient class
___
```Python
    print i.remind_patients() 
```
determines what texts to send, and sends them
___
