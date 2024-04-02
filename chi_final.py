import csv
import tkinter as tk
from tkinter import simpledialog
from tkinter import ttk


#main window
root = tk.Tk()
root.title("Car Selection")
root.geometry("900x400")

#label
brand_on = tk.IntVar()
year_on = tk.IntVar()

brand_label = tk.Label(root, text = "You entered:")
brand_label.place(x=350,y=30)

year_label = tk.Label(root, text = "You entered:")
year_label.place(x=350,y=70)

mileage_label = tk.Label(root, text = "enter your annual mileage")
mileage_label.place (x=100,y=10)

yearly_label = tk.Label(root, text = "enter years before change")
yearly_label.place (x=100,y=50)

result_brand = tk.Entry(root,state = tk.DISABLED)
result_brand.place(x=100,y=30)

result_year = tk.Entry(root,state = tk.DISABLED)
result_year.place(x=100,y=70)

final_result = tk.Label(root, text = "")
final_result.place(x=300,y=150)

#button callback function
def start_search():
    button.config(text="Success!")
    reset.config(text="Reset")
    _annual = get_brand()
    _year = get_year()

    if _annual:
        _annual = get_brand()
    else:
        _annual = 8000

    if _year:
        _year = get_year()
    else: 
        _year = 5
    
    final_result.config(text=cheapest_car('merged_cars.csv',_annual, _year))


# Function to read unique models for Audi from CSV
def read_audi_models():
    audi_models_set = set()
    with open('audi.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            model = row['model']
            audi_models_set.add(model)
    return list(audi_models_set)

def read_bmw_models():
    bmw_models_set = set()
    with open('bmw.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            model = row['model']
            bmw_models_set.add(model)
    return list(bmw_models_set)

def read_ford_models():
    ford_models_set = set()
    with open('ford.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            model = row['model']
            ford_models_set.add(model)
    return list(ford_models_set)

def read_hyundai_models():
    hyundai_models_set = set()
    with open('hyundai.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            model = row['model']
            hyundai_models_set.add(model)
    return list(hyundai_models_set)

def read_merc_models():
    merc_models_set = set()
    with open('merc.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            model = row['model']
            merc_models_set.add(model)
    return list(merc_models_set)

def read_skoda_models():
    skoda_models_set = set()
    with open('skoda.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            model = row['model']
            skoda_models_set.add(model)
    return list(skoda_models_set)

def read_toyota_models():
    toyota_models_set = set()
    with open('toyota.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            model = row['model']
            toyota_models_set.add(model)
    return list(toyota_models_set)

def read_vauxhall_models():
    vauxhall_models_set = set()
    with open('vauxhall.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            model = row['model']
            vauxhall_models_set.add(model)
    return list(vauxhall_models_set)

def read_vw_models():
    vw_models_set = set()
    with open('vw.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            model = row['model']
            vw_models_set.add(model)
    return list(vw_models_set)

def read_year_for_model(selected_make, selected_model):
    year_set = set()
    try:
        with open(f'{selected_make.lower()}.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row.get('model') == selected_model:
                    year = row.get('year')  # Change 'Year' to 'year'
                    if year:
                        year_set.add(year)
    except FileNotFoundError:
        print(f"File not found: {selected_make.lower()}.csv")
    return list(year_set)

# Auto-fill the audi_models array
audi_models = read_audi_models()
bmw_models = read_bmw_models()
ford_models = read_ford_models()
hyundai_models = read_hyundai_models()
merc_models = read_merc_models()
skoda_models = read_skoda_models()
toyota_models = read_toyota_models()
vauxhall_models = read_vauxhall_models()
vw_models = read_vw_models()

# Create DropBox
CarMake = ["Audi", "BMW", "Ford", "Hyundai", "Merc", "Skoda", "Toyota", "Vauxhall", "VW"]
my_combo = ttk.Combobox(root, value=CarMake)
my_combo.place(x=90,y=110)

# Model Combo Box
model_combo = ttk.Combobox(root, value="")
model_combo.place(x=90,y=150)

# Years Combo Box
year_combo = ttk.Combobox(root, value="")
year_combo.place(x=90,y=190)

# Callback function for car make selection
def pick_model(e):
    selected_make = my_combo.get()
    if selected_make == "Audi":
        model_combo.config(value=audi_models)
    elif selected_make == "BMW":
        model_combo.config(value=bmw_models)
    elif selected_make == "Ford":
        model_combo.config(value=ford_models)
    elif selected_make == "Hyundai":
        model_combo.config(value=hyundai_models)  
    elif selected_make == "Merc":
        model_combo.config(value=merc_models)  
    elif selected_make == "Skoda":
        model_combo.config(value=skoda_models)  
    elif selected_make == "Toyota":
        model_combo.config(value=toyota_models)  
    elif selected_make == "Vauxhall":
        model_combo.config(value=vauxhall_models)  
    elif selected_make == "VW":
        model_combo.config(value=vw_models)       
    else:
        model_combo.config(value=[])

# Callback function for model selection
def pick_year(e):
    selected_make = my_combo.get()
    selected_model = model_combo.get()
    print(f"Selected make: {selected_make}, Selected model: {selected_model}")  # Debug print
    if selected_make and selected_model:
        year = read_year_for_model(selected_make, selected_model)
        print(f"Available year: {year}")  # Debug print
        year_combo.config(value=year)
    else:
        year_combo.config(value=[])


# Bind Comboboxes
my_combo.bind("<<ComboboxSelected>>", pick_model)
model_combo.bind("<<ComboboxSelected>>", pick_year)

# Details Label
details_label = tk.Label(root, text="")
details_label.place(x=100, y=100)

    


def reset_search():
    reset.config(text="reset finished")
    button.config(text="Search for cars!")
    final_result.config(text = "")
    brand_on = tk.IntVar()
    brand_label = tk.Label(root, text = "You entered:")
    result_brand = tk.Entry(root,state = tk.DISABLED)
    get_brand=8000
    get_year=5

def brand_button():
    current_state = brand_on.get()
    if current_state == 1:
        enable_brand()
    else:
        disable_brand()


def enable_brand():
    result_brand['state'] = tk.NORMAL
    input_button['state'] = tk.NORMAL

def disable_brand():
    result_brand.delete(0,tk.END)
    result_brand['state'] = tk.DISABLED
    input_button['state'] = tk.DISABLED

def year_button():
    current_state = year_on.get()
    if current_state == 1:
        enable_year()
    else:
        disable_year()


def enable_year():
    result_year['state'] = tk.NORMAL
    input_year['state'] = tk.NORMAL

def disable_year():
    result_year.delete(0,tk.END)
    result_year['state'] = tk.DISABLED
    input_year['state'] = tk.DISABLED

    

def get_brand():
    try: 
        user_input = result_brand.get()
        if (user_input != 0):
            print("mileage",user_input)
            brand_label.config(text=f"You entered: {user_input}")
            return user_input
 
        else:
            result_brand.config(text="No input provided")
            return 0
    except TypeError:
        print("int only")

def get_year():
    try: 
        user_input = result_year.get()
        if (user_input != 0):
            print("year",user_input)
            year_label.config(text=f"You entered: {user_input}")
            return user_input
        
        else:
            result_year.config(text="No input provided")
            return 0
    except TypeError:
        print("int only")  





brand_on_button = tk.Checkbutton(root, text = "toggle", variable = brand_on, command = brand_button)
brand_on_button.place(x=500,y=30)


input_button = tk.Button(root, text = "get input", command =get_brand)
input_button.place (x=250,y=30)

year_on_button = tk.Checkbutton(root, text = "toggle", variable = year_on, command = year_button)
year_on_button.place(x=500,y=70)

input_year = tk.Button(root, text = "get input", command =get_year)
input_year.place (x=250,y=70)



#create button
button = tk.Button(root, text="Search for cars!",height = 2, width = 20, command=start_search)
button.place(x=650,y=30)
reset = tk.Button(root, text="Reset",height = 2, width = 10, command=reset_search)
reset.place(x=800,y=30)


def cheapest_car(file_path, annual_mileage, year):
    calculated_value = []
    row_string = []
    years=int(year)
    with open (file_path, 'r', newline='') as f:
        reader = csv.reader(f)
        next(reader)
        # Extract values from the specified column
        for row in reader:
            price_value = row[3]
            tax_value = row[7]
            mpg_value = row[8]
            maintenance_price = row[10]
            if row[6] == "Petrol": 
                fuel_price = 1.4251
            else:
                fuel_price = 1.5090

            calculated = float(price_value) + float(tax_value) + float(annual_mileage)/float(mpg_value)*5.546*float(fuel_price) + float(maintenance_price)*years
            calculated_value.append(calculated)
            row_string.append(row)
        index_of_smallest = calculated_value.index(min(calculated_value))
        #print ("the cheapest option for 5 years is: ", row_string[index_of_smallest])
        #print ("for the cost of 5 years of :",min(calculated_value) )
        #print ("in line", index_of_smallest)
        return (f"cheapest value: {min(calculated_value)}\n"+f"make: {row_string[index_of_smallest][0]}\n"+f"model: {row_string[index_of_smallest][1]}\n"+f"year: {row_string[index_of_smallest][2]}\n"+f"price: {row_string[index_of_smallest][3]}\n"+f"transmission: {row_string[index_of_smallest][4]}\n"+f"mileage: {row_string[index_of_smallest][5]}\n"+f"fuel type: {row_string[index_of_smallest][6]}\n"+f"tax: {row_string[index_of_smallest][7]}\n"+f"mpg: {row_string[index_of_smallest][8]}\n"+f"engine size: {row_string[index_of_smallest][9]}\n"+f"yearly maintenance cost: {row_string[index_of_smallest][10]}\n"+f"in line{index_of_smallest}")




#Run
root.mainloop()
