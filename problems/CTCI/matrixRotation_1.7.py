from math import cos, sin, pi

def matrixRotation(mat, angle=90):
    """
    itype : N*N mamtrix, angle is subset of {90,180,270,360}
    rtype: N*N matrix
    """
    def rotMat(angle):
        angle = angle/180 * pi
        return [
            [cos(angle), -sin(angle)], 
            [sin(angle), cos(angle)]
                ]
    
    rtmat = rotMat(90)
    for row in range(len(mat)):
        for col in range(row, len(mat[0])):
            
            mat[]
            