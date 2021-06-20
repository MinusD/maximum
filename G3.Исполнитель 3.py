st = str('5' * 44 + '3')
while st.find('322') >= 0 or st.find('553') >= 0:
    if st.find('322') >= 0:
        st = st.replace('322', '53', 1)
    else:
        st = st.replace('553', '32', 1)
    print(st)
print(st)
