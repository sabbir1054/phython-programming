class Phone:
    color='black'
    feature=['camera','water proof']
    def call(self):
        print("Ring Ring Ring")

    def sendSms(self,number,text):
        sms=f'sending...{text} to {number}'
        return sms


my_phone=Phone()
my_phone.call()
sms=my_phone.sendSms('01733205248','I missed to miss you')
print(sms)

