import csv

def load_resources(filename):
    resources = []

    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                resources.append(row)
    except FileNotFoundError:
        print("Error: resources.csv file was not found.")

    return resources


def search_resources(resources, search_term):
    matches = []
    search_term = search_term.lower().strip()

    for resource in resources:
        if (
            search_term in resource["zip_code"].lower()
            or search_term in resource["type"].lower()
            or search_term in resource["name"].lower()
        ):
            matches.append(resource)

    return matches


def display_results(matches):
    if not matches:
        print("\nNo resources found.")
        print("Try searching by ZIP code, food pantry, or community support.")
        return

    print(f"\n{len(matches)} resource(s) found:\n")

    for resource in matches:
        print(f"Name: {resource['name']}")
        print(f"Type: {resource['type']}")
        print(f"Address: {resource['address']}")
        print(f"ZIP Code: {resource['zip_code']}")
        print(f"Phone: {resource['phone']}")
        print(f"Hours: {resource['hours']}")
        print("-" * 45)


def main():
    print("Community Resource Finder")
    print("Find food assistance and community resources near you.")

    resources = load_resources("resources.csv")

    if not resources:
        return

    while True:
        search_term = input("\nSearch by ZIP code, name, or resource type: ")

        results = search_resources(resources, search_term)
        display_results(results)

        again = input("\nWould you like to search again? yes/no: ").lower()

        if again != "yes":
            print("\nThank you for using Community Resource Finder.")
            break


if __name__ == "__main__":
    main()
