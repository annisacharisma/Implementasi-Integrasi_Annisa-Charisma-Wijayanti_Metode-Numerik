import numpy as np
import time

# Mendefinisikan fungsi Integral 
def f(x):
    return 4 / (1 + x**2)

def simpson_1_3(a, b, N):
    h = (b - a) / N
    integral = f(a) + f(b)
    
    for i in range(1, N, 2):
        integral += 4 * f(a + i * h)
    for i in range(2, N-1, 2):
        integral += 2 * f(a + i * h)
        
    integral *= h / 3
    return integral

def rms_error(estimate, reference):
    error = (estimate - reference)**2
    return np.sqrt(error)

# Nilai referensi pi
reference_pi = 3.14159265358979323846

# Variasi dari nilai N
N_values = [10, 100, 1000, 10000]

# Menyimpan hasil estimasi, galat RMS, dan waktu eksekusi
results = []
execution_times = []
rms_errors = []

for N in N_values:
    start_time = time.time()
    estimate = simpson_1_3(0, 1, N)
    end_time = time.time()
    
    results.append(estimate)
    execution_times.append(end_time - start_time)
    
    # Menghitung galat RMS untuk nilai N saat ini
    rms_errors.append(rms_error(estimate, reference_pi))

# Hasil yang akan ditampilkan 
for N, result, error, exec_time in zip(N_values, results, rms_errors, execution_times):
    print(f"n={N}")
    print(f"nilai pi= {result}")
    print(f"ralat rms= {error}")
    print(f"waktu= {exec_time} detik\n")