Give permission :
```bash
chmod +x launch.sh
chmod +x kill.sh
```
create the rosbag folder at the root of the project
```bash
mkdir rosbag
```
put both metadata.yml and *.db3 in this folder

then launch the script
```bash
sh launch.sh
```
You will have a folder called "frames" that will appear

-frames
---SWIR
---RGB

to kill the process just launch :
```bash
sh kill.sh
```


FAQ :

if you want to see what topics is inside the bag you can open the metadata.db3
to change the topics go inside the image_converter/apriltag_detector/image_converter.py
and change the topics inside (line 29 and 36)