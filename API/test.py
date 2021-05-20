import messanger

# Mobile number registered in way2sms website.
phone = '+263783481766'

# Password in way2sms website.
password = ''

# Receiver mobile number.
receiver = '+14529959578'

# Text message that you want to send
message = """Hey Donald Trump,
Can write a python program which can send free text messages
"""

messanger.send(phone, password, receiver, message)