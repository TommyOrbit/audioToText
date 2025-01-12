import pydub as pd

def convert_to_wav(file_path):
    sound = pd.AudioSegment.from_file(file_path)
    sound.export(file_path + '.wav', format='wav')

file_path = 'ai.mp4'

convert_to_wav(file_path)