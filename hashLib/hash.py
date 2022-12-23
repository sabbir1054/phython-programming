import hashlib
""" email="sabbir.com"
pwd="sabbir"

pwd_encode=pwd.encode()
pwd_hash=hashlib.md5(pwd_encode).hexdigest()
print(pwd_encode)
print(pwd_hash)
 """

email2="jhankermahabub@gmail.com"
email2pass="abudaby"
hased_pass=hashlib.md5(email2pass.encode()).hexdigest()
your_email="jhankermahabub@gmail.com"
your_pasword="abudaby"
your_hased_pass=hashlib.md5(your_pasword.encode()).hexdigest()
if email2==your_email and hased_pass==your_hased_pass:
    print("OK")
else:
    print("Not match")
