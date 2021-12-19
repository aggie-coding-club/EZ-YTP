from moviepy.decorators import outplace
import requests
import pickle
import re
from moviepy.editor import VideoFileClip, concatenate_videoclips
import time

# This program generates a sentence mixed YTP from the following parameters. 

video_filename = "test_files/words.mp4" # replace with the video you want to sample from's file path
transcript_filename = "test_files/words.txt" # replace with the above video's transcript file path
script_filename = "test_files/script.txt" # replace with desired script's file path
output_filename = "test_files/output.mp4" # replace with output video file path

def get_phonemes_in_video(video_filename, transcript_filename):
    # make api call
    params = (
        ('async', 'false'),
    )
    files = {
        'audio': (video_filename, open(video_filename, 'rb')),
        'transcript': (transcript_filename, open(transcript_filename, 'rb')),
    }
    response = requests.post('http://localhost:8765/transcriptions', params=params, files=files)

    # save relevant results to dictionary
    body = response.json()
    word_dict = {}
    phoneme_dict = {}
    words = body['words']
    for word in words:
        if word['case'] == 'success':
            if word['word'].upper() not in word_dict:
                word_dict[word['word'].upper()] = {'start': word['start'], 'end': word['end']}
            start_offset = 0
            for phoneme in word['phones']:
                phoneme_name = phoneme['phone'].upper()
                phoneme_name = phoneme_name.split("_")[0]
                if phoneme_name not in phoneme_dict:
                    start = word['start'] + start_offset
                    end = start + phoneme['duration']
                    start_offset += phoneme['duration']
                    phoneme_dict[phoneme_name] = {'start': start, 'end': end}

    return (word_dict, phoneme_dict)

def get_phonemes_in_script(script_filename, word_dict):
    
    # load word pronounciation dictionary
    dict_file = open("pronounciation_dict.pkl", "rb")
    pronounciation_dict = pickle.load(dict_file)
    dict_file.close()

    script_file = open(script_filename, "r")
    script_content = script_file.readlines()

    # regular expression to match all non alpha-num characters except spaces
    pattern = re.compile('[^\' \w+]')

    # list to store all phonemes in script
    phoneme_list = []

    for line in script_content:
        line = pattern.sub('', line).upper()
        line = line.split()
        for word in line:
            if word in word_dict:
                phoneme_list.append(word)
            else:
                try:
                    phoneme_list.extend(pronounciation_dict[word])
                except KeyError:
                    print("No match in dict: ", word)
    script_file.close()
    return phoneme_list

def splice_video(script_phonemes, video_words, video_phonemes, video_filename, output_filename):
    clip_list = []
    for phoneme in script_phonemes:
        if phoneme in video_words:
            start = video_words[phoneme]["start"]
            end = video_words[phoneme]["end"]
            clip = VideoFileClip(video_filename).subclip(start, end)
            clip_list.append(clip)
        else:
            try:
                start = video_phonemes[phoneme]["start"]
                end = video_phonemes[phoneme]["end"]
                clip = VideoFileClip(video_filename).subclip(start, end)
                clip_list.append(clip)
            except KeyError:
                print("Phoneme not in video: ", phoneme)
    final_clip = concatenate_videoclips(clip_list)
    final_clip.write_videofile(output_filename)

start_time = time.time()

print("Analyzing video")
audio_dicts = get_phonemes_in_video(video_filename, transcript_filename)
word_dict = audio_dicts[0]
phoneme_dict = audio_dicts[1]
print("Analyzing script")
script_phonemes = get_phonemes_in_script(script_filename, word_dict)
print("Creating video")
splice_video(script_phonemes, word_dict, phoneme_dict, video_filename, output_filename)

print("Program finished in :", time.time() - start_time, "seconds")
