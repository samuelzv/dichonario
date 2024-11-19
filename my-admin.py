from subprocess import run


def main():
    print("Menu:")
    print("0. Build svelte")
    print("1. Make messages")
    print("2. Compile messages")
    print("3. Make migrations")
    print("4. Migrate")
    print("5. @echo: Login to app container")
    print("6. @echo: Install package into app container")
    print("7. Update Web App - Down app")
    print("8. Update Web App - Build app")
    print("9. Update Web App - Upp app")
    print("10. Reinstall requirements")
    print("11. Load fixtures")

    option = input("Select your option: ")
    result = None
    if option == "0":
        print("Build svelte...")
        result = run("cd svelte; npm run build", capture_output=True, shell=True)
    if option == "1":
        print("Making messages...")
        result = run(
            [
                "docker",
                "exec",
                "-it",
                "-u",
                "root",
                "dichonario-app-1",
                "/bin/sh",
                "-c",
                "python manage.py makemessages -l es",
            ]
        )
    elif option == "2":
        print("Compiling messages...")
        result = run(
            [
                "docker",
                "exec",
                "-it",
                "-u",
                "root",
                "dichonario-app-1",
                "/bin/sh",
                "-c",
                "python manage.py compilemessages",
            ]
        )
    elif option == "3":
        print("Making migrations...")
        result = run(
            [
                "docker",
                "exec",
                "-it",
                "-u",
                "root",
                "dichonario-app-1",
                "/bin/sh",
                "-c",
                "python manage.py makemigrations",
            ]
        )
    elif option == "4":
        print("Migrate...")
        result = run(
            [
                "docker",
                "exec",
                "-it",
                "-u",
                "root",
                "dichonario-app-1",
                "/bin/sh",
                "-c",
                "python manage.py migrate",
            ]
        )
    elif option == "5":
        print(
            " ".join(
                ["docker", "exec", "-it", "-u", "root", "dichonario-app-1", "/bin/sh"]
            )
        )
    elif option == "6":
        print(
            " ".join(
                [
                    "docker",
                    "exec",
                    "-it",
                    "-u",
                    "root",
                    "dichonario-app-1",
                    "/bin/sh",
                    "-c",
                    '"python -m pip install PACKAGE_NAME"',
                ]
            )
        )
    elif option == "7":
        print("Update Web App - Down App...")
        result = run(
            ["docker-compose", "-f", "docker-compose-deploy.yml", "down", "app"],
            capture_output=True,
            encoding="utf-8",
        )
    elif option == "8":
        print("Update Web App - Build App...")
        result = run(
            ["docker-compose", "-f", "docker-compose-deploy.yml", "build", "app"],
            capture_output=True,
            encoding="utf-8",
        )
    elif option == "9":
        print("Update Web App - Up App...")
        result = run(
            [
                "docker-compose",
                "-f",
                "docker-compose-deploy.yml",
                "up",
                "app",
                "--detach",
                "--no-recreate",
            ],
            capture_output=True,
            encoding="utf-8",
        )
    elif option == "10":
        print(
            " ".join(
                [
                    "docker",
                    "exec",
                    "-it",
                    "-u",
                    "root",
                    "dichonario-app-1",
                    "/bin/sh",
                    "-c",
                    '"python -m pip install -r requirements/base"',
                ]
            )
        )
    elif option == "11":
        print(
            " ".join(
                [
                    "docker",
                    "exec",
                    "-it",
                    "-u",
                    "root",
                    "dichonario-app-1",
                    "/bin/sh",
                    "-c",
                    '"python manage.py loaddata language"',
                ]
            )
        )

    print(result)


if __name__ == "__main__":
    main()
