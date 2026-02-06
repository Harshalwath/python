#take marks of 3 subject and calculate :
#marks & percentage 

sub1 = int(input("Enter marks of sub1:"))
sub2 = int(input("Ente marks of sub2:"))
sub3 = int(input("Enter marks of sub3:"))

total = (sub1 + sub2 + sub3) 
percentage = (total/300 * 100)

print("total marks:" ,total)
print("percentage:" , percentage)
