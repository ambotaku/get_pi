def gospers_pi():
    q,r,t,n,i = 1,0,1,8,1
    while True:
        if n == (q*(675*i-216)+125*r)//(125*t):
            yield n
            q,r = 10*q,10*r-10*n*t
        else:
            q,r,t,i = i*(2*i-1)*q,3*(3*i+1)*(3*i+2)*((5*i-2)*q+r),3*(3*i+1)*(3*i+2)*t,i+1
        n = (q*(27*i-12)+5*r) // (5*t)
