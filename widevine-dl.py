#!/usr/bin/env python3

import os 
import subprocess
import shutil
import glob
import pathlib
import platform
import time

FILE_DIRECTORY=str(pathlib.Path(__file__).parent.absolute())
TEMPORARY_PATH = FILE_DIRECTORY+"/cache"
OUTPUT_PATH = FILE_DIRECTORY+"/output"

def osinfo():
	global PLATFORM
	if platform.system()== "Darwin":
		PLATFORM = "Mac"
	else:
		PLATFORM = platform.system()
		
def divider():
	print ('-' * shutil.get_terminal_size().columns)
	
def empty_folder(folder):
	files = glob.glob('%s/*'%folder)
	for f in files:
		os.remove(f)
	print("Emptied Temporary Files!")
	divider()
	quit()
	
def extract_key (prompt):
	global key,kid,keys
	key = prompt[30 : 62]
	kid = prompt[68 : 100]
	keys = "%s:%s"%(kid,key)
	return key,kid,keys

def download_drm_content(mpd_url):
	divider()
	print("Processing Video Info..")
	os.system('yt-dlp --external-downloader aria2c --no-warnings --allow-unplayable-formats --no-check-certificate -F "%s"'%mpd_url)
	divider()
	VIDEO_ID = input("ENTER VIDEO_ID (Press Enter for Best): ")
	if VIDEO_ID == "":
		VIDEO_ID = "bv"
	
	AUDIO_ID = input("ENTER AUDIO_ID (Press Enter for Best): ")
	if AUDIO_ID == "":
		AUDIO_ID = "ba"
	
	divider()
	print("Downloading Encrypted Video from CDN..")	
	os.system(f'yt-dlp -o "{TEMPORARY_PATH}/encrypted_video.%(ext)s" --no-warnings --external-downloader aria2c --allow-unplayable-formats --no-check-certificate -f {VIDEO_ID} "{mpd_url}" -o "{TEMPORARY_PATH}/encrypted_video.%(ext)s"')
	print("Downloading Encrypted Audio from CDN..")
	os.system(f'yt-dlp -o "{TEMPORARY_PATH}/encrypted_audio.%(ext)s" --no-warnings --external-downloader aria2c --allow-unplayable-formats --no-check-certificate -f {AUDIO_ID} "{mpd_url}"')

VIDEO_ID = "video_avc1"
AUDIO_ID = "audio_und_mp4a"

def decrypt_content():
	extract_key(KEY_PROMPT)
	divider()
	print("Decrypting WideVine DRM.. (Takes some time)")
	osinfo()
	if PLATFORM == "Mac":
		MP4DECRYPT_PATH = "%s/mp4decrypt/mp4decrypt_mac"%FILE_DIRECTORY
	elif PLATFORM == "Windows":
		MP4DECRYPT_PATH = "%s/mp4decrypt/mp4decrypt_win.exe"%FILE_DIRECTORY
	elif PLATFORM == "Linux":
		MP4DECRYPT_PATH = "%s/mp4decrypt/mp4decrypt_linux"%FILE_DIRECTORY
	else:
		MP4DECRYPT_PATH = MP4DECRYPT_PATH = "mp4decrypt"
		
	os.system('%s %s/encrypted_video.mp4 %s/decrypted_video.mp4 --key %s --show-progress'%(MP4DECRYPT_PATH,TEMPORARY_PATH,TEMPORARY_PATH,keys))
	os.system('%s %s/encrypted_audio.m4a %s/decrypted_audio.m4a --key %s --show-progress'%(MP4DECRYPT_PATH,TEMPORARY_PATH,TEMPORARY_PATH,keys))
	print("Decryption Complete!")

def merge_content():
	divider()
	FILENAME=input("Enter File Name (with extension): \n> ")
	divider()
	print("Merging Files and Processing %s.. (Takes a while)"%FILENAME)
	time.sleep(2)
	os.system('ffmpeg -i %s/decrypted_video.mp4 -i %s/decrypted_audio.m4a -c:v copy -c:a copy %s/%s'%(TEMPORARY_PATH,TEMPORARY_PATH,OUTPUT_PATH,FILENAME))

divider()
print("**** Widevine-DL by vank0n ****")
divider()
MPD_URL = input("Enter MPD URL: \n> ")
KEY_PROMPT = input("Enter WideVineDecryptor Prompt: \n> ")
download_drm_content(MPD_URL)
decrypt_content()
merge_content()
divider()
print("Process Finished. Final Video File is saved in /output directory.")
divider()

delete_choice = input("Delete cache files? (y/n)\ny) Yes (default)\nn) No\ny/n> ")

if delete_choice == "n":
	divider()
else:
	empty_folder(TEMPORARY_PATH)



		
	
