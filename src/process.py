# Class of process
class Process():
    def __init__(self, data):
        self.process = data["process"]
        self.weigth = data["weigth"]
        self.exec_time = 0
        self.block_time = 0
        self.block_list = data["block_list"]
