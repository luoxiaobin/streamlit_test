import pandas as pd
import numpy as np

def load_data(nrows):
    data = pd.read_csv("statement.csv",
        header=0,
        names=["First Bank Card",	"Transaction Type",	"Date Posted",	 "Transaction Amount", "Description"],
        parse_dates=["Date Posted"])    
    return data

data = load_data(10000)

print(f"Loaded statement data")
print (data)

di = {"'5510290010786688'":"BMO"}
print(data.replace({"First Bank Card": di}))

print('Number of transactions by month')
DATE_COLUMN="Date Posted"
print (np.histogram(data[DATE_COLUMN].dt.month, bins=12, range=(1,12))[0])

# Some number in the range 0-23
#hour_to_filter = st.slider('hour', 0, 23, 17)
#filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

#st.subheader('Map of all pickups at %s:00' % hour_to_filter)
#st.map(filtered_data)