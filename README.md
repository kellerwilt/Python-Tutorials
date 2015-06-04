# Python Tutorial
These are some file IO and OO examples. 


Patients.py contains an importer class that interacts with Patients.txt to retrieve the data for each patient. Lets start with the file we're reading the data from. `Patients.txt` has one line for every patient, containing several pieces of data for that patient, separated by commas, in the following format.


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
You can see, that it doesn't return `2015, 5, 26, 8, 55, 59, 205000`, or `May 26th, 2015`, and if you check the type, it's actually in datetime's own format. I wanted the program to display the date in a sentence, so in order to make it look nice, I can use the attributes of the variable we have assigned to the current date. `today.day` returns `26`, 
returns `5`, `today.year` returns `2015` and `today.weekday` returns `1`. For the week and month, we can use a list of all the months/weekdays, and get an element from that list using the data from `today.month` or `today.weekday` we can put together a string that displays the date the way a human would by doing something like this
```Python
print "Today is " + ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday",
"Sunday"][today.weekday()] + ", " + ["January","Fabruary","March","April","May",
"June","July","August","September","October","November","December"][date.month] + 
' ' + str(today.day) + ', ' + str(today.year)
```

which returns `Today is Tuesday, June 26, 2015 `

Next, the program, `Patients.py` contains 2 classes, `PatientsImporter` and `Patient`. 

The `PatientsImporter` class reads through each line, and puts the data in a more readable format. It then figures out when the next appointment should be based on when the previous one was (appointments occur every 5 months), and determines how many days remain until the next appointment. If an appointment was scheduled for the current day, it updates patients.txt with the data from that days appointment, and resets the last appointment's date. Then the importer gives all this data to the Patients class.

The `Patient` class displays everything to the user. If the next appointment is in less than a month, it displays the number of days until the next appointment. The `Patient` class also sends out texts to remind patients of upcoming appointments (code for texts are currently commented so I don't text someone every time I test the program). It sends texts 10 days before, on the day before, and on the day of the appointment.

Now let's go over how all this works.

Before anything else, we need to open `Patients.txt`. The syntax for this is `open(file, mode, buffering)`. The `file` argument is a string containing the file's address. The next argument, `mode`, determines what you are able to do with the file (read, write, etc.). By default it opens in read, which is all we need for now, so we can just make a variable, file, and set `file = open("Patients.txt")`.

To start reading the file, we will want to get each line into a string. We can do this using the `readline()` attribute on `file`. `.readline()` returns a line of the file in the form of a string. Every time you call this function, it moves to the next line, meaning `file.readline()` would return the first line of `file`, but calling it a second time would return the second line. So, we can just make a while loop and set `line = file.readline()` at the beginning of the the loop, to iterate through it line by line.

Now that we have the data for the first patient, we can start picking it apart and taking what we need. Most of this can be done for us using the `split()` function. Calling `split()` on a string, will turn it into a list containing all the different pieces separated by a given string (space by default), so `"thing1 thing2 thing3".split()` would return `["thing1", "thing2", "thing3"]`. All we have to do is call `line.split(',')`, and then set different variables to their corresponding elements in the list we get.

We can make our own datetime object in the format mentioned before, by setting a varible to `datetime.date(year, month, day)`. So to make the variable `last_appointment`, we declare it equal to `calling datetime.date()` on the appropriate elements of the list we made earlier with `line.split()`. Now We need to find when the next appointment should be, and how many days are left until then. 

To find the date of the next appointment, we need is to add 5 months to the date of the last appointment. Using the `.replace()` function from datetime, we can replace different values, without going through the whole process of making a datetime object again. We can use modulo to keep the month between 1 and 12. Python rounding down when working with integers can help us by changing the year when necessary. When we add `(last_appointment.month + 5) / 12` to the year, if the month plus 5 is less than 12, then deviding it by 12 will be less than one, and will be rounded down to 0, but if the result is more than 12, we end up changing the year by one.

```Python
next_appointment = last_appointment.replace(month = last_appointment.month + 5 % 12, year = 
last_appointment.year + (last_appointment.month + 5) / 12)
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
patients.append(Patient(self.name, self.height, self.weight, self.age, self.last_appointment, 
self.next_appointment, self.until_next_appointment))
```
Finally, we go through the list and print the data, and give any necessary reminders using a for loop
```Python
patients = PatientImporter("Patients.txt")
for i in patients:
    print i
    i.remind_patients()
