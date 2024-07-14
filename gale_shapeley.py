#gale shapeley with user input
def gale_shapley(men_preferences, women_preferences, men_names, women_names):
    n = len(men_preferences)  # Number of men/women
    free_men = list(range(n))  # List of free men
    women_partners = [-1] * n  # Partner for each woman, -1 means no partner
    men_next_proposal = [0] * n  # Next woman to propose to for each man

    women_index = {name: i for i, name in enumerate(women_names)}

    while free_men:
        man = free_men.pop(0)
        woman_name = men_preferences[man][men_next_proposal[man]]
        woman = women_index[woman_name]
        men_next_proposal[man] += 1

        if women_partners[woman] == -1:
            women_partners[woman] = man
        else:
            current_partner = women_partners[woman]
            woman_prefers_new = women_preferences[woman].index(men_names[man]) < women_preferences[woman].index(men_names[current_partner])

            if woman_prefers_new:
                women_partners[woman] = man
                free_men.append(current_partner)
            else:
                free_men.append(man)

    matches = {women_names[woman]: men_names[man] for woman, man in enumerate(women_partners)}
    return matches

def get_preferences(num_people, names, role):
    preferences = []
    for name in names:
        print(f"Enter the preferences for {role} {name} (space-separated names of the other group in order of preference):")
        preferences.append(input().split())
    return preferences

def main():
    num_people = int(input("Enter the number of men/women: "))

    print("Enter the names of the men (space-separated):")
    men_names = input().split()

    print("Enter the names of the women (space-separated):")
    women_names = input().split()

    print("Enter the preferences for men:")
    men_preferences = get_preferences(num_people, men_names, "man")

    print("Enter the preferences for women:")
    women_preferences = get_preferences(num_people, women_names, "woman")

    matches = gale_shapley(men_preferences, women_preferences, men_names, women_names)

    print("The matches are:")
    for woman, man in matches.items():
        print(f"{woman} is matched with {man}")

if __name__ == "__main__":
    main()
