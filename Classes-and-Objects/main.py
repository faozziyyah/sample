class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, track, score):
        self.name = name
        self.age = age
        self.track = track
        self.score = score

    def change_name(self, new_name):
        self.name = new_name
        print(f"changed name to {new_name}")

    def change_age(self, new_age):
        try:
            new_age = int(new_age)
        except:
            print("failed to change age, invalid data type")
            raise Exception

        self.age = new_age
        print(f"changed age to {new_age}")

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
