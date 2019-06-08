# Deeplack
Deeplack is an experimental script for finding differences between images and notifiying the user via Slack. It makes use of [DeepAI](https://deepai.org/) to compare the images. The purpose of this project is to look for changes on web applications given old and new screenshots.
# Installation

```
git clone TODO
export SLACK_CHANNEL="<SLACK CHANNEL NAME>"
export SLACK_BOT_TOKEN="<SLACK BOT TOKEN>"
export DEEPAI_API_KEY="<DEEP API KEY"
```
DeepAI api key can be obtained after signing up at https://deepai.org
Slack bot access_token can be found under `OAuth & Permissions` within your App settings. To add a bot to a channel you can follow this guide https://api.slack.com/bot-users.
The slack channel name is the name of the channel that you want the images to be uploaded to.

# Usage
Pass both old and new directories to Deeplack: `deeplack.py -nd <NEW_DIRECTORY> -od <OLD_DIRECTORY>`
It's best to combine this functionality with [webscreenshot](https://github.com/maaaaz/webscreenshot) since it gives the best input for Deeplack.
### Usage WITHOUT webscreenshot
Put your screenshots in two directories, one for old screenshots and another one for new ones. The filenames of both new and old screenshots must be the same (ex. `DirectoryOld/http_google.com.png` and `DirectoryNew/http_google.com.png`).

### Sensitivity
DeepAI API returns a value that represents the distance between both images, the bigger the value, the more different both images are. The minimum distance is 0, which means both images are the same. The default value for sensitivity is set to 0, meaning that every distance bigger than 0 will alert the user via Slack that both images are different. This value can be changed to avoid false positives on dynamic websites.

# Options
```
usage: deeplack.py [-h] [-nd NEW_DIRECTORY] [-od OLD_DIRECTORY]
                   [-s SENSITIVITY]

optional arguments:
  -h, --help            show this help message and exit
  -nd NEW_DIRECTORY, --new-directory NEW_DIRECTORY
                        <NEW_DIRECTORY> Directory containing lastest
                        screenshots.
  -od OLD_DIRECTORY, --old-directory OLD_DIRECTORY
                        <OLD_DIRECTORY> Directory containing older
                        screenshots.
  -s SENSITIVITY, --sensitivity SENSITIVITY
                        Adjust distance sensitivity (default 0)
```
# License
__Deeplack__ is made with :black_heart: by Lerhan. See the __LICENSE__ file for more details.

# Contact
This is my first project and I'm sure there's a lot of things to improve, if you have any suggestions email me at lerhan@protonmail.com.
