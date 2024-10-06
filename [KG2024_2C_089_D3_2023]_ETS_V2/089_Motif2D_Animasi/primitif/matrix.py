def zero_matrix3x3():
    return [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]

def identity_matrix():
    mtemp = zero_matrix3x3()
    for r in range(3):
        for c in range(3):
                mtemp[r][c] = int(r == c)              
    return mtemp
            
def mul_matrix3x3(ma, mb):
    mtemp = zero_matrix3x3() 
    for r in range(3):
        for c in range(3):
            mtemp[r][c] = (
                ma[r][0]*mb[0][c]
                + ma[r][1]*mb[1][c]
                + ma[r][2]*mb[2][c]
            )
    for r in range(3):
        for c in range(3):
            mb[r][c] = mtemp[r][c]        
    
    return mb