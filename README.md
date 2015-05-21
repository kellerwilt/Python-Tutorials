# Pythons
These are some file IO and OO examples. 
Patients.py contains an importer class that interacts with Patients.txt and reads the data for each patient. Patients.txt has one line for evey patient, and is written in the format, 'patient name, height, weight, age, last appointment: yyyy,mm,dd'. 

The PatientsImporter class reads through each line, and puts the data in a more readable format. It figures out when the next appointment should be based on when the previous one (appointments occur every 5 months), and determines how many days remain until the next appointment. If an appointment was scheduled for today, it updates patients.txt with the data from that days appointment, including resetting the date of the last appointment to the current date. Then the importer gives all this data to the Patients class.

The Patients class displays everything to the user. If the next appointment is in less than a month, it displays the number of days until the next appointment. The Patients class also sends out texts to remind patients of upcoming appointments (code for texts are currently commented so I don't text someone every time I test the program). It sends texts 10 days before, on the day before, and on the day of the appointment.

I am currently working on adding comments that explain each step of the program, to make it easier to look at.