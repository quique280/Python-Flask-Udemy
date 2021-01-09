friends = {"Bob","Rolf","Anne"}
abroad = {"Bob","Anne"}

local_friends = friends.difference(abroad)

print(local_friends)
####################################################
local = {"Rolf"}
abroad = {"Bob","Anne"}

abroad_friends = local.union(abroad)

print(abroad_friends)

####################################################

art={"Bob","Jen","Rolf","Charlie"}
science={"Bob","Jen","Adam","Anne"}

both = art.intersection(science)
print(both)