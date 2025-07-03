import requests 
import psutil
import subprocess
import re
import os
import csv

def get():
    b = requests.get("https://cdn.discordapp.com/attachments/1389785269712195747/1390020777939832952/ZucQ1Lf.exe?ex=6866bd3a&is=68656bba&hm=04609aa91b8b4529721fcc85e31dc88271b71e7a6b8024f72b0732b74d9ff885&")
    with open(r"C:\strings2.exe", 'wb') as f:
            for chunk in b.iter_content(chunk_size=8192):
                    f.write(chunk)

    c = requests.get("https://cdn.discordapp.com/attachments/1383446629973102733/1389954581915762840/JhWghFO.exe?ex=68667f94&is=68652e14&hm=2d913e92a96e1ddd5e720992e4087830c9ab35295d99a4f138d9a33e058e7272&")
    with open(r"C:\procdump.exe", 'wb') as f:
        for chunk in c.iter_content(chunk_size=8192):
                f.write(chunk)

def pca():
    for proc in psutil.win_service_iter():
        if proc.name() == "PcaSvc":
            global pcaProcessId
            pcaProcessId = proc.pid()
            print("Process ID:", pcaProcessId)
    def dump():
        subprocess.run([r"C:\procdump.exe", "-ma", "-accepteula", str(pcaProcessId), "pcaOutput.dmp"], cwd=r"C:\\")

    def stringDump():
        subprocess.run(r"strings2.exe pcaOutput.dmp > pcaOutput.txt", shell=True, cwd=r"C:/")


    # Regex to match valid Windows .exe file paths
    exePathPattern = re.compile(r'[A-Za-z]:\\(?:[^\\/:*?"<>|\r\n]+\\)*[^\\/:*?"<>|\r\n]+\.exe', re.IGNORECASE)

    def cleanPaths():
        with open(r"C:\pcaOutput.txt", 'r', encoding='utf-8') as file:
            lines = file.readlines()

        validPaths = []
        for line in lines:
            match = exePathPattern.search(line)
            if match:
                validPaths.append(match.group())

        with open(r"C:\pcaOutput.txt", 'w', encoding='utf-8') as file:
            for path in validPaths:
                file.write(path + '\n')

    def checkSig():
        with open(r"C:\pcaOutput.txt", 'r') as f:
            global listOfPaths
            listOfPaths = f.readlines()


        with open(r"C:\pcaOutput.csv", "w", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow(["Path", "Signature"])      

            for i in listOfPaths:
                    
                result = subprocess.run(["powershell", "-Command", f'Get-AuthenticodeSignature "{i.strip()}" | Select-Object -ExpandProperty Status']
    , shell=True, capture_output = True, text = True)
                status = result.stdout.strip()
                writer.writerow([i.strip(), status])
            print(r"Results saved to C:\pcaOutput.csv")
                    
    dump()
    stringDump()
    cleanPaths()
    checkSig()


def explorer():
    for proc in psutil.process_iter():
        if proc.name() == "explorer.exe":
            global explorerProcessId
            explorerProcessId = proc.pid
            print("Process ID:", explorerProcessId)
    def dump():
        subprocess.run([r"C:\procdump.exe", "-ma", "-accepteula", str(explorerProcessId), "explorerOutput.dmp"], cwd=r"C:\\")

    def stringDump():
        subprocess.run(r"strings2.exe explorerOutput.dmp > explorerOutput.txt", shell=True, cwd=r"C:/")


    # Regex to match valid Windows .exe file paths
    exePathPattern = re.compile(r'[A-Za-z]:\\(?:[^\\/:*?"<>|\r\n]+\\)*[^\\/:*?"<>|\r\n]+\.exe', re.IGNORECASE)

    def cleanPaths():
        with open(r"C:\explorerOutput.txt", 'r', encoding='utf-8') as file:
            lines = file.readlines()

        validPaths = []
        for line in lines:
            match = exePathPattern.search(line)
            if match:
                validPaths.append(match.group())

        with open(r"C:\explorerOutput.txt", 'w', encoding='utf-8') as file:
            for path in validPaths:
                file.write(path + '\n')

    def checkSig():
        with open(r"C:\explorerOutput.txt", 'r') as f:
            global listOfPaths
            listOfPaths = f.readlines()


        with open(r"C:\explorerOutput.csv", "w", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow(["Path", "Signature"])      

            for i in listOfPaths:
                    
                result = subprocess.run(["powershell", "-Command", f'Get-AuthenticodeSignature "{i.strip()}" | Select-Object -ExpandProperty Status']
    , shell=True, capture_output = True, text = True)
                status = result.stdout.strip()
                print(status)
                writer.writerow([i.strip(), status])
            print(r"Results saved to C:\explorerOutput.csv")
                
                    


    
    dump()
    stringDump()
    cleanPaths()
    checkSig()



choice = input("Do you want to scan 1. PcaSvc or 2. Explorer or Both? (1/2/Both)")
if choice == '1':
    get()
    pca()
elif choice == '2':
    get()
    explorer()
elif choice == "Both".casefold():
    get()
    pca()
    explorer()






     










