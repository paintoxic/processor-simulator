import time
from process import Process
import json
import random
from colorama import Fore, init


class Processor():
    def __init__(self, readiness):
        self.readiness = readiness
        self.blocked = []
        self.executed = []
        self.completed = []
        self.outfile = open('simulator.txt', 'w+')
        init()

    #Execute process and manipulate states, weigth and time execution
    def execute(self):
        self.mapProcess()
        while len(self.readiness) != 0:
            tempReadiness = self.readiness
            self.processExecution(tempReadiness)
            self.createReadiness()
            time.sleep(1)
        self.outfile.close()
        return True

    #Execute process create list of block or complete process
    def processExecution(self, tempReadiness):
        for item in tempReadiness:
            weigth = item.weigth
            if (weigth == 0):
                self.completeProcess(item)
                return
            else:
                item = self.addExecTime(item)
                self.blockProcess(item)
                return

    #Convert process give by user to Process obj that easer manipulate
    def mapProcess(self):
        mapedProcess = []
        for item in self.readiness:
            item = Process(item)
            mapedProcess.append(item)
        self.readiness = mapedProcess

    #Convert Process Obj to JSON Objs and print
    def printProcess(self, processList):
        textItem = ""
        for item in processList:
            textItem += "| PID : " + str(item.process) + " | WEIGTH : " + str(
                item.weigth) + " | EXEC TIME : " + str(
                    item.exec_time) + " | BLOCK TIME : " + str(
                        item.block_time) + " |"
            textItem += "\n"
        return textItem if (textItem != "") else "Vacio"

    #Reduce weigth of process and increases exec time
    def addExecTime(self, item):
        item.weigth = item.weigth - 1
        item.exec_time = item.exec_time + 1
        return item

    #Add process to complete list when this its completed, and remove process of readiness list
    def completeProcess(self, item):
        ind = self.readiness.index(item)
        processComplete = self.readiness.pop(ind)
        self.completed.append(processComplete)

    #Create a random number to determine if a process pass to block
    #If block process : Remove this of readiness list
    def blockProcess(self, item):
        blocked = item.exec_time in item.block_list
        if (blocked):
            item.block_time = item.block_time + 1
            ind = self.readiness.index(item)
            blockedProcess = self.readiness.pop(ind)
            self.blocked.append(blockedProcess)

    #Create readiness list from concat blocked list and actual readiness list
    def createReadiness(self):
        self.logProcess()
        self.readiness = self.readiness + self.blocked
        self.blocked = []

    #Logging
    def logProcess(self):
        print(Fore.LIGHTGREEN_EX + "------------------------------------")
        print(Fore.BLUE + "Readiness process")
        print(self.printProcess(self.readiness))
        print(Fore.RED + "Blocked process")
        print(self.printProcess(self.blocked))
        if (len(self.completed) != 0):
            print(Fore.GREEN + "Completed process")
            print(self.printProcess(self.completed))
        print(Fore.LIGHTGREEN_EX + "------------------------------------")
        self.logProcessToFile()

    def logProcessToFile(self):
        self.outfile.write("------------------------------------\n")
        self.outfile.write("Readiness process\n")
        self.outfile.write(str(self.printProcess(self.readiness)) + "\n")
        self.outfile.write("Blocked process\n")
        self.outfile.write(str(self.printProcess(self.blocked)) + "\n")
        if (len(self.completed) != 0):
            self.outfile.write("Completed process\n")
            self.outfile.write(str(self.printProcess(self.completed)) + "\n")
        self.outfile.write("------------------------------------\n")