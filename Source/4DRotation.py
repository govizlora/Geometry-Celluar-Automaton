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
            x1 = pts[i][j][k][0]
            y1 = pts[i][j][k][1]
            z1 = pts[i][j][k][2]
            w1 = pts[i][j][k][3]
            vec = [x1,y1,z1,w1]
            angles = [XY, XZ, XW, YZ, YW, ZW]
            
            for l in range(len(angles)):
                
                angle = math.radians(angles[l])
                c = math.cos(angle)
                s = math.sin(angle)
                
                rotationMatrix = [
                [[c,s,0,0]  ,[-s,c,0,0] ,[0,0,1,0] ,[0,0,0,1]  ],
                [[c,0,-s,0] ,[0,1,0,0]  ,[s,0,c,0] ,[0,0,0,1]  ],
                [[c,0,0,s]  ,[0,1,0,0]  ,[0,0,1,0] ,[-s,0,0,c] ],
                [[1,0,0,0]  ,[0,c,s,0]  ,[0,-s,c,0],[0,0,0,1]  ],
                [[1,0,0,0]  ,[0,c,0,-s] ,[0,0,1,0] ,[0,s,0,c]  ],
                [[1,0,0,0]  ,[0,1,0,0]  ,[0,0,c,-s],[0,0,s,c]  ]
                ]
                
                matrix = rotationMatrix[l]
                
                newVec = []
                for m in range(4):#matrix
                    sum = 0
                    for n in range(4):#vec
                        sum += vec[n] * matrix[m][n]
                    newVec.append(sum)
                vec = newVec
            ring.append(vec)
        gen.append(ring)
    ptsOut.append(gen)
