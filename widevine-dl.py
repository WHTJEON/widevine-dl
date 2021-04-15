#!/usr/bin/env python3

import os 
import subprocess
import shutil
import glob
import pathlib

FILE_DIRECTORY=str(pathlib.Path(__file__).parent.absolute())
TEMPORARY_PATH = FILE_DIRECTORY+"/cache"
OUTPUT_PATH = FILE_DIRECTORY+"/output"

def divider():
	print ('-' * shutil.get_terminal_size().columns)
	
def empty_folder(folder):
	files = glob.glob('%s/*'%folder)
	for f in files:
		os.remove(f)
	print("Emptied Temporary Files!")
	divider()
	
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
	VIDEO_ID = input("ENTER VIDEO_ID (Press Enter for Default): ")
	if VIDEO_ID == "":
		VIDEO_ID = "video_avc1"
	
	AUDIO_ID = input("ENTER AUDIO_ID (Press Enter for Default): ")
	if AUDIO_ID == "":
		AUDIO_ID = "audio_und_mp4a"
	
	divider()
	print("Downloading Encrypted Version from MPD CDN..")
	output = "%s/encrypted"%TEMPORARY_PATH
	args = '%s+%s "%s"'%(VIDEO_ID,AUDIO_ID,mpd_url)
	os.system('yt-dlp --external-downloader aria2c --no-warnings --allow-unplayable-formats --no-check-certificate -f '+args+' -o '+"'"+output+".%(ext)s'")	
	
VIDEO_ID = "video_avc1"
AUDIO_ID = "audio_und_mp4a"

def decrypt_content():
	extract_key(KEY_PROMPT)
	divider()
	print("Decrypting WideVine DRM..")
	os.system('mp4decrypt %s/encrypted.f%s.mp4 %s/decrypted_video.mp4 --key %s --show-progress'%(TEMPORARY_PATH,VIDEO_ID,TEMPORARY_PATH,keys))
	os.system('mp4decrypt %s/encrypted.f%s.m4a %s/decrypted_audio.m4a --key %s --show-progress'%(TEMPORARY_PATH,AUDIO_ID,TEMPORARY_PATH,keys))
	print("Decryption Complete!")

def merge_content():
	divider()
	FILENAME=input("Enter File Name (with extension): ")
	divider()
	print("Merging Files and Processing Output.. (Takes a while)")
	os.system('ffmpeg -i %s/decrypted_video.mp4 -i %s/decrypted_audio.m4a -c:v copy -c:a aac %s/%s'%(TEMPORARY_PATH,TEMPORARY_PATH,OUTPUT_PATH,FILENAME))

print("\n**** Widevine-DL by vank0n ****")
divider()
KEY_PROMPT = input("Enter WideVineDecryptor Prompt: ")
MPD_URL = input("Enter MPD URL: ")
download_drm_content(MPD_URL)
decrypt_content()
merge_content()
divider()
print("Process Finished. Final Video File is saved in /output directory.")
divider()

delete_choice = input("Delete cache files? Enter yes or no: ")
	
if delete_choice == "yes":
	empty_folder(TEMPORARY_PATH)
	
else:
	quit()



		
