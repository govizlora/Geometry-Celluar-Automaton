import rhinoscriptsyntax as rs
import math

pts = []

altitude = []
azimuth = []

altInterval = (math.pi / 2) / ring
aziInterval = 2 * math.pi / div

for i in range(1, ring+1):
    altitude.append(math.pi / 2 - altInterval * i)

for i in range(div):
    azimuth.append(aziInterval * i)

for i in range(1, vtc+1):
    r = length
    ptsVtc = []
    for j in range(ring):
        ptsRing = []
        for k in range(div):
            x = r * math.cos(azimuth[k]) * math.sin(altitude[j])
            y = r * math.sin(azimuth[k]) * math.sin(altitude[j])
            z = r * math.cos(altitude[j])
            w = r * i
            ptsRing.append((x,y,z,w))
        ptsVtc.append(ptsRing)
    pts.append(ptsVtc)
