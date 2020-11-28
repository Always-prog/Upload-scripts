# Upload-scripts
This repository for auto update repository.
If you need to update your program in the server, after once you upload new changes in the master branch - this program will do it
To use this auto-update program:

1. download repository Upload-scripts
2. open config.txt
3. Write your data in the config
For example
```java
REPOSITORY==Upload-scripts
ROOT==C:\Users\Stepan\Desktop\Upload-scripts\
TOKEN==bc4ef98nfn3498sasip34os6fd2add8b2459e
USERNAME==Always-prog
START==python main.py
```
4. Run this program by command `python auto_update.py`


After this steps, auto_update.py check master branch every 10 seconds, and if in master have new changes, this program update your project and rerun program.
I use this auto-update program for my bot in telegram: @YouToneBot


