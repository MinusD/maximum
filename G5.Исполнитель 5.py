st = str('1' * 80)
while st.find('11111') >= 0 or st.find('888') >= 0:
    if st.find('11111') >= 0:
        st = st.replace('11111', '88', 1)
    elif st.find('888') >= 0:
        st = st.replace('888', '8', 1)
    print(st)
print(st)
