# BabbleSort-MPI

Anata Ryu Ilhami (09011382126168)

Agung Rizqi Ramadhan (09011382126157)

Nanda Apriadi (09011382126170)

program ini memerlukan 1 komputer yang bertindak sebagai master dan beberapa komputer lain yang bertindak sebagai slave

UNTUK SLAVE

pastikan sudah menginstal NFS Client dan sudah melakukan mounting dengan perintah

sudo mount serverhost:/lokasi/shared/folder/server /lokasi/shared/folder/client

untuk menjalankan program masukan perintah ini di MASTER

mpirun -np "jumlah prosesor" -host "daftar host" python3 Bubblesort.py
