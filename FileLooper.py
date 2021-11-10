import os
import Beta1

events_files = []
for dirpath, dirnames, files in os.walk('./data/events'):
    for file_name in files:
        events_files.append(file_name)

for i in range(803, 804):
    Beta1.main('./data/events/' + events_files[i])