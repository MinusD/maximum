st = '8' * 100 + '1'
while '133' in st or '881' in st:
    if '133' in st:
        st = st.replace('133', '81')
    else:
        st = st.replace('881', '13')
print(st)
