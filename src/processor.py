import time
from process import Process
import json
import random

class Processor(): 
    
    def __init__(self,readiness):
        self.readiness = readiness
        self.blocked = []
        self.executed = []
        self.completed = []

    def execute(self):
        self.mapProcess();
        while len(self.readiness) != 0:
            tempReadiness = self.readiness
            self.processExecution(tempReadiness)                
            self.createReadiness()            
            time.sleep(2)
            
    def processExecution(self,tempReadiness):
        for item in tempReadiness:
            weigth = item.weigth                 
            if (weigth == 0):                    
                self.completeProcess(item)   
                return                    
            else:
                item = self.addExecTime(item)
                self.blockProcess(item)
                return

    def mapProcess(self):
        mapedProcess = []
        for item in self.readiness:
            item = Process(item)
            mapedProcess.append(item)
        self.readiness = mapedProcess    

    def printProcess(self,processList):
        mapedProcess = []
        for item in processList:
            item = json.dumps(item.__dict__)   
            mapedProcess.append(item) 
        print(mapedProcess)  

    def addExecTime(self,item):
        item.weigth = item.weigth - 1
        item.execTime = item.execTime + 1
        return item   

    def completeProcess(self,item):
        ind = self.readiness.index(item)
        processComplete = self.readiness.pop(ind)
        self.completed.append(processComplete)  

    def blockProcess(self,item):
        blockCriter = random.randrange(10)
        if (blockCriter >= 5):
            item.blockTime = item.blockTime + 1
            ind = self.readiness.index(item)
            blockedProcess = self.readiness.pop(ind)
            self.blocked.append(blockedProcess)             
        
    def createReadiness(self):
        self.logProcess()    
        self.readiness = self.readiness + self.blocked         
        self.blocked = []

    def logProcess(self):
        print("------------------------------------")
        print()
        print("Readiness process")
        self.printProcess(self.readiness)
        print()
        print("Blocked process")
        self.printProcess(self.blocked)    
        print()
        if(len(self.completed) != 0):
            print("Completed process")
            self.printProcess(self.completed) 
            print()    
        print("------------------------------------")