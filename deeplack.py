#!/usr/bin/env python3

# Copyright (C) 2019  Xavier Blasco <lerhan@protonmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from __future__ import print_function
import requests
import argparse
import json
import sys
import os

# Options
parser=argparse.ArgumentParser()
parser.add_argument('-nd','--new-directory', help='<NEW_DIRECTORY> Directory containing lastest screenshots.')
parser.add_argument('-od','--old-directory', help='<OLD_DIRECTORY> Directory containing older screenshots.')
parser.add_argument('-s','--sensitivity', help='Adjust distance sensitivity (default 0)', default=0, type=int)

# Slack variables
slack_channel=os.environ["SLACK_CHANNEL"]
slack_bearer=os.environ["SLACK_BOT_TOKEN"]

# Python 2 and 3 compatibility
if (sys.version_info < (3, 0)):
    os_getcwd = os.getcwdu
else:
    os_getcwd = os.getcwd

# Upload the given file to slack
def upload_image_slack(path, comment):
    r = requests.post(
        "https://slack.com/api/files.upload",
        files={
            'file': open(path, 'rb')
        },
        data={
            'title':os.path.basename(path),
            'initial_comment':comment,
            'channels':slack_channel,
            'token':slack_bearer
        }
    )
    if(r.json()["ok"] != True):
        print('There was a problem uploading' + path + 'to Slack')


def main():
    options=parser.parse_args()

    if (options.new_directory == None) or (options.old_directory == None):
        parser.error('Please specify new and old directories')

    for file in os.listdir(os.path.join(os_getcwd(), options.old_directory)):
        new_path=os.path.join(os.path.join(os_getcwd(), options.new_directory, file))
        old_path=os.path.join(os.path.join(os_getcwd(), options.old_directory, file))
        if os.path.isfile(new_path):

            r = requests.post(
                "https://api.deepai.org/api/image-similarity",
                files={
                    'image1': open(new_path, 'rb'),
                    'image2': open(old_path, 'rb'),
                },
                headers={'api-key': os.environ['DEEPAI_API_KEY']}
            )
            distance=r.json()["output"]["distance"]
            print("The images are different and the distance is: " + str(distance))
            if (distance >= options.sensitivity):
                print("Uploading files to slack...")
                upload_image_slack(new_path,"NEW")
                upload_image_slack(old_path,"OLD")
                print("Done")
        else:
            print("The following file doesn't exist:" + new_path)

if __name__ == "__main__" :
    main()
