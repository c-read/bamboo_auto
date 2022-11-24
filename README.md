# Python/Selenium script to automate timesheet logging

NOTE : procedure works specifically for BambooHR
The selenium package is required for Python. This can be obtained through npm:
npm install selenium
create the following files with the relevant credentials stored:
bambooe.txt - email
bamboop.txt - password
bamboologin.txt - login url ( ie. https://{company name}.bamboohr.com/login.php )
make sure to specify the paths in the .py script

# .bat file creation

1) open notepad and enter the following text:
"file path of python.exe" "file path of bamboo-auto.py" pause

2) save with .bat extension

Double-clicking this file will now run the script.

# Windows Task Scheduler

1) For Windows machines, Open Windows Task Scheduler.

2) Follow the prompts and set a schedule for the task to be run, supplying the .bat file when prompted for a program script.

You should be good to go!
