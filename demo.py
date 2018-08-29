import itchat
import thread,os
from itchat.content import TEXT
from qrcode import printQR as pqr

@itchat.msg_register(TEXT)
def _(msg):
    print msg.fromUserName
    print msg
    print msg.user

os.system("rm /home/pi/QR.png")
thread.start_new_thread(pqr,())
itchat.auto_login()


itchat.run()
