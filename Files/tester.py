class Animal:
    def __init__(self):
        print("Inside Init")
    def __str__(self):
        return "I am inside STR"
    
dog=Animal()
print(dog)
