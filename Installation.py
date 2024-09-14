#https://www.python.org/downloads/ (#download version 3.11.9, )
#https://code.visualstudio.com/download (to write code IDE)
#https://docs.anaconda.com/anaconda/install/windows/ (For AIML)

#steps to update python
#Updating Python on Windows
#There are two simple ways to update your current Python version with the latest one. They are as follows: 
#
#Using the Python Installer
#Using the Windows Chocolatey Package Manager
#So let’s see how we can update the Python version with these two methods, one by one.
#
#Method 1: Python update on Windows using the Python Installer
#This method of updating the Python version will work whether Python is installed or not on your System.
#
#If Python is already installed on your system, you can check it using the Python -V command.
#
#Step 1: Download the Python installer from the Official Website of Python
#The easiest way to update the Python version is to download the latest version from the official website (https://www.python.org/downloads/)
#
#You can click on the Download Python 3.11.0 button, and it will download the latest compatible Python version for your system.
#
#Step 2: Install the Downloaded Python Installer
#After downloading the exe file, double-click on it to install Python.
#
#Step 3: Install Python
#Now, you can install the latest version of Python.
#
#Check the “Add python.ext to PATH”, then click on the “Install Now” button.
#
#This will start the installation process. 
#
#After processing, the latest version of Python will be installed on your system. 
#
#Click on the “Close” Button.
#
#Step 4: Verify the Update
#After successful installation, you can verify whether or not the latest version is installed on your system. To check the Python version, you can again run the same command, python -V, on the prompt command.
#
#Now, you can see that it is showing the latest installed version, i.e., Python 3.11.0.
#
#Note: If it still shows the old version, you may restart your system. Or uninstall the old version from the control panel.
#
#Method 2: Install Python using Command Line Only using the Chocolatey Package Manager
#Chocolatey is a Package Manager command line tool for Windows, and we can use it to install software for our Windows system. In our case, we can use it to install Python or update the current version of Python.
#
#Step 1 Open The Powershell as Administrator
#To install Chocolatey, you need to open PowerShell as Administrator.
#
#Step 2: Install the Chocolatey Package Manager Command
#Now, you can install the Chocolatey package manager using the following command.
#
#Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
# Copy
#
#Step 3: Verify the Chocolatey Installation
#Now, you need to check whether Chocolatey has been installed successfully. To check it, run the “choco” command.
#
#
#
#It is installed successfully because it is showing version Chocolatey v1.2.0.
#
#Step 4: Update Python with Chocolatey
#With the help of the choco upgrade command, we can update our current Python version.
#
#choco upgrade python -y
# Copy
#
#
#
#Step 5: Verify the Version
#You can again check the latest installed Python version using the following command.
#
#python -V
#
