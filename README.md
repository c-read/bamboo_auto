# This is a Python/Selenium script to automate timesheet logging daily.

# NOTE : procedure works specifically for BambooHR

make sure to create email, password and login .txt files, with the paths specified in the .py script

# .bat file creation

1) open notepad and enter the following text:
"file path of python.exe" "file path of bamboo.py" pause

2) save with .bat extension

Double-clicking this file will now run the script.

# Windows Task Scheduler

1) For Windows machines, Open Windows Task Scheduler.

2) Follow the prompts and set a schedule for the task to be run, supplying the .bat file when prompted for a program script.

You should be good to go!
