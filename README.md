# Python/Selenium script to automate timesheet logging

NOTE : procedure works specifically for BambooHR using Chrome <br>

# Installations

The selenium package is required for Python. This can be obtained through npm: <br>

  - npm install selenium <br> 
  <br>
  
Chrome Webdriver is also required and can be found (https://chromedriver.storage.googleapis.com/index.html?path=107.0.5304.62/). <br>
You made need to add this .exe file to your system path
  
 create the following files with the relevant credentials stored:
 
  - bambooe.txt - email
  - bamboop.txt - password
  - bamboologin.txt - login url ( ie. https://{company name}.bamboohr.com/login.php )
  - make sure to specify the paths in the .py script

# .bat file creation

  - open notepad and enter the following text:
"file path of python.exe" "file path of bamboo-auto.py" pause

  - save with .bat extension

Double-clicking this file will now run the script.

# Windows Task Scheduler

  - For Windows machines, Open Windows Task Scheduler.

  - Follow the prompts and set a schedule for the task to be run, supplying the .bat file when prompted for a program script.

<br> 

You should be good to go!
