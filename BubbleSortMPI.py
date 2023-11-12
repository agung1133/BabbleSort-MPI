from mpi4py import MPI
import time

def bubble_sort_odd(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] % 2 == 1 and arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if _name_ == "_main_":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0:
        data = [9, 3, 7, 5, 1, 8, 4, 6, 2]
    else:
        data = None

    data = comm.bcast(data, root=0)

    # Menyortir angka ganjil pada setiap proses
    local_data = [x for x in data if x % 2 == 1]

    # Mulai mengukur waktu
    start_time = time.time()

    bubble_sort_odd(local_data)

    # Menghentikan pengukuran waktu
    end_time = time.time()

    # Mengumpulkan hasil dari setiap proses
    sorted_data = comm.gather(local_data, root=0)

    if rank == 0:
        result = []
        for sublist in sorted_data:
            result.extend(sublist)
        print("Hasil setelah disortir: ", result)

        # Menampilkan waktu eksekusi
        execution_time = end_time - start_time
        print("Waktu eksekusi: {:.6f} detik".format(execution_time))