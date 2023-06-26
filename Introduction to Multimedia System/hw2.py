import subprocess

input_file = 'input_image.jpg'
output_file = 'output_image.jpg'

# Define FFmpeg command to convert to grayscale
ffmpeg_command = ['ffmpeg','-i',input_file,'-vf','hue=s=0',output_file]

# Run FFmpeg command
subprocess.run(ffmpeg_command)




