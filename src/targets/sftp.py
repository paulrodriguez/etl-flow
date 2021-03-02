class Sftp:
    '''
    sftp target to dump data
    '''
    def __init__(self, host,username, password, port=22, commands=[]):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.commands = commands

    def execute(self, payload):
        pass
