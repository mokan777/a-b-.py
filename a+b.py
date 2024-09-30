input_data = open('input.txt', 'r')


data = data.split()
a = int(data[0])
b = int(data[1])
c = str(a+b)



output_data = open('output.txt', 'r')
                   

output_data.write(c)
input_data.close()
