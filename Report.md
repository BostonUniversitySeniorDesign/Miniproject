Authors: Jonathan Ngo U73460730 |  David Cocero Quintanilla U18754031
Measurement


Our goal was to use the wifi_scan.py script and the raspberry pi to observe the human traffic at lunch times across two days. We chose Sunday 9/12 and Tuesday 9/14 to take measurements since we wanted to observe any differences that could be seen on a weekday vs on the weekend. To keep consistency as high as possible, we chose the same central location and similar times on both days. 
For Sunday, we began at 1:25pm and took measurements over 6o minutes in 5-minute intervals. For Tuesday, we created a script to automate scanning and began at 1:00pm. We took measurements over 50 minutes in 2-minute intervals. 
We tried to keep the start time and intervals the same for the measurements but we couldn’t due to schedule conflicts and debugging issues. For each interval, we ran wifi_scan.py for a single loop and saved results in a JSON file. 


Analysis


After collecting the data we decided to plot it using the wifi_plot.py script provided for the assignment. However, we encountered several difficulties. First, we needed to install libraries like pandas and matplotlib. Once installed, we ran it but realized that the results were not what we expected. This is because wifi_scan.py was built to detect moving objects. One of its functions selected what to plot based on if the object was detected only a few times across 100 loops. Since our measurements were aimed at students sitting down and only ran for 1 loop, the number of moving objects was near zero. 
 The README.md was modified to change the deliverables a few days after we had already taken the measurements. As such, the python script did not really work for our purpose.
We finally decided creating a Matlab script to process our data. The script imported and decoded the JSON files and counted the number of devices encountered. We decided to plot the results in a bar graph to see the evolution of the number of people. 
We found out that the number of people on Sunday was more steady than on Tuesday, probably because on Tuesday there were students going to classes.
We were surprised that the number of devices connected to wifi was so little. We expected a large increase on Tuesday than from what we saw on Sunday. One reason that might explain this is that at each interval, we only ran wifi_scan.py for 1 loop. The Raspberry Pi may not have been able to detect every device.