# Pythons
These are some file IO and OO examples. 

Patients.py contains an importer class that interacts with Patients.txt and reads the data for each patient. Lets start with the file we're reading the data from. `Patients.txt` has one line for every patient, containing several pieces of data for that patient, separated by commas, in the following format.

| Patient Name | Height  | Weight  | age    | date of last appointment |
| :----------: | :-----: | :-----: | :----: | :----------------------: |
| First Name,  | Inches, | Pounds, | Years, | yyyy,mm,dd               |

Lets start with displaying the date, before we analyze and display all of our data.
We will need the `datetime` module to find todays date, and do any calculations involving time.
`datetime.now()` is a function of the `datetime` module, that returns the current date;  

`from datetime import datetime`

`today = datetime.datetime.now()`

`   today`

`=> datetime.datetime(2015, 5, 26, 8, 58, 29, 899000)`

You can see, that it doesn't return `2015, 5, 26, 8, 55, 59, 205000`, or `May 26th, 2015`, and if you check the type, it's actually in datetime's own format. I wanted the program to display the date in a sentence, so in order to make it look nice, I can use the attributes of the variable we have assigned to the current date. `today.day` returns `26`, `today.month` returns `5`, `today.year` returns `2015` and `today.weekday` returns `1`. For the week and month, we can use a list of all the months/weekdays, and get an element from that list using the data from `today.month` or `today.weekday` we can put together a string that displays the date the way a human would by doing something like this
`print "Today is " + ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"][today.weekday()] + ", " + ["January","Fabruary","March","April","May","June","July","August","September","October","November","December"][date.month] + ' ' + str(today.day) + ', ' + str(today.year)` which returns `Today is Tuesday, June 26, 2015` 

Next, the program, `Patients.py` contains 2 classes, `PatientsImporter` and `Patient`. 

The `PatientsImporter` class reads through each line, and puts the data in a more readable format. It then figures out when the next appointment should be based on when the previous one was (appointments occur every 5 months), and determines how many days remain until the next appointment. If an appointment was scheduled for the current day, it updates patients.txt with the data from that days appointment, and resets the last appointment's date. Then the importer gives all this data to the Patients class.

The `Patient` class displays everything to the user. If the next appointment is in less than a month, it displays the number of days until the next appointment. The `Patient` class also sends out texts to remind patients of upcoming appointments (code for texts are currently commented so I don't text someone every time I test the program). It sends texts 10 days before, on the day before, and on the day of the appointment.

Now let's go over how all this works.

Before anything else, we need to open `Patients.txt`. The syntax for this is `open(file, mode, buffering)`. The `file` argument is a string containing the file's address. The next argument, `mode`, determines what you are able to do with the file (read, write, etc.). By default it opens in read, which is all we need for now, so we can just make a variable, file, and set `file = open("Patients.txt")`.

To start reading the file, we will want to get each line into a string. We can do this using the `readline()` attribute on `file`. `.readline()` returns a line of the file in the form of a string. Every time you call this function, it moves to the next line, meaning `file.readline()` would return the first line of `file`, but calling it a second time would return the second line.

Now that we have the data for the first patient, we can start picking it apart and taking what we need. Most of this can be done for us using the `split()` function. Calling `split()` on a string, will turn it into a list containing all the different pieces sepparated by a given string (space by default), so `"thing1 thing2 thing3".split()` would return `["thing1", "thing2", "thing3"]`.

Lets start with the file we're reading. `Patients.txt` contains a set of patients, and data referring to those patients, in the format `name, height, weight, age, year, month, day (of last appointment)`

