from moviepy.editor import VideoFileClip, concatenate_videoclips

clip_list = []
clip1 = VideoFileClip("test_files/words.mp4").subclip(10,20)
clip2 = VideoFileClip("test_files/words.mp4").subclip(0,10)
clip_list.append(clip1)
clip_list.append(clip2)
print(clip_list)
final_clip = concatenate_videoclips(clip_list)
final_clip.write_videofile("test_files/concat_words.mp4")
