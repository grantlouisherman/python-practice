import sys, termios
import os


VIRTUAL_DIR = os.getcwd()
DEBUGGING=False

def __DEBUG__(message):
    if DEBUGGING:
        sys.stdout.write(message)


def CommandPWD():
    sys.stdout.write(os.getcwd())



def _walk_directory(path):
    print("DIRRR", path)
    for item in os.listdir(path):
        tag = "file" if os.path.isfile(item) else "dir"
        sys.stdout.write(f"------ {tag} {item}\n")

def CommandLS(path):
    if len(path) <= 0:
        _walk_directory(VIRTUAL_DIR)
        return
    _walk_directory(path)
       

def main(args):
   sys.stdout.write(f"WGAF v1.0 on {os.name}\n")
   sys.stdout.write('Type "help", "copyright", "credits" or "license" for more information.\n')
   sys.stdout.write('$ ')
   while True:
    command = input()
    parse_command = command.split(" ")
    root_command = parse_command[0]
    arguments = ""
    if len(parse_command) > 1:
        arguments = parse_command[1]
    match root_command:
        case "exit":
            break
        case "pwd":
            CommandPWD()
            break
        case "ls":
                print("ARGUEMNTS", len(arguments))
                CommandLS(arguments)
                break

    

        
        
		

if __name__ == "__main__":
    main(sys.argv[:1])
