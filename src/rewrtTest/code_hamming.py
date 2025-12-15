def code_hemming(mes: str) -> str:
    bin_view = []
    for i in mes:
        b = bin(ord(i))[2::]
        while len(b)<8:
            b = '0'+b
        bin_view.append(b)
    
    for i in range(len(bin_view)):
        bin_view[i] = "00"+bin_view[i][0]+"0"+bin_view[i][:4]+"0"+bin_view[i][4:]


    return bin_view

print(code_hemming("Hello"))