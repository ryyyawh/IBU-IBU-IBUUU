import time
from termcolor import colored
from colorama import init

# Inisialisasi colorama
init()

# Lirik lagu "Ibu Ibu Ibu" ©® Pidi Baiq
lyrics = [
    "Kau mengajari aku mengucapkan kata-kata baru",
    "Kau menghendaki aku mengucapkan kata-kata bagus",
    "Kau adalah yang tidak membunuhku selagi masih janin",
    "Kau adalah yang tidak mengutukku hingga menjadi batu",
    "Kau tanyakan kabarku di saat aku tinggal jauh",
    "Kau adalah yang bimbang tanya dengan siapa aku pergi",
    "Kau adalah yang risau mengapa aku belum pulang",
    "Kau adalah yang malu di saat aku berbuat memalukan",
    "Kau adalah yang bilang dengan bangga bahwa aku anakmu",
    "Kau sebut nama aku pada tiap ucap doamu",
    "Kau jauh lebih tinggi daripada aneka macam sorga",
    "Kau adalah dirimu dengan getar ku panggil engkau ibu"
]

# Warna yang akan digunakan
colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']

# Menampilkan lirik dengan efek warna-warni
for line in lyrics:
    for color in colors:
        print(colored(line, color))
        time.sleep(0.5)  # Memberikan delay untuk efek warna
