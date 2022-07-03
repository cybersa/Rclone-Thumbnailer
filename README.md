# Rclone-Thumbnailer
Rclone Thumbnailer - Thumbnail generator for encrypted remote in the Rclone.

[Rclone](https://github.com/rclone/rclone) - is a great open source tool to save personal photos in any cloud storage in encrypted format for privacy concern.

## Description:

I'm using the Rclone tool to upload/sync all my personal photos to cloud storage. Rclone does the job easily when I want to upload(encrypt) or download(decrypt) the photo through CLI or Web GUI. But when I want to view certain photos or search for certain photos without downloading(decrypting), it's not possible in this tool because the photo was in encrypted format and it will take some time to download, decrypt and view the photo. So I have created this small utility tool(Web GUI) to view the photo(Thumbnail) without downloading/decrypting by keeping the thumbnail of the encrypted photo locally. Note this tool is in a very early stage(alpha) and it may have bugs.

## Features:

1. Thumbnail generation whenever you upload a new photo.
2. Directory creation.
3. Thumbnail will be generated automatically for the existing photos or the photos that uploaded directly through rclone CLI. Note: This will happen when you browse through the photos using this tool for the first time.
4. Photo Viewer - To view the photos with controls from Web GUI.

## Requirement:

* Python 3.8+ with PIP
* Rclone setup in your local.

## How to 

1. Download or Clone this repo to your local.
2. Open a terminal/command prompt/power shell and navigate to the downloaded/cloned repo.
3. Create a python virtual environment using this command:  (Ref: https://docs.python.org/3.8/library/venv.html)
`python -m venv venv`
4. Activate a virtual environment based on your OS/Terminal
  - Linux / Mac - `source ./venv/bin/activate`
  - Windows - Command prompt - `.\venv\Scripts\activate.bat`
  - Windows - Powershell - `.\venv\Scripts\activate.ps1`
5. Install the required dependencies using pip.
    - `pip install -r requirements.txt`
6. Now start the tool using `flask run` command.
7. Next we have to start the rclone.
8. Open another terminal/command prompt/power shell and navigate to the rclone folder.
9. Start the rclone in remote control mode using this command:
  - Windows - `.\rclone.exe rcd --rc-allow-origin '*' --rc-no-auth --rc-serve`
  - Linux / Mac - `./rclone rcd --rc-allow-origin '*' --rc-no-auth --rc-serve`
10. Now open the browser and navigate to http://localhost:5000. You should be able to see all your remotes.
11. For the first time, just navigate around the encrypted remotes and a thumbnail will be generated and saved locally.

## Open Source Libraries used:

### Viewer.js - JavaScript image viewer.
https://github.com/fengyuanchen/viewerjs

### Remix Icon - https://remixicon.com/
https://github.com/Remix-Design/remixicon 

### Bootstrap
https://github.com/twbs/bootstrap
