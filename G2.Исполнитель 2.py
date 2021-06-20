st = str('1' + '5' * 60)
while st.find('15') >= 0 or st.find('255') >= 0 or st.find('3555') >= 0:
    if st.find('15') >= 0:
        st = st.replace('15', '2', 1)
    elif st.find('255') >= 0:
        st = st.replace('255', '3', 1)
    else:
        st = st.replace('3555', '1', 1)
    print(st)
print(st)
