# Pythons
These are some file IO and OO examples. 

Patients.py contains an importer class that interacts with Patients.txt and reads the data for each patient. Patients.txt has one line for evey patient, and is written in the following format, 'name, height, weight, age, year, month, day (of last appointment)'. 

The PatientsImporter class reads through each line, and puts the data in a more readable format. It figures out when the next appointment should be based on when the previous one was (appointments occur every 5 months), and determines how many days remain until the next appointment. If an appointment was scheduled for today, it updates patients.txt with the data from that days appointment, and resets the last appointment's date. Then the importer gives all this data to the Patients class.

The Patients class displays everything to the user. If the next appointment is in less than a month, it displays the number of days until the next appointment. The Patients class also sends out texts to remind patients of upcoming appointments (code for texts are currently commented so I don't text someone every time I test the program). It sends texts 10 days before, on the day before, and on the day of the appointment.

Patients.py has comments after every significant part of the program, that help explain how things work. I have a feeling the comments are a little too detailed, but if so that's an easy fix.