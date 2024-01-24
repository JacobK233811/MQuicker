from colorama import Fore

def num_puller(body):
    # Iterates over all words to find the chapter number and saves that number as an int if possible and if not, a float
    numbers = []
    for word in body.split():
        word = word.replace(":", "")
        try:
            numbers.append(int(word.strip()))
        except ValueError:
            try:
                numbers.append(float(word.strip()))
            except ValueError:
                pass
    return numbers or [-1]

def set_changes(mangas, current):
    # Sets the mangas and current lists to the recent adjustments in case of subsequent calls to a, n, or s
    with open("saved/list.txt", "rt", encoding="utf-8") as new_list:
        mangas = [line.split("|") for line in new_list.readlines()]
    with open("saved/latest.txt") as new_latest:
        current = new_latest.readlines()

    return mangas, current

def verify_status(number_file):
    while True:
        status = input(f"\n{Fore.LIGHTWHITE_EX}Which chapter are you on?  {Fore.RESET}"), \
                 input(
                     f"{Fore.LIGHTMAGENTA_EX}Are you yet to start (yts), work in progress (wip), or up to date (utd)?\n" +
                     f"{Fore.LIGHTWHITE_EX}Please enter the corresponding three letter code found in parentheses.  {Fore.RESET}")
        if "" in status:   # status == ("", "") or
            number_file.write(" ".join(["0", "yts"]) + "\n")
            break
        elif status[0].replace(".", "").isnumeric() and status[1] in ["yts", "wip", "utd"]:
            number_file.write(" ".join(status) + "\n")
            break
        else:
            print(f"{Fore.LIGHTRED_EX}Please enter a number for the chapter and one of yts, wip, or utd for the code.  {Fore.RESET}")
    return status