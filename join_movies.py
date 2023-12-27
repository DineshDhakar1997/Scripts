from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
import glob
def concatenate_videos(video_paths, output_path):
    clips = [VideoFileClip(path) for path in video_paths]
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
    

def list_folders(directory):
    entries = os.listdir(directory)
    folders_name = [entry for entry in entries if os.path.isdir(os.path.join(directory, entry))]

    folders = [directory+'/'+entry for entry in entries if os.path.isdir(os.path.join(directory, entry))]
    return folders_name,folders
folder_names,all_folders = list_folders("/Users/dinesh/Downloads/react18")
print(list_folders("/Users/dinesh/Downloads/react18"))
def list_files(directory):
    files = glob.glob(directory+'/*.mp4')
    files=sorted(files)
    return files



for (name,folder) in zip(folder_names,all_folders):
    print(name ,folder)
    list_of_files=list_files(folder)
    video_paths = list_of_files
    output_path = f"{name}.mp4"
    concatenate_videos(video_paths, output_path)