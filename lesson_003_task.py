import csv, json

f1 = lambda x: x / (x + 100)
f2 = lambda x: 1 / x
f3 = lambda x: 20 * ( f1(x) + f2(x) ) / x

def range_gen(start, stop, step=1):
    i = start
    while i < stop:
        yield i
        i += step

def main():

    dict_x = {x: [f1(x), f2(x), f3(x)] for x in range_gen(5,90)}

    with open('dict_x.csv', mode='w') as csv_file:   
        field_names = ['x', 'f1(x)', 'f2(x)', 'f3(x)']
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writerow(field_names)
        
        for k,v in dict_x.items():
            csv_writer.writerow([k] + v)
    
    list_x = []
    with open('dict_x.csv') as csv_file:
        csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        next(csv_reader)
    
        for line in csv_reader:
            list_x.append(line)

    with open('list_x.json', 'w') as json_file:
        json.dump(list_x, json_file, indent=4)

if __name__ == "__main__":
    main()