import tkinter

#window
window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=400,height=400)
window.config(padx=50,pady=50)


#Heading Label
heading_label = tkinter.Label(text=("BMI CALCULATOR"),font=('arial',35,))
heading_label.config(padx=5,pady=5)
heading_label.pack()

#Weight Label
weight_label = tkinter.Label(text=("Enter Your Weight (kg)"),font=('arial',15,))
weight_label.config(padx=15,pady=15)
weight_label.pack()

#Weight Entry

def weight_value():
    try:
        value_1 = float(weight_entry.get())
        print(value_1)
        return value_1
    except ValueError:
        print("Please enter a valid number !")
        return None


weight_entry = tkinter.Entry(width=25)
weight_entry.pack()

#Height Label
height_label = tkinter.Label(text=("Enter Your Height (cm)"),font=('arial',15,))
height_label.config(padx=15,pady=15)
height_label.pack()

#Height Entry

def height_value():
    try:
        value_2 = float(height_entry.get())
        print(value_2)
        return value_2
    except ValueError:
        print("Please enter a valid number !")
        return None

height_entry = tkinter.Entry(width=25)
height_entry.pack()

#Calculate Button

def calculate_main():
    h = height_value()
    w = weight_value()

    if h is None or w is None:
        result_label.config(text="Please enter a valid number!")
        result_label.pack()
        return

    h = h /100
    result = round(w / (h ** 2),2)
    if result < 18.5:
        comment = "Underweight"
    elif result < 25:
        comment = "Normal"
    elif result < 30:
        comment = "Overweight"
    else:
        comment = "Obese"

    print(result)
    result_label.config(text=f"Result: {result} → {comment}")
    result_label.pack()

calculate_button = tkinter.Button(text="Calculate",width=20,height=2,command=calculate_main)
calculate_button.pack(padx=20,pady=20)

#Result Label

result_label = tkinter.Label(text="Result:",font=('arial',25))
result_label.config(padx=10,pady=10)

window.mainloop()

