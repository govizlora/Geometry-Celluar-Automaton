import random
import copy

class Cell:
    def __init__(self):
        self.state = 0
        self.nextState = 0
        self.adj = 0
        self.case = 0
        self.age = 0
        self.inLine = -1
        
    def clear(self):
        self.inLine = -1
    
    def update(self, cells):
        self.case = 0
        for i in range(3):
            if cells[self.adj[i]].state == 1:
                self.case += pow(2, i)
        self.nextState = rule[self.case]
        
    def updateState(self):
        self.state = self.nextState
        self.age += 1

def makeRule():
    global rule
    binary = bin(ruleInt)
    binStr = str(binary)
    if len(binStr) < 10:
        for i in range(10 - len(binStr)):
            binStr = binStr[:2] + '0' + binStr[2:]
    
    for i in range(8):
        rule.append(int(binStr[9-i]))

def main():
    
    firstGen = []
    
    for i in range(div):
        cell = Cell()
        if i == 0:
            cell.adj = [div-1, i, i+1]
        elif i == div - 1:
            cell.adj = [i-1, i, 0]
        else:
            cell.adj = [i-1, i, i+1]
        cell.state = init[i]
        firstGen.append(cell)
    
    makeRule()
    
    cellGens = []
    curGen = firstGen
    cellGens.append(copy.deepcopy(curGen))
    
    for i in range(1, genRing + genVtc - 1):
        for cell in curGen:
            cell.update(curGen)
        for cell in curGen:
            cell.updateState()
        cellGens.append(copy.deepcopy(curGen))
    
    for i in range(genVtc):
        cellVtc = []
        for j in range(genRing):
            cellRing = []
            for k in range(div):
                cellRing.append(copy.deepcopy(cellGens[i+j][k]))
            cellVtc.append(cellRing)
        cellOut.append(cellVtc)

cellOut = []
rule = []
main()
