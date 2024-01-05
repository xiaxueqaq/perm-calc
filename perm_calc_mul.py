n=int(input("Under group S_?:"))
perm=[0]*100
def split(s):
    cnt=0
    s=s+' '
    l=-1
    lst=[]
    for i in range(0,len(s)):
        if (s[i]==' '):
            cnt=cnt+1
            lst.append(int(s[l+1:i]))
            l=i

    #print("split("+s+") with return=",lst)
    return lst

def get_ans():
    mapp=[0]*100
    vis=[0]*100
    for i in range(1,n+1):
        mapp[perm[i]]=i
    for i in range(1,n+1):
        if(vis[i]==0):
            pt=i
            print('(',end='')
            while(vis[pt]==0):
                vis[pt]=1
                if(vis[mapp[pt]]==0):
                    print(pt,end=' ')
                else:
                    print(pt,end='')

                pt=mapp[pt]
            print(')',end='')
    print()
def process(s):
    global perm
    l=0
    r=len(s)-1
    while(r>=0):
        l=r
        while(s[l]!='('):
            l=l-1
            ts=s[l+1:r]
        arg=split(ts)
        t=perm[arg[len(arg)-1]]
        i=len(arg)-2
        while (i>=0):
            perm[arg[i+1]]=perm[arg[i]]
            i=i-1
        perm[arg[0]]=t
        r=l-1
        '''
        print('After perm:',arg)
        get_ans()
        print()
        for i in range(1,n+1):
            print(perm[i],end=' ')
        print()
        '''

while(True):
    expr=input()
    if(expr=="break"):
        break
    perm=[0]*100
    for i in range(1,n+1):
        perm[i]=i

                
    process(expr)
    get_ans()            
