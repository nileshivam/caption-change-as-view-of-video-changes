#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import http.client
import uuid
import json

class Microsoft_ASR():
    def __init__(self):
        self.sub_key = 'YOUR-KEY'
        self.token = None
        pass

    def get_speech_token(self):
        FetchTokenURI = "/sts/v1.0/issueToken"
        header = {'Ocp-Apim-Subscription-Key': self.sub_key}
        conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
        body = ""
        conn.request("POST", FetchTokenURI, body, header)
        response = conn.getresponse()
        str_data = response.read()
        conn.close()
        self.token = str_data
        return True

    def transcribe(self,speech_file):

        # Grab the token if we need it
        if self.token is None:
            print ("No Token... Getting one")
            self.get_speech_token()

        endpoint = 'https://speech.platform.bing.com/recognize'
        request_id = uuid.uuid4()
        # Params form Microsoft Example 
        params = {'scenarios': 'ulm',
                  'appid': 'D4D52672-91D7-4C74-8AD8-42B1D98141A5',
                  'locale': 'en-US',
                  'version': '3.0',
                  'format': 'json',
                  'instanceid': '565D69FF-E928-4B7E-87DA-9A750B96D9E3',
                  'requestid': uuid.uuid4(),
                  'device.os': 'linux'}
        content_type = "audio/wav; codec=""audio/pcm""; samplerate=16000"

        def stream_audio_file(speech_file, chunk_size=1024):
            with open(speech_file, 'rb') as f:
                while 1:
                    data = f.read(1024)
                    if not data:
                        break
                    yield data

        headers = {'Authorization': 'Bearer ' + str(self.token,'utf-8'), 
                   'Content-Type': content_type}
        resp = requests.post(endpoint, 
                            params=params, 
                            data=stream_audio_file(speech_file), 
                            headers=headers)
        val = json.loads(resp.text)
        if('results' not in val):
            return "",0
        return val["results"][0]["name"], val["results"][0]["confidence"]


def getCaption(my_audio):
    ms_asr = Microsoft_ASR()
    ms_asr.get_speech_token()
    text, confidence = ms_asr.transcribe(my_audio)
    return (text, confidence)
