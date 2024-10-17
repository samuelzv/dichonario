from subprocess import run

def main():
    print("Menu:")
    print("1. Make messages")
    print("2. Compile messages")
    print("3. Make migrations")
    print("4. Migrate")
    print("5. @echo: Login to app container")
    print("6. @echo: Install package into app container")

    option = input("Select your option: ")
    result = None
    if option == "1":
        print("Making messages...")
        result = run(["docker-compose", "run", "--rm", "app", "sh", "-c", "python manage.py makemessages -l es"], capture_output=True, encoding="utf-8")
    elif option == "2":
        print("Compiling messages...")
        result = run(["docker-compose", "run", "--rm", "app", "sh", "-c", "python manage.py compilemessages"], capture_output=True, encoding="utf-8")
    elif option == "3":
        print("Making migrations...")
        result = run(["docker", "exec", "-it", "-u", "root", "dichonario-app-1", "/bin/sh", "-c" , "python manage.py migrate"])
    elif option == "4":
        print("Migrate...")
        result = run(["docker", "exec", "-it", "-u", "root", "dichonario-app-1", "/bin/sh", "-c" , "python manage.py makemigrations"])
    elif option == "5":
        print (' '.join(["docker", "exec", "-it", "-u", "root", "dichonario-app-1", "/bin/sh"]))
    elif option == "6":
        print (' '.join(["docker", "exec", "-it", "-u", "root", "dichonario-app-1", "/bin/sh", "-c" , '"python -m pip install PACKAGE_NAME"']))

    print(result)

if __name__ == "__main__":
    main()