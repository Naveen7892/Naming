#python 2
def naming_convention(str1):
    i,charType,count = 0,1,1
    length=len(str1)
    str2=''
    while(i<length):
        c=str1[i]
        if c in 'abcdefghijklmnopqrstuvwxyz':
            if charType==2 and count>2:
                str2+='_'
            str2+=c
            charType=1
            count=1
        elif c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if charType==1:
                str2+='_'
            str2+=c.lower()
            charType=2
            count+=1
        else:
            if charType!=3:
                str2+='_'
            str2+=c
            charType=3
        i+=1
    if str2[0]=='_':
        return str2[1:]
    else:
        return str2

print 'Fold3D-->',naming_convention('Fold3D')
print 'unfold45-->',naming_convention('unfold45')
print 'ClearType-->',naming_convention('ClearType')
print 'fold45CAM-->',naming_convention('fold45CAM')
print 'Fold3dCAM-->',naming_convention('Fold3dCAM')
print 'Ab1ABCabc123-->',naming_convention('Ab1ABCabc123')
print 'ABCabc123-->',naming_convention('ABCabc123')
print 'CAM3d-->',naming_convention('CAM3d')

raw_input('Print Any Key To Exit!')
