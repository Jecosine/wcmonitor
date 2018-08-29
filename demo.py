import itchat
import thread,os
from itchat.content import TEXT
from qrcode import printQR as pqr
import cv2
from PIL import Image

def get_snapshot():
    capture = cv2.VideoCapture(0)
    _, frame = capture.read()
    cv2.imwrite('snap.jpg',frame)


@itchat.msg_register(TEXT,)
def text_reply(msg):
    if msg.user.UserName == "filehelper":
        print msg.Text
        if "snapshot" in msg.Text:
            try:
                get_snapshot()
                im = open('snap.jpg','rb')
            except:
                msg.user.send("Fail to get snap")
            else:
                msg.user.send_image(im)
            im.close()
        else:
            msg.user.send("asdasdad")
    #auth = itchat.search_friends(nickName = 'MJ')[0]
    #auth.send("reply alter")
    #return "balala"

os.system("rm /home/pi/QR.png")
thread.start_new_thread(pqr,())
itchat.auto_login()


itchat.run()
