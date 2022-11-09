# mul 2 matrice
A=[]
r1=int(input("enter no. of rows"))
c1=int(input("enter no. of columns"))
print("enter elements")
for i in range(r1):
    row=[]
    for j in range(c1):
        row.append(int(input()))
    A.append(row)
        
print("matrix A is :")
for i in range(r1):
    for j in range(c1):
        print(A[i][j], end=" ")
    print()
    
B=[]
r2=int(input("enter no. of rows"))
c2=int(input("enter no. of colmns"))
print("ener elements")
for i in range(r2):
    row=[]
    for j in range(c2):
        row.append(int(input()))
    B.append(row)
        
print("matrix B is :")
for i in range(r2):
    for j in range(c2):
        print(B[i][j], end=" ")
    print()
    
rs=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            rs[i][j]+=A[i][j]*B[i][j]
print("resultant matrix is :")
print()
for r in rs:
    print(r)
        
