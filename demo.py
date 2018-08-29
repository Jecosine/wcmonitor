import itchat
from itchat.content import TEXT
import 
@itchat.msg_register(TEXT)
def _(msg):
    print msg.fromUsername

itchat.auto_login()


itchat.run()
