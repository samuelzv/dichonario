from subprocess import run

def main():
    print("Menu:")
    print("1. Make messages")
    print("2. Compile messages")

    option = input("Select your option: ")
    result = None
    if option == "1":
        print("Making messages...")
        result = run(["docker-compose", "run", "--rm", "app", "sh", "-c", "python manage.py makemessages -l es"], capture_output=True, encoding="utf-8")
    elif option == "2":
        print("Compiling messages...")
        result = run(["docker-compose", "run", "--rm", "app", "sh", "-c", "python manage.py compilemessages"], capture_output=True, encoding="utf-8")

    print(result)

if __name__ == "__main__":
    main()