import pandas as pd
import os

def load_data():
    try:
        # Show current folder (for debugging)
        print("Working Directory:", os.getcwd())

        # Correct way to read CSV file
        df = pd.read_csv("books.csv")
        return df

    except FileNotFoundError:
        print("Error: 'books.csv' file not found!")
        print("Make sure file is in same folder OR use full path")
        return None

    except Exception as e:
        print("Error:", e)
        return None


def display_all(df):
    print("\n--- Complete Book Report ---")
    print(df.to_string(index=False))


def search_author(df):
    name = input("Enter author name: ").strip().lower()
    result = df[df['author'].str.lower() == name]

    if result.empty:
        print("No books found!")
    else:
        print("\nBooks by author:")
        print(result[['title', 'author', 'price']].to_string(index=False))


def search_publisher(df):
    name = input("Enter publishing house: ").strip().lower()
    result = df[df['publishing_house'].str.lower() == name]

    if result.empty:
        print("No books found!")
    else:
        print("\nBooks from publisher:")
        print(result[['title', 'publishing_house', 'price']].to_string(index=False))


def cheapest_costliest(df):
    min_price = df['price'].min()
    max_price = df['price'].max()

    print("\nCheapest Book:")
    print(df[df['price'] == min_price][['title', 'price']].to_string(index=False))

    print("\nCostliest Book:")
    print(df[df['price'] == max_price][['title', 'price']].to_string(index=False))


def sort_books(df):
    sorted_df = df.sort_values(by='publication_year')
    print("\n--- Sorted by Publication Year ---")
    print(sorted_df[['title', 'publication_year', 'price']].to_string(index=False))


def main():
    df = load_data()
    if df is None:
        return

    while True:
        print("\n===== MENU =====")
        print("1. Display all books")
        print("2. Search by author")
        print("3. Search by publisher")
        print("4. Cheapest & Costliest book")
        print("5. Sort by year")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            display_all(df)
        elif choice == '2':
            search_author(df)
        elif choice == '3':
            search_publisher(df)
        elif choice == '4':
            cheapest_costliest(df)
        elif choice == '5':
            sort_books(df)
        elif choice == '6':
            print("Program ended.")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()