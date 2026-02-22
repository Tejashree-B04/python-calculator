# calculator 

import tkinter

button_values = [
    ["AC","+/-","%","÷"],
    ["7","8","9","×"],
    ["4","5","6","-"],
    ["1","2","3","+"],
    ["0",".","√","="],
]

right_symbols = ["÷","×","-","+","="]
top_symbols = ["AC","+/-","%"]

row_count = len(button_values) #5
column_count =len(button_values[0]) #4

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white"

#window setup
window = tkinter.Tk() # create the window
window.title("calculator")
window.resizable(False,False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0" , font=("Arial",45) , background=color_black , foreground=color_white, anchor="e", width=column_count)

label.grid(row=0 , column=0, columnspan=column_count, sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30),
                                width=column_count-1, height=1,
                                command=lambda value=value: button_clicked(value))
        if value in top_symbols:
            button.config(foreground=color_black, background=color_light_gray)
        elif value in right_symbols:
            button.config(foreground=color_white,background=color_orange)
        else :
            button.config(foreground=color_white, background=color_dark_gray)
        button.grid(row=row+1 , column=column)

frame.pack()

#A+B, A-B, A*B, A/B

# Initialize global variables
A = "0"
operator = None
B = None

def clear_all():
    global A,B, operator
    A = "0"
    operator = None
    B = None

def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)

def button_clicked(value):
    global right_symbols, top_symbols, label, A, B, operator

    if value in right_symbols:
        if value == "=":
            if operator is not None:
                try:
                    B = label["text"]
                    numA = float(A)
                    numB = float(B)

                    if operator == "+":
                        result = numA + numB
                    elif operator == "-":
                        result = numA - numB
                    elif operator == "×":
                        result = numA * numB
                    elif operator == "÷":
                        if numB != 0:
                            result = numA / numB
                        else:
                            label["text"] = "Error"
                            clear_all()
                            return
                    
                    label["text"] = remove_zero_decimal(result)
                    A = label["text"]
                    operator = None
                    B = None
                except Exception as e:
                    label["text"] = "Error"
                    clear_all()
                    
                    


            
        elif value in "+-×÷":
            # If there's already an operator, calculate the previous operation first
            if operator is not None:
                try:
                    B = label["text"]
                    numA = float(A)
                    numB = float(B)

                    if operator == "+":
                        result = numA + numB
                    elif operator == "-":
                        result = numA - numB
                    elif operator == "×":
                        result = numA * numB
                    elif operator == "÷":
                        if numB != 0:
                            result = numA / numB
                        else:
                            label["text"] = "Error"
                            clear_all()
                            return
                    
                    label["text"] = remove_zero_decimal(result)
                    A = label["text"]
                except Exception as e:
                    label["text"] = "Error"
                    clear_all()
            
            # Set up for new operation
            A = label["text"]
            operator = value
            label["text"] = "0" 

    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)
        
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)
            
    

    else: #digits or . or other buttons like √
        if value == "√":
            try:
                num = float(label["text"])
                if num >= 0:
                    result = num ** 0.5
                    label["text"] = remove_zero_decimal(result)
                else:
                    label["text"] = "Error"
            except:
                label["text"] = "Error"
        elif value == ".":
            # Normal number entry
            if "." not in label["text"]:
                if label["text"] == "0":
                    label["text"] = "0."
                else:
                    label["text"] += value
        elif value in "0123456789":
            # Get current display value
            current_text = label["text"]
            # If operator is None, we're either in initial state or just finished a calculation
            if operator is None:
                # If display is "0", replace it
                if current_text == "0":
                    label["text"] = value
                else:
                    # Display shows a result from previous calculation
                    # Check if current display is the same as A (the stored result)
                    # If so, this is first digit after =, replace it
                    # Otherwise, we're continuing to type, so append
                    if A is not None and current_text == A:
                        # First digit after calculation, replace
                        label["text"] = value
                    else:
                        # Continuing to type a number, append
                        label["text"] = current_text + value
            # If operator is set, we're entering the second number
            elif current_text == "0":
                label["text"] = value
            else:
                label["text"] = current_text + value


#center the window
window.update() #update window with the new size dimensions
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int(screen_width  - window_width)//2
window_y = int(screen_height - window_height)//2

#format "(w)×(h)+(x)+(Y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


window.mainloop()