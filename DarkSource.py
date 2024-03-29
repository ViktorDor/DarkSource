import colorama
import os
import socket
import requests
import wmi
import threading
import json
import subprocess
import ctypes
import sys
from colorama import Fore, Style
from time import sleep
import datetime
import stat

if ctypes.windll.shell32.IsUserAnAdmin() == 0:
  ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
#*Setting

Animation_Status = True
work_dir = f'C:/Users/{os.getlogin()}/DarkSource/Resource'
if os.path.exists(f'C:/Users/{os.getlogin()}/DarkSource') == False:
  os.system(f"""mkdir "C:/Users/{os.getlogin()}/DarkSource" """)
  os.system(f"""mkdir "C:/Users/{os.getlogin()}/DarkSource/Resource" """)
if os.path.isfile(f'C:/Users/{os.getlogin()}/DarkSource/Resource/config.json') == False:
  default_config = """{"console_color": "RED", "console_output_color": "RED", "console_anims_color": "RED", "console_input_color": "RED"}"""
  os.system(f'echo {default_config} > C:/Users/{os.getlogin()}/DarkSource/Resource/config.json')
with open(f'{work_dir}/config.json', 'r') as f:
    json_data = json.load(f)
list_data = []
for line, num in json_data.items():
    list_data.append(num)
console_color = getattr(Fore,list_data[0])
console_output_color = getattr(Fore,list_data[1])
console_anims_color = getattr(Fore,list_data[2])
console_input_color = getattr(Fore,list_data[3])
curent_dir = os.getcwd()
user = os.getlogin()
Input_line = f'{console_input_color}🗁  {os.getcwd()} ✎ {os.getlogin()} >>>{Fore.RESET}'
colors = ['RED', 'CYAN', 'BLUE', 'GREEN', 'WHITE', 'MAGENTA', 'YELLOW']

#*Init
data_ip = ''
data_network = ''


colorama.init(autoreset=True)
def get_data():
    global data_ip
    global data_network
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    public_ip = requests.get("https://api.ipify.org").text
    data_ip = f"host:{hostname} local:{local_ip} public:{public_ip}"


class console_itil():
  def reload_color():
    global console_color
    global console_anims_color
    global console_input_color
    global console_output_color
    with open(f'{work_dir}/config.json', 'r') as f:
      json_data = json.load(f)
    list_data = []
    for line, num in json_data.items():
        list_data.append(num)
    console_color = getattr(Fore,list_data[0])
    console_output_color = getattr(Fore,list_data[1])
    console_anims_color = getattr(Fore,list_data[2])
    console_input_color = getattr(Fore,list_data[3])
    
    
  def get_netstats():
    for interface in wmi.WMI().Win32_NetworkAdapter():
      if interface.NetConnectionStatus==2:
          interface=interface
          print(f"{console_output_color} {interface}")
          
          
  def menu_main():
    global Animation_Status
    os.system("cls")
    anim = ["'########:::::'###::::'########::'##:::'##:::::'######:::'#######::'##::::'##:'########:::'######::'########:", " ##.... ##:::'## ##::: ##.... ##: ##::'##:::::'##... ##:'##.... ##: ##:::: ##: ##.... ##:'##... ##: ##.....::", " ##:::: ##::'##:. ##:: ##:::: ##: ##:'##:::::: ##:::..:: ##:::: ##: ##:::: ##: ##:::: ##: ##:::..:: ##:::::::", " ##:::: ##:'##:::. ##: ########:: #####:::::::. ######:: ##:::: ##: ##:::: ##: ########:: ##::::::: ######:::", " ##:::: ##: #########: ##.. ##::: ##. ##:::::::..... ##: ##:::: ##: ##:::: ##: ##.. ##::: ##::::::: ##...::::", " ##:::: ##: ##.... ##: ##::. ##:: ##:. ##:::::'##::: ##: ##:::: ##: ##:::: ##: ##::. ##:: ##::: ##: ##:::::::", " ########:: ##:::: ##: ##:::. ##: ##::. ##::::. ######::. #######::. #######:: ##:::. ##:. ######:: ########:", "........:::..:::::..::..:::::..::..::::..::::::......::::.......::::.......:::..:::::..:::......:::........::"]
    # anim = [" __      _______ ______   _____ _____  ______ ", " \ \    / / ____|  ____| |_   _|  __ \|  ____|", "  \ \  / / |  __| |__      | | | |  | | |__   ", "   \ \/ /| | |_ |  __|     | | | |  | |  __|  ", "    \  / | |__| | |       _| |_| |__| | |____ ", "     \/   \_____|_|      |_____|_____/|______|"]
    # if Animation_Status:
    #   for i in anim:
    #       print(f'{console_anims_color}{i}')
    #       sleep(0.3)
    # else:
    if True:
      logo = ''
      for i in anim:
        logo = f"{logo}{i}\n"
      print(f"{console_anims_color}{logo}")
    Animation_Status = False
      

  def load():
    two = [""]
    for i in range(10):
        os.system('cls')
        two.append("▉")
        print(str(console_anims_color + "".join(two)))
        sleep(0.25)
    os.system('cls')
    two.append(" complete.")
    print(str(console_anims_color + "".join(two)))
    sleep(0.25)
  
  
  def set_color():
    global console_color
    global console_input_color
    global console_output_color
    global console_anims_color
    print(f"{console_output_color} 0.Console Color \n 1.Console output \n 2.Console animation \n 3.Console input")
    select_type_data = int(input(f"{console_input_color}>>>"))
    num = 0
    for color in colors:
      print(f"{console_output_color}{num}. {color}")
      num+=1
    select_color_data = int(input(f"{console_input_color}>>>"))
    if select_type_data == 0:
      console_color = getattr(Fore, colors[select_color_data])
      with open(f'{work_dir}/config.json', 'w') as f:
        save_data = {
          "console_color": colors[select_color_data],
          "console_output_color": list_data[1],
          "console_anims_color": list_data[2],
          "console_input_color": list_data[3]
        }
        json.dump(save_data, f)
    if select_type_data == 1:
      console_output_color = getattr(Fore, colors[select_color_data])
      with open('DarkSource/config.json', 'w') as f:
        save_data = {
          "console_color": list_data[0],
          "console_output_color": colors[select_color_data],
          "console_anims_color": list_data[2],
          "console_input_color": list_data[3]
        }
        json.dump(save_data, f)
    if select_type_data == 2:
        console_input_color = getattr(Fore, colors[select_color_data])
        with open(f'{work_dir}/config.json', 'w') as f:
          save_data = {
            "console_color": list_data[0],
            "console_output_color": list_data[1],
            "console_anims_color": colors[select_color_data],
            "console_input_color": list_data[3]
          }
          json.dump(save_data, f)
    if select_type_data == 3:
      console_anims_color = getattr(Fore, colors[select_color_data])
      with open(f'{work_dir}/config.json', 'w') as f:
        save_data = {
          "console_color": list_data[0],
          "console_output_color": list_data[1],
          "console_anims_color": list_data[2],
          "console_input_color": colors[select_color_data]
        }
        json.dump(save_data, f)


def wait():
  try:
    global Input_line
    while True:
      console_itil.reload_color()
      Input_line = f'{console_input_color}🗁  {os.getcwd()} ✎ {os.getlogin()} >>>{Fore.RESET}'
      data = str(input(Input_line))
      if data == "exit":
          print(f"{console_output_color}Stopping...")
          exit()
      if data in ['clear', 'cls', 'clr']:
        console_itil.menu_main()
        continue
      if data == 'ip':
        print(f"{console_output_color}{data_ip}")
        continue
      if data == "netstats":
        console_itil.get_netstats()
        continue
      if data == 'color':
        console_itil.set_color()
        continue
      if data == 'activate':
        command = str("irm https://massgrave.dev/get | iex")
        result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
        if result.returncode == 0:
            output = result.stdout
        else:
            output = result.stderr
        print(output)
        continue
      if data == 'snoop':
        if os.path.isfile(f"{work_dir}/snoop.exe"):
          user_name = str(input("User: "))
          console_itil.load()
          os.system(f""""{work_dir}/snoop.exe" {user_name}""")
        else:
          print(f"{console_output_color}Resource not installed! Use apt install snoop!")
        continue
      if data.split()[0] == 'ls':
        if len(data.split()) > 1:
          if data.split()[1] == '-l':
            if len(data.split()) > 3:
              directory = str(data.split()[3:])
            else:
              directory = str(os.getcwd())
            for entry in os.listdir(directory):
              file_path = os.path.join(directory, entry)
              file_stat = os.stat(file_path)
              mode = file_stat.st_mode
              permissions = stat.filemode(mode)
              size = file_stat.st_size
              if os.path.isdir(file_path):
                name = str(f"{Fore.CYAN}{os.path.basename(file_path)}")
              else:
                name = str(f"{Fore.WHITE}{os.path.basename(file_path)}")
              modified_time = datetime.datetime.fromtimestamp(file_stat.st_mtime).strftime('%b %d %H:%M')
              print("{:1}{:<10} {:<5} {:<10} {:<10}".format(Fore.WHITE, permissions, size, modified_time, name))  
            continue
          else:
            path = f'{"".join(data.split()[2:])}'
            files = os.listdir(path)
        else:
          files = os.listdir(os.getcwd())
        b = 0
        for i in files:
          if os.path.isdir(i):
            files[b] = f"{Fore.CYAN}{i}"
          else:
            files[b] = f"{Fore.WHITE}{i}"
          b+=1
        files = "   ".join(files)
        print(f"{console_output_color}{files}")
        continue
      if data.split()[0] == 'nmap':
        if os.path.isfile(f"{work_dir}/nmap/nmap.exe"):
          if len(data.split()) < 2:
            print(f"{console_output_color} Print ip!")
            continue
          ip = str(data.split()[1])
          print(f"{console_output_color}")
          os.system(f""""{work_dir}/nmap/nmap.exe" {ip}""")
        else:
          print(f"{console_output_color}Resource not installed! Use apt install nmap!")
        continue
      if data.split()[0] == 'cd':
        try:
          argus = data.split()
          argus.pop(0)
          print(f"{console_output_color}")
          if (len(argus) == 0):
            os.chdir(f"C:/Users/{user}")
            continue
          path_to_dir = " ".join(argus)
          if path_to_dir == '~':
            os.chdir(f"C:/Users/{user}")
            continue
          os.chdir(f"{path_to_dir}")
          continue
        except Exception as e:
          ...
      if data.split()[0] == 'sudo':
        argus = data.split()
        if len(argus) < 2:
          print(f"{console_output_color} Print command!")
          continue
        command = " ".join(argus[1:])
        print(f"{console_output_color}")
        try:
          subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
          ...
        continue
      if data.split()[0] == 'ufw':
        print(data.split())
        if len(data.split()) < 3:
          print(f"{console_output_color} Print status and port!")
          continue
        status = str(data.split()[1])
        port = int(data.split()[2])
        if (status not in ['allow', 'deny']):
          print(f"{console_output_color} None status {status}. allow / deny")
          continue
        if status == 'deny':
          status = 'block'
        command =  f"""netsh advfirewall firewall add rule name= "{status} port {port}" dir=in action=allow protocol=TCP localport={port}"""
        try:
          subprocess.run(f"{command}",shell=True, check=True)
        except subprocess.CalledProcessError as e:
          ...
        continue
      if data.split()[0] == 'nano':
        user_name = os.getlogin()
        if os.path.isfile(f"{work_dir}/nano.exe"):
          if len(data.split()) < 2:
            os.system(f""""{curent_dir}/DarkSource/Resource/nano.exe" """)
          else:
            os.system(f""""C:/Users/{user_name}/DarkSource/Resource/nano.exe" {"".join(data.split()[1:])}""")
        else:
          print(f"{console_output_color}Resource not installed! Use apt install nano!")
        continue
      if data.split()[0] == 'touch':
        if len(data.split()) < 2:
          print(f"{console_output_color} Input file name!")
        else:
          file_name = str("".join(data.split()[1:]))
          os.system(f"type nul > {file_name}")
        continue
      if data.split()[0] == 'rm':
        if len(data.split()) < 2:
          print(f"{console_output_color} Input file name!")
        else:
          file_name = str("".join(data.split()[1:]))
          os.system(f"del {file_name}")
        continue
      if data.split()[0] == 'cp':
        if len(data.split()) < 3:
          print(f"{console_output_color} Input file name!")
        else:
          file_name = str("".join(data.split()[1]))
          new_file_name = str("".join(data.split()[2]))
          os.system(f"copy {file_name} {new_file_name}")
        continue
      if data.split()[0] == 'mv':
        if len(data.split()) < 3:
          print(f"{console_output_color} Input file name!")
        else:
          file_name = str("".join(data.split()[1]))
          new_file_name = str("".join(data.split()[2]))
          os.system(f"move {file_name} {new_file_name}")
        continue
      if data.split()[0] == 'cat':
        if len(data.split()) < 2:
          print(f"{console_output_color} Input file name!")
        else:
          file_name = str("".join(data.split()[1:]))
          try:
            with open(f"{file_name}", 'r') as f:
              content = str(f.read())
              content = content.split()[:50]
              content = "".join(content)
            print(f"{console_output_color}{content}")
          except FileNotFoundError as e:
            print(f"{console_output_color}{e}")
        continue
      # if data.split()[0] == 'apt':
      #   packet_list = ['nmap', 'snoop', 'nano']
      #   if (data.split()[1] != 'list') & (len(data.split()) < 3):
      #     print(f"{console_output_color} Input: apt install/unistall packet_name")
      #   if data.split()[1] == 'install':
      #     if data.split()[2] == 'nano':
      #       # os.system(f'curl -O https://drive.google.com/uc?export=download&id=1MdqUKoThEiTOavRS4SLq2mJIK6aukfve')
      #       response = requests.get("https://github.com/ViktorDor/DarkSourceResourse/blob/main/Resource/nano.exe")
      #       print(response.content)
      #       # with open(f"{work_dir}/nano.exe", 'wb') as f:
      #         # f.write(response.content)
      #       #   f.close()
        # if data.split()[1] == 'unistall':
        #   ...
        # if data.split()[1] == 'list':
        #   for i in packet_list:
        #     print(f"{console_output_color}{i}")
        # continue
      try:
        print(f"{console_output_color}")
        os.system(f"{data}")
      except:
        print(f"{Fore.RED} Неизвестная комманда!")
  except KeyboardInterrupt:
    exit()
 
threading_load_data = threading.Thread(target=get_data)
threading_load_data.start()
# console_itil.load()
console_itil.menu_main()
wait()