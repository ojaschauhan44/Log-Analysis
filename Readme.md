#LOG-ANALYSIS
 
Aim of this project is to print report based on data in database by using python.


Prerequisites:

->PostgreSQL

->Vagrant

->VirtualBox



How To Install

1.Install Vagrant and VirtualBox.

2.Download fullstack-nanodegree-vm repository.

3.Unzip this file after downloading it.

4.Now we got newsdata.sql in our vagrant directory and we are good to go.




How to run the virtual machine


1.Go to vagrant directory 

2.Run the vagrant on vm (vagrant up)

3.Login into vm (vagrant ssh)

4.Change directory to vagrant (cd vagrant)

5.Use command psql -d news -f newsdata.sql to load database

6.Use command python analysis.py to run the programm


Running the queries:

From the vagrant directory inside the virtual machine,run logs.py using:
  $ python3 logs.py
