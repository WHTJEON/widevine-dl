# Widevine-DL     
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Github All Releases](https://img.shields.io/github/downloads/WHTJEON/widevine-dl/total.svg)]() [![License](https://img.shields.io/github/license/WHTJEON/widevine-dl.svg)](https://github.com/WHTJEON/widevine-dl)

Encrypted MPD Manifest Content Downloader + Decryptor (not a Widevine Key Extractor!)<br>

## Requirements
- ffmpeg, yt-dlp, aria2, widevine-l3-decryptor

```
$ pip install ffmpeg yt-dlp aria2p
```
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
- `WideVineDecryptor Prompt` - Copy from widevine-l3-decryptor extension *(**exactly like the format below**)*
```
WidevineDecryptor: Found key: 100b6c20940f779a4589152b57d2dacb (KID=eb676abbcb345e96bbcf616630f1a3da)
```
- `MPD URL` - MPD URL of Widevine Content
- `VIDEO_ID` - Video Track ID Shown in Stream Info *(Leave blank for best)*
- `AUDIO_ID` - Audio Track ID Shown in Stream Info *(Leave blank for best)*
- `FILENAME` - Desired File Name of Final Decrypted File *(with extension!)*
- If you only want to _download_ the encrypted content from the MPD File not _decrypt_ it, simply leave the `WideVineDecryptor Prompt` empty.

## Legal Notice
Educational purposes only. Downloading DRM'ed materials may violate their Terms of Service.

##
If you enjoyed using the script, a star or a follow will be highly appreciated! 😎


