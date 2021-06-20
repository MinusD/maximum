st = str('444444444' + '5' * 12)
while st.find('444') >= 0 or st.find('888') >= 0:
    if st.find('444') >= 0:
        st = st.replace('444', '8', 1)
    else:
        st = st.replace('888', '2', 1)
    while st.find('555') >= 0:
        st = st.replace('555', '8', 1)
        
    if st.find('888') >= 0:
        st = st.replace('888', '3', 1)
    print(st)
print(st)
