list =['everest','himalaya','fuji','kilimanjoro','blanc']
print(list[0].title())
print(list[-1])
message = ("The first mountain that i went to was " + list[1].title() +".")
print(message)
list[0] = 'rainier'
print(list)
list.append('bromo')
print(list)
list.insert(0,'everest')
print(list)
del list[-1]
print(list)
list.remove('fuji')
print(list)
x = list.pop(0)
print(list)
list.sort()
print(sorted(list))
list.sort(reverse=True)
print(list)
list.reverse()
print(list)
print(len(list))
