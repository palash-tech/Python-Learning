def welcome(name="Palash"):
    print("Welcome",name)
welcome()

def add(a,b=100):
    print(a+b)
add(5)
add(5,20)

def student(name,branch="AI&DS"):
    print(name,branch)
student("Palash")
student("Rahul","CSE")