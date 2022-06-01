class ContactList:



    def __init__(self, test):
        self.label = test
        self.list_name = []

    def add_contact(self, contact_name, phone_number):
        self.list_name.append({"name":contact_name, "number":phone_number})
        self.list_name = sorted(self.list_name, key = lambda x : x["name"])
    
    def remove_contact(self, contact_name):
        for x in range(0, len(self.list_name)):
            if self.list_name[x]["name"] == contact_name:
                del self.list_name[x]
                break
    
    def find_shared_contact(self, ContactList):
        contacts_in_common = []
        for i in range(0, len(ContactList.list_name)):
            for x in range(0, len(self.list_name)):
                if ContactList.list_name[i]["name"] == self.list_name[x]["name"] and ContactList.list_name[i]["number"] == self.list_name[x]["number"]:
                    contacts_in_common.append(ContactList.list_name[i])
        return contacts_in_common
            
    
work_friends = ContactList("work_buddies")
work_friends.add_contact("Bob", "153-5321")
work_friends.add_contact("Addison", "341-9402")
# Begins making the second contact list
real_friends = ContactList("true_friends")
real_friends.add_contact("Jakob", "734-9021")
real_friends.add_contact("Addison", "341-9402")
# print(work_friends.list_name)
# work_friends.remove_contact("Bob")
# print(work_friends.list_name)
print(f"{real_friends.label} {real_friends.list_name}," f"\n{work_friends.label} {work_friends.list_name}")
print(f"On both list {real_friends.find_shared_contact(work_friends)}")

