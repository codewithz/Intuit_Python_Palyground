import subprocess

subprocess.call([r"C:\Program Files\Mozilla Firefox\firefox.exe",
                 r"C:\Program Files\YouTube Downloader\YouTubeDownloader.exe"])

completed=subprocess.run(["ls","-l"])

print("args",completed.args)
print("returncode",completed.returncode)
print("stderr",completed.stderr)
print("stout",completed.stdout)