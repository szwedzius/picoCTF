#File used to test multiple values
import hashlib

username_trial = "ANDERSON"
bUsername_trial = b"ANDERSON"

print(hashlib.sha256(bUsername_trial).hexdigest())
#We see that the value of the hash is:
#31250184996c31741ab6ae8452c205deb7dbf431c5bdba21dea5f1289b646bfa

#Let's try to print the value that the key is checked with
values= [4,5,3,6,2,7,1,8]
hash = hashlib.sha256(bUsername_trial).hexdigest()
result = "".join(hash[i] for i in values)
#This is the value necessary to pass into the dynamic part of the key
print(result)