import rhinoscriptsyntax as rs

curves = []
temp = []
walls = []

"""
for i in lines:
    for line in i:
        print line
        curves.append(rs.AddCurve(line.pts))"""

for srf in srfs:
    forSrf = []
    for i in srf:
        crv = rs.AddCurve(lines[i[0]][i[1]].pts)
        curves.append(crv)
        forSrf.append(crv)
    bakeSrf = rs.AddLoftSrf(forSrf)
    walls.append(bakeSrf[0])
