import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(email, target, passwd):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = email
    receiver_email = target
    password = passwd

    message = MIMEMultipart("alternative")
    message["Subject"] = "Rendez l'argent"
    message["From"] = email
    message["To"] = target

    corps = """\
Bonjour, \n
Rendez l'argent \n
Cordialement la SIGL 2021
 """
    msg = MIMEText(corps, "plain")
    message.attach(msg)
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    return True


def not_usefull():
    print("-------------------------------------------------")
    print("-                    WELCOME                    -")
    print("-               This is SPAM 3000               -")
    print("-      Si vous aussi vous voulez l'argent       -")
    print("-              SPAM 3000 IS FOR YOU             -")
    print("-------------------------------------------------")

if __name__ == "__main__":
    not_usefull()
    print("[STARTING]\n")
    default_mail = "rendlargent3000@gmail.com"
    default_pass = "money-money"
    default_target = input("Target's email : ")
    print("\n")
    print("Default Settings : email: " + default_mail + ", number of messages : 10")
    print("Message text : Bonjour, Rendez l'argent . Cordialement la SIGL 2021\n")
    print("Do you want default ?")
    inp = input("It will send the message 10 times to your target (Y/n) : ")
    if inp == "Y" or inp == "y" or inp == "":
        for i in range(10):
            send_email(default_mail, default_target, default_pass)
            print("-> " + str(i), end='\r')
        print("DEUS VULT")
        exit(0)
    else:
        number = input("How many spam do you want : ")
        print("\n")
        print("Si tu veux modifier le text, ouvre un editeur et tu va ligne 18.")
        print("wsh je vais pas tout faire pour toi non plus\n")
        go = input("Go ? (Y/n) : ")
        if go == "Y" or go == "y" or go == "":
            try:
                n = int(number)
                for i in range(n):
                    send_email(default_mail, default_target, default_pass)
                    print("-> " + str(i), end='\r')
                print("DEUS VULT")
                exit(0)
            except Exception as e:
                print(e)
                print("T'es sur que t'a mis un nombre et pas n'importe quoi ?")
                exit(0)
        else:
            print("Chicken")
            exit(0)
