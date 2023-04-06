class student:
    crs='python' #memory is allocated once,#cls level data member
#obj creation for class ,
s1=student()
s2=student()
#adding instance data members
s1.sname='nandu'
s1.marks=45
print('stu name:',s1.sname)
print('stu marks:',s1.marks)
print('course',s1.crs)
