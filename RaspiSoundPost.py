import requests
import json
import pyaudio
import wave
from base64 import b64encode
import io
import numpy as np

API_URL = "https://cogear1.ibm-sound.com/IoT-SoundServer/api/model/classifyWAV"
Authorization = "Basic YWNvdXN0aWMucG9rQGdtYWlsLmNvbTpBY291c3RpY3BvazEyMw=="

#=========Recording Settings=========
form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 44100 # 44.1kHz sampling rate
chunk = 4096 # 2^12 samples for buffer
record_secs = 3 # seconds to record
dev_index = 2 # device index found by p.get_device_info_by_index(ii)
wav_output_filename = 'test_audio.wav' # name of .wav file
#=================================
#=========Record=============
audio = pyaudio.PyAudio() # create pyaudio instantiation
# create pyaudio stream
stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                            input_device_index = dev_index,input = True, \
                            frames_per_buffer=chunk)
print("recording")
frames = []

# loop through stream and append audio chunks to frame array
for ii in range(0,int((samp_rate/chunk)*record_secs)):
    data = stream.read(chunk)
    frames.append(data)

print("finished recording")

stream.stop_stream()

frame = np.frombuffer(b''.join(frames), dtype=np.uint16)

with io.BytesIO() as wave_buffer:
    with wave.open(wave_buffer, 'wb') as wave_file:
        wave_file.setnchannels(1)
        wave_file.setsampwidth(2)
        wave_file.setframerate(44100)
        wave_file.writeframes(frame.tostring())

    wave_data = wave_buffer.getvalue()

# print(b64encode(frame).decode('utf-8'))

# upload_data = {'wav': b64encode(frame).decode('utf-8'), 'modelName': 'Tap01'}
upload_data = {'modelName': 'AGV01'}
headers = {'Host': 'cogear1.ibm-sound.com', 'Authorization': Authorization}
r = requests.post(
    API_URL, 
    data = upload_data, 
    files = {'wav': ('test.wav', wave_data)},
    headers = headers
)
print(r.status_code, r.reason)
API_result = r.content
print(API_result)
predictions = API_result.classification.infill.rankedValues
