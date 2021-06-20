st = '2' * 92
while st.find('222') >= 0 or st.find('888') >= 0:
    if st.find('222') >= 0:
        st = str(st.replace('222', '8', 1))
    else:
        st = str(st.replace('888', '2', 1))
    print(st)
print(st)
