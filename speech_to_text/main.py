# in this project we will be working on a speech to text creation
# we will be working with assembly AI API

# audio file dormat 
# (1).mp3 
# (2).flac  #less compression format
# (3).wav # uncompressed file format
# (is the standard for cd audio quality)this is easy to work in python bcox it has a buildin model

"""API is the acronym for Application 
Programming Interface, which is a software 
intermediary that allows two applications to 
talk to each other. Each time you use an app 
like Facebook, send an instant message, or 
check the weather on your phone, you're using an API."""



# first step
from api_communication import *

import sys

filename = sys.argv[1]

audio_url = upload(filename)
save_transcript(audio_url, filename)

