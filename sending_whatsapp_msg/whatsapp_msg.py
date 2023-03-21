#pip install pywhatkit
# pls ensure you install in the visual environment of the file
# create a vitual environment by typing in  python3 -m venv name_of_the_environment eg 'env'
# becox it hass many dependecies
#   +2349074827008
# we import
import time

# this is for individual message
import pywhatkit
phone_number = input("Enter phone number: ")
# pywhatkit.sendwhatmsg(phone_number, "test", 10, 00)
text = input("Enter a caption: ")
pywhatkit.sendwhatmsg(phone_number, text, 12, 7, )   #("phonenumber eg +234phoneno.", "message", Hour, minutes)


# for group messages
# import pywhatkit
# group_id = input("Enter phone Group id: ")
# group_msg = input("Enter group message: ")
# pywhatkit.sendwhatmsg_to_group(group_id, group_msg, 10, 30)