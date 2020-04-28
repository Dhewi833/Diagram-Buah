import matplotlib.pyplot as plt
import identitas

   listNama = ["Farhan", "Randi", "Reny", "Eka"]
   listKelas = [8,8,8,8]  
   listIdentitas = []  
   for i in range(len(listkelas)):
       listIdentitas.append(Identitas.Identitas(listNama[i], listkelas[i]))

       print("Show all {}".format(listIdentitas))  

   for j in range(len(listIdentitas)):
       print(" Nama Siswa  : {} ".format(listIdentitas[j].show_nama()))
       print(" Kelas       : {} ".format(listIdentitas[j].show_kelas()))



def total_weight(list_weight):
    return sum(list_weight)

def degrees_fruits(list_fruits):
    result =[]

    
    for value in list_fruits:
        result.append((value/total_weight(list_weight))*360)
    return result

def do_piechart(list_degrees, list_fruits):
    fig1, ax1 = plt.subplots()
    ax1.pie(list_degrees, explode=None, labels=list_fruits,
            autopct='%1.1f%%', shadow=True, startangle=90)

    plt.show()
    plt.savefig('diagrambuah.png')

if __name__ =="__main__":

    list_fruits = []
    list_weight = []

    datasize = int(input("Jenis Buah : "))

    print("Masukkan jenis buah")
    for index in range(datasize):
        data_fruit = str(input("Buah: "))
        list_fruits.append(data_fruit)

    print("Masukkan Banyak Panen")
    for index in range(datasize):
        data_weight = int(input("Banyak Panen : "))
        list_weight.append(data_weight)

    print("Jenis Buah {}".format(list_fruits))
    print("Banyak Panen {}".format(list_weight))
    print("Total Panen {}".format(total_weight(list_weight)))

    list_degrees = degrees_fruits(list_weight)
    print("degrees fruits {}".format(list_degrees))

    do_piechart(list_degrees, list_fruits)
