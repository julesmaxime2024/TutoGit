# Votre code SYMANTEC ANTIVIRUS
#VERSION AMELIORER BY MAX GIT
import os
import win32com.client
from datetime import datetime
d=datetime.now().strftime('%d-%m-%Y %H:%M')
outlook = win32com.client.Dispatch("Outlook.Application")
mail = outlook.CreateItem(0)
mail.To="j.maxime@premierbet.com;l.zagba@premierbet.com"
#mail.To = "jp.kouame@premierbet.com;g.khalife@editec.co;s.liyanage@premierbet.com;it_cameroun@premierbet.com"

# Définir le sujet
mail.Subject = " >> CAMEROUN  SYMANTEC ANTIVIRUS SCREENSHOT "  + d

# Définir le corps du mail
mail.Body = "Bonjour,\n\nVeuillez trouver ci-joint la capture symantec antivirus screenshort : " + d 
# Parcourir le dossier
dossier = r"\\192.168.20.11\data\AUTOSCRIPTv2\SYMANTEC\SYMANTEC ANTIVIRUS"
for fichier in os.listdir(dossier):
 chemin = os.path.join(dossier, fichier)
 mail.Attachments.Add(chemin)

#  send email
mail.Send()