st = '*' + '7' * 58
while st.find('*77') >= 0 or st.find('*') >= 0:
    if st.find('*77') >= 0:
        st = str(st.replace('*77', '7*', 1))
    elif st.find('*') >= 0:
        st = str(st.replace('*', '777', 1))
    print(st)
print(len(st))
