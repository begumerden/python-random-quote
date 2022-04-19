import random
def primary():
    more_content = "Your time is limited, so don't waste it living someone else's life"

    print("Opening a file.")
    f = open("quotes.txt", "a+")
    quotes = f.readlines()

    iterate(quotes)
    print("New Content Added to File")

    iterate(quotes)

    f.write(more_content)
    f.close()

    iterate(quotes)


def iterate(quotes):
    for i in range(len(quotes)):
        rnd = random.randint(0, i)
        print(quotes[rnd].replace("\n", ","))


if __name__ == "__main__":
    primary()
