from colorama import Fore

from standard.config import mangas
from standard.utils import verify_status

def change_current():
    # Allows for a fast run-through of all manga on the list and provides the option to update status and chapter
    change_counter = 0
    with open("saved/latest.txt", "rt", encoding="utf-8") as numbers_read:
        chapters = [line for line in numbers_read.readlines()]
    with open("saved/latest.txt", "wt", encoding="utf-8") as numbers:
        for i, manga in enumerate(mangas):
            if chapters[i].split()[1] != "utd" and input(
                    f"\n{Fore.LIGHTMAGENTA_EX}Would you like to update {manga[0]}'s current chapter? " +
                    f"{Fore.LIGHTWHITE_EX}Right now it is {chapters[i]}" +
                    f"{Fore.LIGHTGREEN_EX}Type anything for yes {Fore.LIGHTRED_EX}or simply press enter for no.  {Fore.RESET}"):
                change_counter += 1
                verify_status(numbers)
            else:
                numbers.write(chapters[i])
    add_to_sheet("change current", change_counter)
    set_changes(mangas, current)


# Progressive input statements provide a clean text editing experience with proper formatting and alignment
# Deters user error or frustration with sensitive entries.
def primer():
    # Choosing which manga of the base list to keep and setting their current chapter/status for that one-by-one
    if not input(
            f"{Fore.LIGHTYELLOW_EX}Are you sure? This is a somewhat long process meant only for first-time users." +
            f"\n{Fore.LIGHTRED_EX}Press enter to cancel. {Fore.LIGHTGREEN_EX}Typing anything else will begin the " +
            f"priming procedure.  {Fore.RESET}"):
        return "Interrupt"

    if input(
            f"{Fore.LIGHTMAGENTA_EX}Are you comfortable entering a first name or user name? " +
            f"{Fore.LIGHTGREEN_EX}Type anything for yes {Fore.LIGHTRED_EX}or enter for no.  {Fore.RESET}"):
        with open("user.txt", "wt", encoding="utf-8") as user:
            written_name = input(f"{Fore.LIGHTWHITE_EX}Please enter your name.  {Fore.RESET}")
            generated_id = str(max([int(row[2]) for row in worksheet.get_all_values()[1:]]) + 1)
            user.write(written_name + "\n" + generated_id)
            global uname, uid
            uname = written_name
            uid = generated_id

    with open("saved/list.txt", "wt", encoding="utf-8") as names, \
            open("saved/latest.txt", "wt", encoding="utf-8") as numbers:
        keep_counter = 0
        keep_list = []
        for manga in mangas:
            title = manga[0]
            if input(f"\n\n{Fore.LIGHTYELLOW_EX}Would you like to keep {title} on your list? " +
                     f"\n{Fore.LIGHTGREEN_EX}Type anything for yes {Fore.LIGHTRED_EX}or enter for no.  {Fore.RESET}"):
                keep_list.append(title)
                keep_counter += 1
                names.write("|".join(manga))
                print(f"{Fore.GREEN}Note: If you would like to quickly set up a new \"0 yts\" manga, "
                      + "please press enter without any input for both of the following")
                verify_status(numbers)
    add_to_sheet("primer", keep_counter, keep_list)
    print(f"{Fore.LIGHTGREEN_EX}Well Done! You've primed your personal MQuicker.{Fore.RESET}")
    set_changes(mangas, current)


def add():
    # Quickly add new manga information in both list.txt and latest.txt
    add_counter = 0
    add_list = []
    with open("saved/list.txt", "at", encoding="utf-8") as names, \
            open("saved/latest.txt", "at", encoding="utf-8") as numbers:
        continuation = "Yep"
        while continuation:
            add_counter += 1
            print(f"{Fore.LIGHTWHITE_EX}Please enter all of the following information for the manga you'd like to add")
            title = input(f'{Fore.RESET}Name  ')
            add_list.append(title)
            while True:
                link_var, source_var = input('Link  '), input('Source (see supported source codes)  ')
                if link_var[:8] == "https://" and "." in link_var and source_var in source_methods:
                    break
                else:
                    print(f"{Fore.LIGHTRED_EX}Please enter a valid link and supported source code.  {Fore.RESET}")
            names.write(f"{title}|{link_var}|{source_var}|\n")
            # numbers.write(f"{input('Current Chapter  ')} {input('Status (yts/wip/utd)  ')}\n")
            verify_status(numbers)
            continuation = input(
                f"{Fore.LIGHTRED_EX}Press enter to quit {Fore.LIGHTGREEN_EX}or type anything into the input to continue adding manga  {Fore.RESET}")
    add_to_sheet("add manga", add_counter, add_list)
    set_changes(mangas, current)

    return ("add manga", add_counter, add_list)


# Rate/Recommend Interlude
def rate():
    # The rate function collects user ratings to help build a database for a future recommend feature
    rate_list = []
    for manga in mangas:
        if input(f"\n{Fore.LIGHTYELLOW_EX}Would you like to rate {manga[0]}? " +
                 f"{Fore.LIGHTGREEN_EX}Type anything for yes {Fore.LIGHTRED_EX}or simply press enter for no.  {Fore.RESET}"):
            ratings = [manga[0]]
            for scale in ["Overall", "Plot", "Action", "Romance", "Comedy", "Art"]:
                ratings.append(float(input(
                    f"\n{Fore.LIGHTMAGENTA_EX}How would you rate {manga[0]}'s {scale} on a scale of 1 - 10? {Fore.RESET}")))
            for boolean in ["Family Friendly", "Happy"]:
                ratings.append(float(input(f"\n{Fore.LIGHTMAGENTA_EX}Did you find {manga[0]} {boolean} " +
                                           f"{Fore.LIGHTGREEN_EX}Type 1 for yes {Fore.LIGHTRED_EX}and 0 for no  {Fore.RESET}")))
            rate_list.append(ratings)
    add_to_sheet("rate", mlst=rate_list)