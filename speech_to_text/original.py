# in this project we will be working on a speech to text creation
# we will be working with assembly AI API

# audio file dormat 
# (1).mp3 
# (2).flac 
# (3).wav (is the standard for cd audio quality)this is easy to work in python bcox it has a buildin model

"""API is the acronym for Application 
Programming Interface, which is a software 
intermediary that allows two applications to 
talk to each other. Each time you use an app 
like Facebook, send an instant message, or 
check the weather on your phone, you're using an API."""


# we are having 4 main steps
#import request #our library for assembly AI
#upload
#poll
#save our

import requests
# import sys
#
# upload_endpoint = 'https://api.assemblyai.com/v2/upload'
#
#
# filename = sys.argv[1]
# def read_file(filename, chunk_size=5242880):
#     with open(filename, 'rb') as _file:
#         while True:
#             data = _file.read(chunk_size)
#             if not data:
#                 break
#             yield data
#
# headers = {'authorization': "YOUR-API-TOKEN"}   #the headers are use for authentication
# response = requests.post(upload_endpoint,
#                         headers=headers,
#                         data=read_file(filename))
#
# print(response.json())
#
# audio-url = response.json()['upload-url']
#
#
# #second step    our code will look like this
#
# import requests
# upload_endpoint = 'https://api.assemblyai.com/v2/upload'
# transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
#
# filename = sys.argv[1]
# def read_file(filename, chunk_size=5242880):
#     with open(filename, 'rb') as _file:
#         while True:
#             data = _file.read(chunk_size)
#             if not data:
#                 break
#             yield data
#
# headers = {'authorization': "YOUR-API-TOKEN"}   #the headers are use for authentication
# response = requests.post(upload_endpoint,
#                         headers=headers,
#                         data=read_file(filename))
#
# print(response.json())
#
# audio-url = response.json()['upload-url']
#
#
#
# json = { "audio_url": audio-url }
#
# response = requests.post(transcript_endpoint, json=json, headers=headers)
# print(response.json())

# then on our terminal run this code again
# "main.py output.wav"  #this is our recorded file  to get the response from assembly AI





#third step
# import requests
# upload_endpoint = 'https://api.assemblyai.com/v2/upload'
# transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
#
# headers = {'authorization': "YOUR-API-TOKEN"}  # the headers are use for authentication
#
# filename = sys.argv[1]
# def upload(filename):
#     def read_file(filename, chunk_size=5242880):
#         with open(filename, 'rb') as _file:
#             while True:
#                 data = _file.read(chunk_size)
#                 if not data:
#                     break
#                 yield data
#
#     upload_response = requests.post(upload_endpoint,
#                                     # we are actually doing a post request with header "upload_endpoint"
#                                     headers=headers,
#                                     data=read_file(filename))
#
#     audio_url = upload_response.json()['upload_url']
#     return audio_url
#
# def transcribe():
#     transcript_request =  { "audio_url": audio_url }
#
#     transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
#     job_id = transcript_response.json()['id']
#     return job_id
#
#
#
# audio_url = upload(filename)
# job_id = transcribe(audio_url)
#
# print(job_id)



#the fourth step
# here we create a pulling end point

import requests
upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"

headers = {'authorization': "YOUR-API-TOKEN"}  # the headers are use for authentication

filename = sys.argv[1]
def upload(filename):
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    upload_response = requests.post(upload_endpoint,
                                    # we are actually doing a post request with header "upload_endpoint"
                                    headers=headers,
                                    data=read_file(filename))

    audio_url = upload_response.json()['upload_url']
    return audio_url

def transcribe():
    transcript_request =  { "audio_url": audio_url }

    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
    job_id = transcript_response.json()['id']
    return job_id





#pull
def poll(transcript_id):
    polling_endpoint = transcript_endpoint + '/'  + transcript_id
    polling_response = requests.get(polling_endpoint, headers=headers)
    return polling_response.json()  #to see how the polling response looks like
#what we are concern here is the status from the result we get from assembly AI

#while status is pending

# we create a function to ask Assaembly ai if it ready or not
def get_transcription_result_url(audio_url):
    transcript_id = transcribe(audio_url)
    while True:
        data = poll(transcript_id)

        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data['error']

        print('Wating 30 seconds')
        time.sleep(30)




# data, error = get_transcription_result_url(audio_url)



# print(data)

#we run our file in the terminal and see the result
#if completed
#next we remove "data, error = get_transcription_result_url(audio_url) " down
# save our file

def save_transcript(audio_url, filename):
    data, error = get_transcription_result_url(audio_url)
    if data:
        text_filename = filename + ".txt"  #you can use any format of file you want
        with open(text_filename, "w") as f:
            f.write(data['text'])
        print('Transcription is saved')
    elif error:
        print("Error", error)

audio_url = upload(filename)
save_transcript(audio_url, filename)