#GUI and LINKING
import backend,sys
import PySimpleGUI as sg

FONT = "comic"
THEME = 'DarkBlack'

sg.theme(THEME)

# Making a fram layout to embrace the subject and body
emailAppFrame = [
    [sg.Text("Subject:",font = FONT),sg.Input(size = (58,0),key = "-subject-",font = FONT)],
    [sg.Text("Body:*",font = FONT)],
    [sg.Multiline(size = (64,18),key = "-body-",font = FONT)],
    
]

# making the app layout
emailAppLayout = [
    [sg.Text("",size = (63,0)),sg.Button(" _ ",disabled=True),sg.Button(" ≡ ",disabled=True),sg.Button(" X ")],
    [sg.Text('EMAIL Application\nDeveloped by Adwait Narayan Pradhan\n\nEnter all the fields for sending the email!\n-----------------------------',size = (67,0),font = FONT,justification='center')],
    [sg.Text("Sender Email Address*:   ",font = FONT),sg.Input(key = "-semail-",size = (46,0),font = FONT)],
    [sg.Text("Sender Email Password*:",font = FONT),sg.Input(key = "-spass-",size = (46,0),font = FONT,password_char="*")],
    [sg.Text("Reciever Email Address*:",font = FONT),sg.Input(key = "-remail-",size = (46,0),font = FONT)],
    [sg.Text("")],
    [sg.Frame(title="Contents",layout=emailAppFrame,font=FONT)],
    [sg.Text("*: Mandatory Fields."),sg.Text("",size = (17,0)),sg.Button("SEND",font = FONT,enable_events=True)]
]

mainWindow = sg.Window(title="EMAIL Application",layout = emailAppLayout,grab_anywhere=True,keep_on_top=True,no_titlebar=True,resizable=False)
                                    #Keeping the window on top of others and removing the title bar which removes the task bar icon
while True:
    
    event, values = mainWindow.read()
    # print(event)          #uncomment to debug for further development
    if event in ('Cancel',None):
        break
    elif event == " X ":
        mainWindow.close()
        sys.exit(0)
    elif event == "SEND":
        if values['-semail-'] != "" and values['-spass-'] != "" and values['-remail-'] != "":    #entry data check
            
            if values['-subject-'] == "":          #assign default to subject
                values['-subject-'] == "No Subject"

            result = backend.StartSending(values)   # results gets the value of None if the email is sent and exceptions gist if not sent
            # print(result)     #uncomment to debug for further development
            if result != None:
                sg.PopupAnnoying(f"An Error ocurred while connectting to the SMTP server.\nRecheck all the Fields and network condition.\nError was {result}",font = "22",keep_on_top=True)            
            else: 
                sg.PopupAnnoying("Mail has been sent. Thank you for using my service.",font = "22",auto_close=True,auto_close_duration=1.4,keep_on_top=True)
                
        else:
            sg.PopupAnnoying("Some files were left empty. Please Ensure that all the fields are Filled.",font = "22",keep_on_top=True)
