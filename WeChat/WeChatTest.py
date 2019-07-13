import itchat


@itchat.msg_register(itchat.content.TEXT)
def auto_reply(msg):
    return "halo (auto reply)"


itchat.auto_login(hotReload=True, enableCmdQR=2)
itchat.run()
