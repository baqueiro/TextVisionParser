#!/usr/bin/env python

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import io
import os
from glob import glob
from google.cloud import vision
from google.cloud.vision import types


def absolute_file_paths(directory):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))

def process_file(file_name, client):
    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)    

    response = client.document_text_detection(image=image)
    document = response.full_text_annotation
    return document.text

def run_quickstart():
    # [START vision_quickstart]

    # Imports the Google Cloud client library
    # [START vision_python_migration_import]
    
    # [END vision_python_migration_import]

    # Instantiates a client
    # [START vision_python_migration_client]
    client = vision.ImageAnnotatorClient()
    # [END vision_python_migration_client]
    # The name of the image file to annotate
    files = [x for x in absolute_file_paths("resources2")]
    for file in files:
        print(file)
        text = process_file(file, client)
        
        with open("res/" + os.path.basename(file) + ".txt", "w") as text_file:
            print(text, file=text_file)
    
if __name__ == '__main__':
    run_quickstart()
