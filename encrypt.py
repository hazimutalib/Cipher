import pandas as pd
import streamlit as st
import sys


st.set_page_config(layout="wide")
st.write(""" # IC Encryption""")
column = st.columns([2,1])
column[0].warning(""" ###### File type accepted is only in Excel or CSV format. The first column needs to be the IC column.""")


def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index = False).encode('utf-8')


def encrypt_digit_additive_inverse(digit,i):
    x = 10 - int(digit[i])
    if x == 10:
        x = 0
    return x


def encrypt_number_additive_inverse(number):
    y = ''
    number = str(int(number))
    if len(number) == 12:
        for i in range(len(number)):
            y = y + str(encrypt_digit_additive_inverse(number,i))
    else:
        y = number        
    
    return y


def encrypt_digit_shifting_backwards(digit,i):
    x = (int(digit[i])-(i+1))%10
    return x


def encrypt_number_shifting_backwards(number):
    y = ''
    number = str(int(number))
    if len(number) == 12:
        for i in range(len(number)):
            y = y + str(encrypt_digit_shifting_backwards(number,i))
    else:
        y = number     
        
    return y


def decrypt_digit_shifting_backwards(digit,i):
    x = (int(digit[i])+(i+1))%10
    return x


def decrypt_number_shifting_backwards(number):
    y = ''
    number = str(int(number))
    for i in range(len(number)):
        y = y + str(decrypt_digit_shifting_backwards(number,i))    
    return y


def encryption_additive_inverse():
    column = st.columns([2,1])
    uploaded_file = column[0].file_uploader("Choose a file", accept_multiple_files=False)
    column = st.columns([1,1,1])
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        ic_number = df.columns[0]
        df[ic_number] = df[ic_number].astype('str')
        column[0].write(""" ### Original """)  
        column[0].write(df)
        df[ic_number] = df[ic_number].apply(lambda x: encrypt_number_additive_inverse(x))
        column[1].write(""" ### Encrypted """)  
        column[1].write(df)
        csv = convert_df(df)

        column[1].download_button(
            label="Download data as CSV",
            data=csv,
            file_name='encrypted_additive_inverse.csv',
            mime='text/csv',
        )

def decryption_additive_inverse():
    column = st.columns([2,1])
    uploaded_file = column[0].file_uploader("Choose a file", accept_multiple_files=False)
    column = st.columns([1,1,1])
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
        except:
            df = pd.read_csv(uploaded_file)
        ic_number = df.columns[0]
        df[ic_number] = df[ic_number].astype('str')
        column[0].write(""" ### Original """)  
        column[0].write(df)
        df[ic_number] = df[ic_number].apply(lambda x: encrypt_number_additive_inverse(x))
        column[1].write(""" ### Decrypted """)  
        column[1].write(df)
        csv = convert_df(df)

        column[1].download_button(
            label="Download data as CSV",
            data=csv,
            file_name='decrypted_additive_inverse.csv',
            mime='text/csv',
        )

def encryption_shifting_backwards():
    column = st.columns([2,1])
    uploaded_file = column[0].file_uploader("Choose a file", accept_multiple_files=False)
    column = st.columns([1,1,1])
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
        except:
            df = pd.read_csv(uploaded_file)
        ic_number = df.columns[0]
        df[ic_number] = df[ic_number].astype('str')
        column[0].write(""" ### Original """)  
        column[0].write(df)
        df[ic_number] = df[ic_number].apply(lambda x: encrypt_number_shifting_backwards(x))
        column[1].write(""" ### Encrypted""")  
        column[1].write(df)
        csv = convert_df(df)

        column[1].download_button(
            label="Download data as CSV",
            data=csv,
            file_name='encrypted_shifting_backwards.csv',
            mime='text/csv',
        )

def decryption_shifting_backwards():
    column = st.columns([2,1])
    uploaded_file = column[0].file_uploader("Choose a file", accept_multiple_files=False)
    column = st.columns([1,1,1])
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
        except:
            df = pd.read_csv(uploaded_file)
        ic_number = df.columns[0]
        df[ic_number] = df[ic_number].astype('str')
        column[0].write(""" ### Original """)  
        column[0].write(df)
        df[ic_number] = df[ic_number].apply(lambda x: decrypt_number_shifting_backwards(x))
        column[1].write(""" ### Decrypted """)  
        column[1].write(df)
        csv = convert_df(df)

        column[1].download_button(
            label="Download data as CSV",
            data=csv,
            file_name='decrypted_shifting_backwards.csv',
            mime='text/csv',
        )

column = st.columns([1,1,1])
option1 = column[0].selectbox('Encryption of Decryption?',('Encryption', 'Decryption'))
option2 = column[1].selectbox('Method',('Additive Inverse Cipher', 'Shifting Backwards Cipher'))

if option1 == 'Encryption' and option2 == 'Additive Inverse Cipher':
    encryption_additive_inverse()

elif option1 == 'Encryption' and option2 == 'Shifting Backwards Cipher':
    encryption_shifting_backwards()

elif option1 == 'Decryption' and option2 == 'Additive Inverse Cipher':
    decryption_additive_inverse()

elif option1 == 'Decryption' and option2 == 'Shifting Backwards Cipher':
    decryption_shifting_backwards()




