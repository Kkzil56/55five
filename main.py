import os

kolom = os.get_terminal_size().columns

R = "\033[0;31;40m" #RED
G = "\033[0;32;40m" # GREEN
Y = "\033[0;33;40m" # Yellow
B = "\033[0;34;40m" # Blue
N = "\033[0m" # Reset
os.system('clear')
print(R+"""
       ███████╗███████╗░░░███████╗██╗██╗░░░██╗███████╗
       ██╔════╝██╔════╝░░░██╔════╝██║██║░░░██║██╔════╝
       ██████╗░██████╗░░░░█████╗░░██║╚██░░██╔╝█████╗░░
       ╚════██╗╚════██╗░░░██╔══╝░░██║░╚████╔╝░██╔══╝░░
       ██████╔╝██████╔╝██╗██║░░░░░██║░░╚██╔╝░░███████╗
       ╚═════╝░╚═════╝░╚═╝╚═╝░░░░░╚═╝░░░╚═╝░░░╚══════╝
""")
print(B+"AUTHOR : @Abahzeus,@Kageyamatobio28".center(kolom))
print("GITHUB : https://github.com/4ndrii".center(kolom))
print("")
print("")
print(f"{R}[1] . {G}Win Go")
print(f"{R}[2] . {G}TRX - Hash")
pilih = input("Masukkan Pilihan : ")
if pilih == '1':
	os.system("python t.py")
elif pilih == '2':
	os.system("python trx.py")