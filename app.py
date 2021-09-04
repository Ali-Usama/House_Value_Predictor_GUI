from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial
import joblib
import pandas as pd
import numpy as np

cols = ['housing_median_age', 'total_rooms', 'rooms_per_house',
        'total_bedrooms', 'bedrooms_per_rooms', 'population', 'households',
        'population_per_household', 'median_income', 'ocean_proximity']

model = joblib.load('RandomForest.pkl')
scalarObj = joblib.load('scalar.pkl')

# from window2 import new_window
# from window2 import new_window

window = Tk()
window.configure(bg='green')
window.title('Login Window')

# setting the size of the geometry:
# Note that, first two parameters indicate the size of the created window;
# and the last two parameters indicate the position of window relative to the screen.

window.geometry('800x400+200+250')
window.resizable(True, True)

'''
# a messagebox to show the selected name:
def show_name(event):
    msg = f'{combo_box.get()} is selected.'
    ans = askokcancel(title='Confirmation', message=f'You are selecting {combo_box.get()}', icon=WARNING)
    if ans:
        messagebox.showinfo('Name selection', message=msg)
'''

# creating a header label
label = Label(window, text='LogIn Menu',
              font=('Times New Roman Bold', 25), bg='cyan', fg='blue')
label.place(relx=0.40)

# creating a username label:
usernameLabel = Label(window, text='Username',
                      font=('Times New Roman Bold', 30), bg='cyan', fg='blue')
usernameLabel.place(relwidth=0.30, relheight=0.08, relx=0.01, rely=0.19)

# creating a username field:
username = StringVar()
usernameEntry = Entry(window, textvariable=username)
usernameEntry.place(relwidth=0.30, relheight=0.08, relx=0.60, rely=0.19)


def login(name, psswd):
    if name.get() == 'Usama' and psswd.get() == '123':
        return new_window()
    else:
        messagebox.showinfo('Login Error', 'Username or password is incorrect')


# creating a password label:
passwordLabel = Label(window, text='Password',
                      font=('Times New Roman Bold', 30), bg='cyan', fg='blue')
passwordLabel.place(relwidth=0.30, relheight=0.08, relx=0.01, rely=0.40)

# creating a password field:
password = StringVar()
passwordEntry = Entry(window, textvariable=password, show='*')
passwordEntry.place(relwidth=0.30, relheight=0.08, relx=0.60, rely=0.40)

# creating a check button:
check_button = Checkbutton(window, text='Remember me',
                           font=('Times New Roman', 15),
                           height=1, width=10)
check_button.place(relx=0.56, rely=0.56)

# creating a login button:
login = partial(login, username, password)
loginButton = Button(window, text='Login', command=login,
                     font=('Times New Roman Bold', 30), bg='cyan', fg='blue')

loginButton.place(relwidth=0.25, relheight=0.15, relx=0.35, rely=0.69)

# creating an exit button:
exit_btn = Button(window, text='EXIT', command=window.destroy,
                  font=('Times New Roman', 20), bg='cyan', fg='red')
exit_btn.place(relwidth=0.20, relheight=0.15, relx=0.8, rely=0.85)

# defining a new window which will accept values from the user:
def new_window():
    branch = Toplevel(window)
    branch.title('Predict House Prices')
    branch.geometry('800x400+250+350')
    branch.configure(bg='blue')
    branch.resizable(True, True)

    label2 = Label(branch, text='Please fill values in the following fields!', font=('Times New Roman', 18))
    label2.place(relx=0.20)

    housing_age = Label(branch, text='House Median Age', font=('Times New Roman', 15),
                        bg='red', fg='cyan')
    housing_age.place(relwidth=0.30, relheight=0.05, relx=0.01, rely=0.10)
    value1 = StringVar()
    housing_age_entry = Entry(branch, textvariable=value1)
    # housing_age_entry.insert(0, '1.0 - 52.0')
    # housing_age_entry.bind("<FocusIn>", lambda args: housing_age_entry.delete('0', 'end'))
    housing_age_entry.place(relwidth=0.15, relheight=0.05, relx=0.50, rely=0.10)

    tot_rooms = Label(branch, text='Total Rooms', font=('Times New Roman', 15),
                      bg='red', fg='cyan')
    tot_rooms.place(relwidth=0.30, relheight=0.05, relx=0.01, rely=0.18)
    value2 = StringVar()
    tot_rooms_entry = Entry(branch, textvariable=value2)
    # tot_rooms_entry.insert(0, '2.0 - 40000.0')
    # tot_rooms_entry.bind("<FocusIn>", lambda args: tot_rooms_entry.delete('0', 'end'))
    tot_rooms_entry.place(relwidth=0.15, relheight=0.05, relx=0.50, rely=0.18)

    rooms_per_house = Label(branch, text='Rooms per House', font=('Times New Roman', 15),
                            bg='red', fg='cyan')
    rooms_per_house.place(relwidth=0.30, relheight=0.05, relx=0.01, rely=0.26)
    value3 = StringVar()
    rooms_per_house_ent = Entry(branch, textvariable=value3)
    # rooms_per_house_ent.insert(0, '1.0 - 140.0')
    # rooms_per_house_ent.bind("<FocusIn>", lambda args: rooms_per_house_ent.delete('0', 'end'))
    rooms_per_house_ent.place(relwidth=0.15, relheight=0.05, relx=0.50, rely=0.26)

    tot_bedrooms = Label(branch, text='Total Bedrooms', font=('Times New Roman', 15),
                         bg='red', fg='cyan')
    tot_bedrooms.place(relwidth=0.30, relheight=0.05, relx=0.01, rely=0.34)
    value4 = StringVar()
    tot_bedrooms_entry = Entry(branch, textvariable=value4)
    # tot_bedrooms_entry.insert(0, '1.0 - 6445.0')
    # tot_bedrooms_entry.bind("<FocusIn>", lambda args: tot_bedrooms_entry.delete('0', 'end'))
    tot_bedrooms_entry.place(relwidth=0.15, relheight=0.05, relx=0.50, rely=0.34)

    bed_per_rooms = Label(branch, text='Bedrooms per Rooms', font=('Times New Roman', 15),
                          bg='red', fg='cyan')
    bed_per_rooms.place(relwidth=0.30, relheight=0.05, relx=0.01, rely=0.42)
    value5 = StringVar()
    bed_per_rooms_entry = Entry(branch, textvariable=value5)
    # bed_per_rooms_entry.insert(0, '0.0 - 1.0')
    # bed_per_rooms_entry.bind("<FocusIn>", lambda args: bed_per_rooms_entry.delete('0', 'end'))
    bed_per_rooms_entry.place(relwidth=0.15, relheight=0.05, relx=0.50, rely=0.42)

    population = Label(branch, text='Total Population', font=('Times New Roman', 15),
                       bg='red', fg='cyan')
    population.place(relwidth=0.30, relheight=0.05, relx=0.01, rely=0.50)
    value6 = StringVar()
    population_entry = Entry(branch, textvariable=value6)
    # population_entry.insert(0, '3.0 - 35680.0')
    # population_entry.bind("<FocusIn>", lambda args: population_entry.delete('0', 'end'))
    population_entry.place(relwidth=0.15, relheight=0.05, relx=0.50, rely=0.50)

    households = Label(branch, text='Households', font=('Times New Roman', 15),
                       bg='red', fg='cyan')
    households.place(relwidth=0.30, relheight=0.05, relx=0.01, rely=0.58)
    value7 = StringVar()
    households_entry = Entry(branch, textvariable=value7)
    # households_entry.insert(0, '1.0 - 6080.0')
    # households_entry.bind("<FocusIn>", lambda args: households_entry.delete('0', 'end'))
    households_entry.place(relwidth=0.15, relheight=0.05, relx=0.50, rely=0.58)

    pop_per_household = Label(branch, text='Population per Household', font=('Times New Roman', 15),
                              bg='red', fg='cyan')
    pop_per_household.place(relwidth=0.30, relheight=0.05, relx=0.01, rely=0.66)
    value8 = StringVar()
    pop_per_household_entry = Entry(branch, textvariable=value8)
    # pop_per_household_entry.insert(0, '0.0 - 1240.0')
    # pop_per_household_entry.bind("<FocusIn>", lambda args: pop_per_household_entry.delete('0', 'end'))
    pop_per_household_entry.place(relwidth=0.15, relheight=0.05, relx=0.50, rely=0.66)

    med_income = Label(branch, text='Median Income', font=('Times New Roman', 15),
                       bg='red', fg='cyan')
    med_income.place(relwidth=0.30, relheight=0.05, relx=0.01, rely=0.74)
    value9 = StringVar()
    med_income_entry = Entry(branch, textvariable=value9)
    # med_income_entry.insert(0, '0.0 - 15.0K')
    # med_income_entry.bind("<FocusIn>", lambda args: med_income_entry.delete('0', 'end'))
    med_income_entry.place(relwidth=0.15, relheight=0.05, relx=0.50, rely=0.74)

    ocean_proximity = Label(branch, text='Ocean Proximity', font=('Times New Roman', 15),
                            bg='red', fg='cyan')
    ocean_proximity.place(relwidth=0.30, relheight=0.05, relx=0.01, rely=0.82)

    # creating a combobox:
    names = StringVar()
    combo_box = ttk.Combobox(branch, textvariable=names)
    combo_box['values'] = ['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN']
    combo_box.place(relwidth=0.15, relheight=0.05, relx=0.50, rely=0.82)
    combo_box.bind('<<ComboboxSelected>>')
	
	# creating a dataframe from the input values
    def df_final():
        attr_array = np.array(
            [value1.get(), value2.get(), value3.get(), value4.get(), value5.get(), value6.get(), value7.get(),
             value8.get(), value9.get(), combo_box.get()])
        final_df = pd.DataFrame([attr_array], columns=cols)
		
		# manually encoding the 'ocean proximity values'
		
        final_df['ocean_proximity'] = final_df['ocean_proximity'].apply(lambda x: 3.0 if x == 'NEAR BAY' else (
            0.0 if x == '<1H OCEAN' else (1.0 if x == 'INLAND' else (2.0 if x == 'ISLAND' else 4.0))))

        cat_cols = final_df.select_dtypes(include='object').columns
        final_df[cat_cols] = final_df[cat_cols].astype('float') 		# converting the object columns to float.
        return final_df

	# applying the randomforestresgression model.
    def predict(df):
        # cat_cols = [col for col in df.columns if df[col].dtypes == 'object']
        num_cols = [col for col in df.columns if col != 'ocean_proximity']

        arr1 = df[num_cols].values.reshape(-1, 1)
        
        # applying standard scalar:
        scaled_arr = scalarObj.fit_transform(arr1)
        encoded_arr = np.array([df['ocean_proximity'].values])

        X_valid1 = np.concatenate((scaled_arr, encoded_arr))

        preds = model.predict(X_valid1.T)
        return preds[0]
	
	# creating a prediction window, which will show the output:
    def preds_window():
        preds = Toplevel(window)
        preds.title('House value Predictions')
        preds.geometry('600x300+280+350')

        preds_label = Label(preds, text=f'The value of this house is ${int(predict(df_final()))}',
                            font=('Times New Roman', 20))
        preds_label.place(relx=0.17)

        ok_btn = Button(preds, text='OK', font=('Times New Roman', 20), command=preds.destroy, bg='cyan', fg='red')
        ok_btn.place(relwidth=0.20, relheight=0.10, relx=0.45, rely=0.54)

    pred_btn = Button(branch, text='Predict Value', command=preds_window, font=('Times New Roman', 20),
                      bg='cyan', fg='red')
    pred_btn.place(relwidth=0.25, relheight=0.25, relx=0.70, rely=0.40)

    branch.mainloop()


window.mainloop()
