# Abstracja


class MailServer:
    def send_mail(self):
        self.__connect()
        self.__authenticate()
        self.__disconnect()

    def __connect(self):
        print("Connect")

    def __authenticate(self):
        print("Autenticate")

    def __disconnect(self):
        print("Disconnect")


m = MailServer()
m.send_mail()
