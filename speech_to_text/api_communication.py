import requests # import  to pull the request library
from   api_secrets import API_KEY_ASSEMBYAI
import time



# second step (uploading)
upload_endpoint = "https://api.assemblyai.com/v2/upload"
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"

headers = {'authorization': API_KEY_ASSEMBYAI}  #set this to our API key #we are actually doing a post request with header



def upload(filename):
    def read_file(filename, chunk_size=5242880): #this is the read file function to read the data
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)   #Assembly AI requies our file to be in chuncks
                if not data:
                    break
                yield data

   
    upload_response = requests.post( upload_endpoint,          #we are actually doing a post request with header "upload_endpoint"
                            headers=headers,
                            data=read_file(filename))

    

    audio_url = upload_response.json()['upload_url']
    return audio_url


# third step (transcribe)
def transcribe(audio_url):
    transcript_request = json = { "audio_url": audio_url }

    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
    # print(response.json())
    job_id = transcript_response.json()['id']
    return job_id




# print(transcript_id)  # if you get <Response [200]> that means everything is gong well


# fourth step (poll our request)
# first thing is to create a pulling end point
# polling
def poll(transcript_id):
    polling_endpoint = transcript_endpoint + '/'  + transcript_id
    polling_response = requests.get(polling_endpoint, headers=headers) 
    return polling_response.json()

# transcribe
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


# fifth step (save our file)
def save_transcript(audio_url, filename):
    data, error = get_transcription_result_url(audio_url)
    if data:
        text_filename = filename + ".txt"  #you can use any format of file you want
        with open(text_filename, "w") as f:
            f.write(data['text'])
        print('Transcription is saved')
    elif error:
        print("Error", error)
