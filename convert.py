import pydub as pd
import os
import glob

file_dir = './'
extension_list = ('*.mp4', '*.flv', '*.mp3')
def convert_to_wav(dir):
    os.chdir(dir)
    for extension in extension_list:
        for file in glob.glob(extension):
            wav_filename = os.path.splitext(os.path.basename(file))[0] + '.wav'
            pd.AudioSegment.from_file(file).export(wav_filename, format='wav')


convert_to_wav(file_dir)