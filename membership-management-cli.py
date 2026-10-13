
from time import sleep 
from os import system,name
class Members:
    def __init__(self,first_name,last_name,id,status):
        self.first_name=first_name 
        self.last_name=last_name
        self.id=id 
        self.status=status
    def display(self):
        print('Displaying all members.....')
        sleep(1)
        print(f'First name : {self.first_name}')
        print(f'Last name  : {self.last_name}')
        print(f'ID         : {self.id}')
        print(f'Status     : {self.status}')
        print('-------------------------------')
        sleep(1)
    def show(self):
        f=self.first_name
        l=self.last_name
        d=self.id
        s=self.status
        return f,l,d,s
def clean():
    system('cls'if name=='nt'else 'clear')
    
def add_member():
    first_name=input('Enter first name  ')
    last_name=input('Enter last name  ')
    id=int(input('Enter ID  '))
    statuse=input('Enter status , or click enter:  ')
    if statuse:
        status1=statuse
    else:
        status1="inactive"
    return Members(first_name,last_name,id,status1)
all_members=[]
while True:
 print("Welcom to gym membership management ")
 print('Choose an action')
 print('1.Add new member\n2.Display all member\n3.Search for a member\n4.Exit')
 choice=input('Enter your choice:  ')
 if choice=='1':
    clean()
    new_member=add_member()
    all_members.append(new_member)
    sleep(2)
    print('Member added successfully....')
    clean()
    continue
 elif choice=='2':
     if all_members:
       for i in all_members:
          i.display()
          sleep(1)
     else :
         print('No members yet')
     sleep(5)
     clean()
     continue
 elif choice=='3':
     choice2=input('''Serch by: 
1.Membership ID
2.Membership Name
3.Status
Enter your choice:  ''')
     if choice2=='1':
         ID=input('Enter the membership ID to search:  ')
         if ID.isdigit():
          ID=int(ID)   
          clean()
          sleep(1)
          check=True
          for i in all_members:
             [f,l,d,s]=i.show()
             if ID ==d:
                 i.display()
                 sleep(1) 
                 check=False
         if check:
                      print('No membership with this ID ')
         else:
             print('INvaild input ......')
             sleep(1)
             continue
         clean()
         continue        
     elif choice2=='2':
         NAME=input('Enter the membership NAME to search:  ')
         sleep(1)
         clean()
         check=True
         for i in all_members:
             [f,l,d,s]=i.show()
             if NAME==f:
                 i.display()
                 sleep(1)
                 check=False
         if check:
                print('No membership with this NAME ')
         clean()
         continue
     elif choice2=='3':
          STATUS=input('Enter the membership STATUS to search:  ')
          sleep(1)
          clean()

          check=True
          for i in all_members:
            [f,l,d,s]=i.show()
            if STATUS==s:
             i.display()
             sleep(1) 
             check=False
          if check:
              print('No membership with this STATUS  ')
          clean()
          continue
     else:
          print('Invaild choice.......')
          sleep(1)
          continue
 elif choice=='4':
    print('Exiting..........')
    sleep(2)
    clean()
    break  
 else:
     print('Invaild choice .......')
     clean()
     continue 
           
                   
                 
                 