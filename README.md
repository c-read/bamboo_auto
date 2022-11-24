# Python/Selenium script to automate timesheet logging

NOTE : procedure works specifically for BambooHR <br>
The selenium package is required for Python. This can be obtained through npm: <br>
  - npm install selenium <br> <br>
  create the following files with the relevant credentials stored: <br>
   - bambooe.txt - email <br>
   -  bamboop.txt - password <br>
   -  bamboologin.txt - login url ( ie. https://{company name}.bamboohr.com/login.php ) <br>
 - make sure to specify the paths in the .py script <br>
<br>
# .bat file creation

   open notepad and enter the following text:
"file path of python.exe" "file path of bamboo-auto.py" pause

   save with .bat extension

Double-clicking this file will now run the script.

# Windows Task Scheduler

   For Windows machines, Open Windows Task Scheduler.

   Follow the prompts and set a schedule for the task to be run, supplying the .bat file when prompted for a program script.

<br> 

You should be good to go!
