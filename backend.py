import smtplib
import ssl


def StartSending(values: dict):
    # print("backend resieved raw data: ",values)                 #uncomment to debug for further development
    
    PORT = 465      #getting this port for ssl security
                    # Assigning the values to relevant holders
    sndrMail = values['-semail-']       
    sndrPass = values['-spass-']
    rcvrMail = values['-remail-']
    msg = "Subject: " + values['-subject-'] + "\n\n" + values['-body-']
    
    # print(f"viewing organized data.\nSenderA: {sndrMail} SenderP: {sndrPass} RecieverA: {rcvrMail} message: {msg}")        #uncomment to debug for further development
    
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com",PORT,context = context) as server:               #constructing the connection to the SMTP server
            
            try:
                server.login(sndrMail,sndrPass)                     #Starting the Connection and logging in 
                result = server.sendmail(sndrMail,rcvrMail,msg)     #send the mail
                # print("backend try block: ",result)
                
            except Exception as e:
                # print("backend except block error : ",values)                 #uncomment to debug for further development
                return e
            
            finally:
                server.quit()
    except Exception as e:
        return e