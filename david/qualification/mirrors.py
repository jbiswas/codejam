def direction(p,q,r):
    "Cross-product between PQ and PR"
    pq = (q[0]-p[0], q[1]-p[1])
    pr = (r[0]-p[0], r[1]-p[1])
    return pq[0]*pr[1] - pq[1]*pr[0]

def onsegment(pi,pj,pk):
    if min(pi[0],pj[0]) <= pk[0] and \
       pk[0] <= max(pi[0],pj[0]) and \
       min(pi[1],pj[1]) <= pk[1] and \
       pk[1] <= max(pi[1],pj[1]):
        return True
    else:
        return False
       
def intersects(s,t):
    "Do segments s and t intersect, assuming no endpoint lies on a segment?"
    p1=s[0]; p2=s[1]; p3=t[0]; p4=t[1]
    d1 = direction(p3,p4,p1)
    d2 = direction(p3,p4,p2)
    d3 = direction(p1,p2,p3)
    d4 = direction(p1,p2,p4)
    if ((d1>0 and d2<0) or (d1<0 and d2>0)) \
           and ((d3>0 and d4<0) or (d3<0 and d4>0)):
        return True
    if d1==0 and onsegment(p3,p4,p1):
        return True
    if d2==0 and onsegment(p3,p4,p2):
        return True
    if d3==0 and onsegment(p1,p2,p3):
        return True
    if d4==0 and onsegment(p1,p2,p4):
        return True
    return False
    
def segmentsaround(p):
    x = p[0]
    y = p[1]
    corners = [(x-.5,y+.5),
               (x+.5,y+.5),
               (x+.5,y-.5),
               (x-.5,y-.5)]
    return [(corners[0],corners[1]),
            (corners[1],corners[2]),
            (corners[2],corners[3]),
            (corners[3],corners[0])]

def nextsquare(square,ray,orig):
    "Find next square traversed by ray coming from given side(s)"
    segs = segmentsaround(square)
    for side in range(4):
        if orig and side in orig:
            continue
        if intersects(segs[side], ray):
            if not (orig and (side+1)%4 in orig) and intersects(segs[(side+1)%4], ray):
                if side==0:
                    return [(square[0]+1, square[1]+1),(2,3)]
                if side==1:
                    return [(square[0]+1, square[1]-1),(0,3)]
                if side==2:
                    return [(square[0]-1, square[1]-1),(0,1)]
                return [(square[0]-1, square[1]+1),(1,2)]
            else:
                if side==0:
                    return [(square[0],square[1]+1),(2,)]
                if side==1:
                    return [(square[0]+1, square[1]),(3,)]
                if side==2:
                    return [(square[0],square[1]-1),(0,)]
                return [(square[0]-1,square[1]), (1,)]

def adjacent(sq1,sq2):
    return sq1[0]==sq2[0] or sq1[1]==sq2[1]

def path(orig,dest):
    ray = (orig,dest)
    yield orig
    nextsq = nextsquare(orig,ray,None)
    while nextsq[0] != dest:
        yield nextsq[0]
        nextsq = nextsquare(nextsq[0],ray,nextsq[1])
    yield dest

def c_reflect_around(center, point):
    return (2*center[0]-point[0], 2*center[1]-point[1])

def m_reflect_around(segment, point):
    if (segment[0][0] == segment[1][0]):
        return (2*segment[0][0]-point[0], point[1])
    else:
        return (point[0], 2*segment[0][1]-point[1])
    
def centerof(p1,p2):
    return ((p1[0]+p2[0])/2.,(p1[1]+p2[1])/2.)

def common_segment(sq1, sq2):
    if (sq1[0] == sq2[0]):
        return ((sq1[0]-.5,(sq1[1]+sq2[1])/2.),(sq1[0]+.5,(sq1[1]+sq2[1])/2.))
    else:
        return (((sq1[0]+sq2[0])/2., sq1[1]-.5),((sq1[0]+sq2[0])/2., sq1[1]+.5))
    
def isreflection(orig,dest,mirrors):
    this_path = path(orig,dest)
    old_square = orig
    x = orig
    new_square = this_path.next()
    has_hit_mirror = False
    while True:
        print new_square
        if new_square in mirrors:
            has_hit_mirror = True
            if not adjacent(new_square, old_square):
                if not (old_square[0],new_square[1]) in mirrors and \
                   not (old_square[1],new_square[0]) in mirrors:
                    return False
                if (old_square[0],new_square[1]) in mirrors and \
                   (old_square[1],new_square[0]) in mirrors:
                   dest = c_reflect_around(centerof(old_square,new_square),dest)
                   orig = c_reflect_around(centerof(old_square,new_square),orig)
                elif (old_square[0],new_square[1]) in mirrors:
                    dest = m_reflect_around(common_segment(old_square,(old_square[0],new_square[1])), dest)
                    orig = m_reflect_around(common_segment(old_square,(old_square[0],new_square[1])), orig)
                elif (old_square[1],new_square[0]) in mirrors:
                    dest = m_reflect_around(common_segment(old_square,(old_square[1],new_square[0])), dest)
                    orig = m_reflect_around(common_segment(old_square,(old_square[1],new_square[0])), orig)
            else:
                dest = m_reflect_around(common_segment(old_square, new_square), dest)
                orig = m_reflect_around(common_segment(old_square, new_square), orig)
            this_path = path(orig,dest)
            while this_path.next() != new_square:
                pass
        try:
            old_square = new_square
            new_square = path.next()
        except:
            if old_square == x:
                return True
            else:
                return False
                
