########################################################################################
#Created by Vigenswaran Bala                                                           #
#Purpose:Was cleaning my laptop and had more than 300+ files in my downloads folder    #
#        decided to write a simple program(which took me 2 whole days)to sort and move #
#        files under respective categories according to their extension.               #
# If you can do more with this code then awesome, Also dont't foget to have fun        #
########################################################################################

import os  # For working with folders
import webbrowser  # to opent the FileDirectory (check last line of program)
import winutils  #This is a built in function that enables the file transfer possible
import platform  #To get the user name from laptop
import tkinter as tk  #for opening the filedialog
from tkinter import filedialog

root=tk.Tk() # initializing the tkinter window
root=root.withdraw() #Removes the window from the screen, without destroying it. If not mentioned then a tkinter pop up with nothing inside it will be seen.

#To begin with the current working folder
initial_folder=os.getcwd()
initial_folder= os.listdir(initial_folder)

#This loop decides the DESTINATION
for files in initial_folder:
    print("Thanks for trying this out "+ platform.node()+ ", hope it helps")
    print("Read The README.txt before you proceed any futher and type ctrl+z and enter to terminate anytime you want or press cancel in file dialogue box " )
    user=(input("Type 1 or 2 and press ENTER from your keyboard-->>1(CUT) and 2(COPY)<<---->: "))
#To make sure user does not give wrong inputs and also to make sure the input is notempty string..try..except block is employed
    try:
        user=int(user)
        if ((user)>2) :
            print("Number is greater than 2, Try Again and Enter either 1 or 2")
            exit()
        elif(user<1):
            print("Number is less than 1, Try Again and Enter either 1 or 2")
            exit()
    except ValueError:
        print("Input is blank, Kindly Try again and type either 1 or 2")
        exit()

#FILE HANDLING
    open_file = os.chdir((filedialog.askdirectory(title="CHOOSE WHERE TO PLACE THE NEW FOLDER and PRESS ENTER ")))
    name=(input("Enter the name of the folder you wish to create and press ENTER(If you do not wish to create one, press only ENTER)-->: "))
    if name == "":
        destination= os.getcwd()
    else:#
        (os.mkdir(name))
        destination=os.chdir(name)
        destination=(os.getcwd())

    print("Creating Newfolder at-->>  "+ destination)
    print("Newfolder successfully created...Dattebayo")

    break

#Now to Select the SOURCE folder and FILES that user must transfer to DESTINATION
for files in initial_folder:
    sourcepath= filedialog.askopenfilenames(initialdir=os.getcwd(), title='Select the files you want to move',
    filetypes=(("JPG File", ".jpg"), ("PNG File", ".png"),("HEIC file","*.heic"),("Plain Text","*.txt"),("ZIP files","*.zip"),("RAR files",".rar"),
    ("XML","*.xml"), ("HTML","*.HTML"),("PDF","*.pdf"),("word documents","*.DOCX"),("MP3 files","*.mp3"),("Power point",".ppt"),("Excel/Sheets",".xls .xlsx"),
    ("MP4 files","*.mp4"),("Wav files","*.wav"),("Mov files","*.mov"),("Wmv files","*.wmv"),("Avi files","*.avi"),("FLV,F4v and SWF files","*.flv,*.f4v,*.swf"),
    ("Photoshop files",".PSD"),("MKV","*.mkv"),("M4A","*.m4a"),("FLAC","*.flac"),("AAC","*.aac"),("Windows files",".exe .bat .dbf .dif .eps .hqx .mdb"),
    ("Pictures",".bmp .TIF .png .jpg .heic .gif .jpeg"),("Song files","*.mp3 *.wav *.m4a *.flac *.aac *.aiff *.aac *.ogg *.wma *.alac .MIDI"),("Video files","*.mp4 *.mov *.wmv *.avi"),
    ("All Files", "*.*")))

#You can also include other extension for your own purpose or remove anything you don't require

#i denotes the files that user selects in filedialog
    for i in sourcepath:
        i=i.replace('/', '\\')#It is done as the source path returns the path seperated by'/' whereas the osdir returns '\' and winutils accepts only '\'

        #Based upon the decision the user gives at the first loop
        if(user ==1):
            winutils.move(i,destination)
        elif(user ==2):
            winutils.copy(i,destination)
        else:
            continue
    break

print("Thank You "+ platform.node()+", Sayanora!!")

webbrowser.open(destination)
