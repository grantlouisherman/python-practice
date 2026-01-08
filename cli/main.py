import sys, termios
import os

def CommandPWD():
    sys.stdout.write(os.getcwd())
    
def CommandLS(path):
    if len(path) <= 0:
        dir = os.listdir(os.getcwd())
        for item in dir:
            tag = "file" if os.path.isfile(item) else "dir"
            sys.stdout.write(f"------ {tag} {item}")


def main():
   sys.stdout.write(f"WGAF v1.0 on {os.name}\n")
   sys.stdout.write('Type "help", "copyright", "credits" or "license" for more information.\n')
   sys.stdout.write('$ ')
   while True:
    command = input()
    parse_command = command.split(" ")
    root_command = parse_command[0]
    arguments = parse_command[1]
    match root_command:
        case "exit":
            break
        case "pwd":
            CommandPWD()
            break
        case "ls":
                CommandLS(arguments)
                break

    

        
        
		

if __name__ == "__main__":
	main()
