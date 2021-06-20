st = "1" + "0" * 90
print(st)
while '100' in st or "1" in st:
    if '100' in st:
        st = st.replace('100', '01')
    else:
        st = st.replace('1', '000')
print("ANS", st)
print("len:", len(st))
