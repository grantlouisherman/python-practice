import sys, termios
import os

def main():
   sys.stdout.write(f"WGAF v1.0 on {os.name}\n")
   sys.stdout.write('Type "help", "copyright", "credits" or "license" for more information.\n')
   sys.stdout.write('$ ')
   while True:
    command = input()
    if command == "exit":
        break
        
        
		

if __name__ == "__main__":
	main()
