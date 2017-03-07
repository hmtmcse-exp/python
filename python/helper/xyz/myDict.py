

if __name__ == '__main__':
    x = dict()
    x["Name"] = "Touhid"
    print(x["Name"])
    x.pop("Name")

    if "Name" in x:
        print(x["Name"])
    else:
        print("Nai Nai")
