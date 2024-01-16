from prettytable import PrettyTable

x = PrettyTable()
x.field_names= ["location", "language of pro" ,"rate"]

x.add_row([1,"python", 100])
x.add_row([1,"c", 98])
x.add_row([3,"java", 90])

print(x)