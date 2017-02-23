class Line:
    def __init__(self):
        self.inSrf = -1
        self.cIndex = [] #the i,j,k in cells[]
        self.pts = [] #the actual points
    
    def clear(self):
        self.index = -1

genVtc = len(cells)
genRing = len(cells[0])
div = len(cells[0][0])

lines = []

for i in range(genVtc):
    for j in range(genRing):
        for k in range(div):
            cells[i][j][k].clear()

for i in range(genVtc):
    lineVtc = []
    lineID = 0
    for j in range(1, genRing):
        for k in range(div):
            now = cells[i][j][k]
            if now.state == flip:
                beforeDiv = now.adj[pos]
                before = cells[i][j-1][beforeDiv]
                if before.state == flip:
                    if before.inLine == -1:
                        line = Line()
                        line.cIndex.append([i, j-1, beforeDiv])
                        line.cIndex.append([i, j, k])
                        line.pts.append(pts[i][j-1][beforeDiv])
                        line.pts.append(pts[i][j][k])
                        now.inLine = lineID
                        before.inLine = lineID
                        lineVtc.append(line)
                        lineID += 1
                    else:
                        lineVtc[before.inLine].cIndex.append([i,j,k])
                        lineVtc[before.inLine].pts.append(pts[i][j][k])
                        now.inLine = before.inLine
    lines.append(lineVtc)

srfs = []
srfID = 0

for i in range(genVtc):
    for j in range(len(lines[i])):
        lines[i][j].clear()

for i in range(1, genVtc):
    for j in range(len(lines[i])):
        line = lines[i][j]
        si = line.cIndex[0] #si = the index of the cell that is at the start of the line
        start = cells[si[0]][si[1]][si[2]]
        srf = []
        if si[1] < genRing - 2:
            cellBefore = cells[i-1][si[1]+1][si[2]]
            lineBefore = lines[i-1][cellBefore.inLine]
            if lineBefore.inSrf == -1:
                srf.append([i-1, cellBefore.inLine])
                srf.append([i, j])
                lineBefore.inSrf = srfID
                line.inSrf = srfID
                srfs.append(srf)
                srfID += 1
            else:
                id = lineBefore.inSrf
                srfs[id].append([i, j])
                line.inSrf = id
