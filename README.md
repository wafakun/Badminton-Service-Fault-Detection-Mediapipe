Sistem Deteksi Service Fault Badminton Berbasis Image Processing
Sistem ini menggunakan metode machine learning dimana fungsi cascade dilatih dari banyak citra positif dan citra negatif yang berfungsi untuk mendeteksi shuttlecock
Kemudian memanfaat mediapipe pose untuk mendeteksi pose dan mengambil titik koordinat pada pergelangan tangan sebagai penentu pelanggaran servis. 
Apabila pemain melakukan servis melebihi 115cm yang ditandai garis horizontal berwarna putih maka sistem akan mendeteksi pelanggaran
Sistem akan mengirimkan notifikasi berupa suara dan mengambil screenshoot saat pemain melakukan pelanggaran, sebagai bukti bahwa terjadi pelanggaran servis yang dilakukan oleh pemain
### Vidio Demo
https://youtu.be/JdUaKTmDCkw
### Reference
https://github.com/cansik/multi-pose-landmark-mediapipe.git
