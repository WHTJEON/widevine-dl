# Widevine-DL     
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Github All Releases](https://img.shields.io/github/downloads/WHTJEON/widevine-dl/total.svg)]() [![Build Status](https://img.shields.io/github/forks/WHTJEON/widevine-dl.svg)](https://github.com/WHTJEON/widevine-dl) [![License](https://img.shields.io/github/license/WHTJEON/widevine-dl.svg)](https://github.com/WHTJEON/widevine-dl)

Encrypted MPD Manifest Content Downloader + Decryptor<br>

## Requirements
- ffmpeg, yt-dlp, aria2, widevine-l3-decryptor

```
$ pip install ffmpeg yt-dlp aria2p
```
- ~~You must add mp4decrypt to `PATH` in order to run this script!~~
- For Linux Users, it is recommended to install aria2 with apt.
```
$ sudo apt-get install aria2
```

## Installation & Run
1. Download and Extract ZIP from [Releases](https://github.com/WHTJEON/widevine-dl/releases)
2. Install Requirements
3. Run widevine-dl.py
```
$ python3 widevine-dl.py
```

## Inputs
- `WideVineDecryptor Prompt` - Copy from widevine-l3-decryptor extension *(exactly like the format below)*
```
WidevineDecryptor: Found key: 100b6c20940f779a4589152b57d2dacb (KID=eb676abbcb345e96bbcf616630f1a3da)
```
- `MPD URL` - MPD URL of Widevine Content
- `VIDEO_ID` - Video Track ID Shown in Stream Info 
- `AUDIO_ID` - Audio Track ID Shown in Stream Info 
- `FILENAME` - Desired File Name of Final Decrypted File *(with extension!)*

## Legal Disclaimer
Educational purposes only. Downloading DRM'ed materials may violate their Terms of Service.

