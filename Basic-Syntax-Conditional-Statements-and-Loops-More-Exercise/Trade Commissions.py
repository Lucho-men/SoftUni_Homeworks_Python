city = input()
sales = float(input())

if city == "Sofia" or city == "Varna" or city == "Plovdiv":
    if sales >= 0:
        if city == "Sofia":
            if sales >= 0 and sales <= 500:
                print(f"{0.05*sales:0.2f}")
            if sales > 500 and sales <= 1000:
                print(f"{0.07*sales:0.2f}")
            if sales > 1000 and sales <= 10000:
                print(f"{0.08*sales:0.2f}")
            if sales > 10000:
                print(f"{0.12*sales:0.2f}")

        if city == "Varna":
            if sales >= 0 and sales <= 500:
                print(f"{0.045*sales:0.2f}")
            if sales > 500 and sales <= 1000:
                print(f"{0.075*sales:0.2f}")
            if sales > 1000 and sales <= 10000:
                print(f"{0.10*sales:0.2f}")
            if sales > 10000:
                print(f"{0.13*sales:0.2f}")

        if city == "Plovdiv":
            if sales >= 0 and sales <= 500:
                print(f"{0.055*sales:0.2f}")
            if sales > 500 and sales <= 1000:
                print(f"{0.08*sales:0.2f}")
            if sales > 1000 and sales <= 10000:
                print(f"{0.12*sales:0.2f}")
            if sales > 10000:
                print(f"{0.145*sales:0.2f}")
    else:
        print("error")
else:
    print("error")