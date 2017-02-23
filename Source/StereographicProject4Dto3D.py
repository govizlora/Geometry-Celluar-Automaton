import rhinoscriptsyntax as rs
import math

ptsOut = []

lGen = len(pts)
lRing = len(pts[0])
lDiv = len(pts[0][0])

for i in range(lGen):
    gen = []
    for j in range(lRing):
        ring = []
        for k in range(lDiv):
            x = pts[i][j][k][0]
            y = pts[i][j][k][1]
            z = pts[i][j][k][2]
            w = pts[i][j][k][3]
            
            amp = 0
            amp += x ** 2
            amp += y ** 2
            amp += z ** 2
            amp += w ** 2
            amp = math.sqrt(amp)
            
            x *= radius / amp
            y *= radius / amp
            z *= radius / amp
            w *= radius / amp
            
            x0 = x * radius / (radius - w)
            y0 = y * radius / (radius - w)
            z0 = z * radius / (radius - w)
            
            ring.append([x0, y0, z0])
        gen.append(ring)
    ptsOut.append(gen)
