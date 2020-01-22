class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.people_greeted = []

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1
        if other_person not in self.people_greeted:
            self.people_greeted.append(other_person)

    def print_contact_info(self):
        print('{}s email: {} {}s phone number: {}'.format(self.name, self.email, self.name, self.phone))
    
    def add_friend(self, friends):
        self.friends.append(friends)

    def num_friends(self):
        print(len(self.friends))
    


sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
#Basics 1-6 
sonny.greet(jordan)
print(sonny.email, sonny.phone)
print(jordan.email, jordan.phone)
#Add a method #2

print(sonny.print_contact_info())

#Add an instance variable (friends)
jordan.friends.append(sonny)
sonny.friends.append(jordan)

#Add a add_friend method 
jordan.add_friend(sonny)
print(len(jordan.friends))

# #Add a num_friends method
print(jordan.num_friends())

