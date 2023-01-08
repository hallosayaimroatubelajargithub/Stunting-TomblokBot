import telebot 

from constants import API_KEY

bot = telebot.TeleBot(API_KEY, parse_mode=None)

@bot.message_handler(commands=["start"])
def send_help_message(msg):
    bot.reply_to(msg, "Selamat Datang Di Tanya Jawab Seputar Stunting : Cegah, Bukan Diobati!!")
    bot.reply_to(msg, "Ketik /rules Untuk Memulai Tanya Jawab")

@bot.message_handler(commands=["rules"])
def send_help_message(msg):
    bot.reply_to(msg, "Perkenalkan Ini Adalah Tomblok Bot. Tomblok Bot Hanya Melayani Tanya Jawab Seputar Stunting. Berikut Adalah List Pertanyaan Di Tomblok Bot :"
    "\n\n1. Seperti apa anjuran nutrisi anak di atas 2 tahun supaya tidak stunting dan tidak anemia defisiensi besi? Klik /one"
    "\n\n2. Bagaimana menilai pertumbuhan dan perkembangan bayi prematur? Klik /two"
    "\n\n3. Pemberian besi pada anak-anak dan remaja sebaiknya bagaimana? Klik /three"
    "\n\n4. Bagaimana pemberian zat besi pada bayi di bawah 12 bulan? Klik /four"
    "\n\n5. Aturan MPASI sangat keliru misalnya banyak karbo, gorengan, terlalu banyak sufor, namun berat badan naik bagus dan kurva pertumbuhan baik, apakah ini berbahaya?"
    "\n\n6. Bayi menyusui 30-40 menit, bagaimana tips supaya bayi kenyang 10-15 menit? Klik /six"
    "\n\n7. Apakah vitamin/ suplemen / minyak ikan dapat mencegah stunting? Klik /seven"
    "\n\n8. Berat badan dan tinggi badan yang “kecil”, bagaimana membedakan stunting atau genetik (keturunan karena ayah ibu juga kecil)? Klik /eight"
    "\n\n9. Adakah cara cepat/ tips mencegah stunting? Klik /nine"
    "\n\n10. Perlukah menambah sufor saat MPASI jika kenaikan berat badan melambat? Klik /ten")

# Answer One
@bot.message_handler(commands=["one"])
def send_help_message(msg):
    bot.reply_to(msg, "Nutrisi untuk anak di atas 2 tahun mengikuti aturan “my plate” terdiri dari ¼ sayuran, ¼ buah, ¼ karbohidrat (grain) dan ¼ protein. Pilih protein hewani dan berbagai jenis sayuran berwarna-warni.")
    bot.reply_to(msg, "Apakah Membantu?"
    "\n/ya /tidak")

# Answer Two
@bot.message_handler(commands=["two"])
def send_help_message(msg):
    bot.reply_to(msg, "Pertumbuhan bayi prematur dipantau menggunakan kurva Fenton sampai usia koreksi 10 minggu, kemudian pindah ke kurva WHO. Sedangkan perkembangan (verbal, motoric halus dan kasar) menggunakan usia koreksi sampai usia 2 tahun, lalu dianggap sama dengan anak lain yang seusianya.")
    bot.reply_to(msg, "Apakah Membantu?"
    "\n/ya /tidak")

# Answer Three
@bot.message_handler(commands=["three"])
def send_help_message(msg):
    bot.reply_to(msg, "Remaja putri (terutama yang sudah haid) dianjurkan mengkonsumsi suplemen besi tiap minggu. Pada anak di atas 1 tahun, dianjurkan pemeriksaan zat besi darah sebelum memutuskan pemberian suplemen zat besi. Pemeriksaan zat besi meliputi darah lengkap, serum besi, TIBC dan ferritin.")
    bot.reply_to(msg, "Apakah Membantu?"
    "\n/ya /tidak")

# Answer Four
@bot.message_handler(commands=["four"])
def send_help_message(msg):
    bot.reply_to(msg, "Pada bayi dengan ASI eksklusif dianjurkan pemberian zat besi usia 4-6 bulan (tanpa pemeriksaan lab terlebih darhulu), untuk bayi prematur diberikan zat besi sejak usia 1 bulan, lalu setelah usia 6 bulan dianjurkan mendapatkan asupan tinggi zat besi dari MPASI (tinggi protein hewani).")
    bot.reply_to(msg, "Apakah Membantu?"
    "\n/ya /tidak")

# Answer Five
@bot.message_handler(commands=["five"])
def send_help_message(msg):
    bot.reply_to(msg, "Kurva berat badan merupakan indikator gizi, namun perlu diingat gizi yang seimbang sangat mendukung perkembangan otak dan mencegah penyakit-penyakit di usia lanjut. Jadi, gizi bukan sekkedar berat badan namun KUALITAS makanan.Misalnya apakah baik jika anak gendut namun kebanyakan karbohidrat? Tentu tidak baik karena hal tersebut meningkatkan risiko diabetes di kemudian hari.Apakah aman jika berat badan cukup namun kurang protein/ kebanyakan susu? Tentu tidak aman karena hal tersebut bisa menyebabkan defisiensi besi, yang berakibat menurunnya daya imunitas dan kecerdasan.")
    bot.reply_to(msg, "Apakah Membantu?"
    "\n/ya /tidak")

# Answer Six
@bot.message_handler(commands=["six"])
def send_help_message(msg):
    bot.reply_to(msg, "Tingkatkan produksi ASI dengan memompa payudara salaam 15-20 menit setelah menyusu, dan berikan ASI perah kepada bayi setelah menyusui.")
    bot.reply_to(msg, "Apakah Membantu?"
    "\n/ya /tidak")

# Answer Seven
@bot.message_handler(commands=["seven"])
def send_help_message(msg):
    bot.reply_to(msg, "Stunting dapat dicegah dengan pemberian nutrisi yang tepat. Nutrisi pembangun tumbuh adalah makronutrien yang terdiri dari Karbohidrat, protein dan lemak. Sedangkan vitamin dan mineral merupakan mikronutrien yang merupakan zat pendukung, bukan pembangun. Vitamin dan mineral terbaik berasal dari makanan, bukan dari apotek. Tidak ada vitamin dan suplemen pencegah stunting.")
    bot.reply_to(msg, "Apakah Membantu?"
    "\n/ya /tidak")

# Answer Eight
@bot.message_handler(commands=["eight"])
def send_help_message(msg):
    bot.reply_to(msg, "Stunting adalah keadaan pendek yang khas disebabkan oleh gangguan nutrisi, infeksi berulang yang tidak tertangani dalam jangka waktu yang lama. Silahkan evaluasi kurva pertumbuhan dari sejak lahir, adalah pertumbuhan janin terhambat? Adakah riwayat infeksi berulang akibat imunisasi tidak lengkap? adakah riwayat gagal tumbuh? Malnutrisi yang tidak teratasi dalam waktu lama sehingga menyebabkan badannya pendek?")
    bot.reply_to(msg, "Apakah Membantu?"
    "\n/ya /tidak")

# Answer Nine
@bot.message_handler(commands=["nine"])
def send_help_message(msg):
    bot.reply_to(msg, "Sayangnya tidak ada cara yang cepat, namun ada cara yang mudah yang harus dilakukan bertahun-tahun. Pencegahan stunting adalah perjalanan yang cukup panjang dari mempersiapkan remaja putri sebelum menempuh kehamilan, perencanaan keluarga dan kehamilan yang matang, menjaga kehamilan yang sehat, nutrisi saat hamil dan menyusui, manajemen laktasi yang baik, manajemen MPASI yang adekuat, mencegah penyakit dengan imunisasi yang LENGKAP dan pemantauan pertumbuhan anak terus-menerus. Jadi tidak ada cara cepat.")
    bot.reply_to(msg, "Apakah Membantu?"
    "\n/ya /tidak")

# Answer Ten
@bot.message_handler(commands=["ten"])
def send_help_message(msg):
    bot.reply_to(msg, "Saat usia 6-12 bulan, ada dua manajemen nutrisi yang harus dievaluasi yaitu:"
    "\nApakah ASI cukup?"
    "\nApakah kuantitas dan kualitas MPASI cukup?"
    "\nPemberian sufor hanya dilakukan jika ASI tidak cukup."
    "\nPemberian ASI pada masa MPASI tetap dominan mencapai 120 ml x Berat badan perharinya.")
    bot.reply_to(msg, "Apakah Membantu?"
    "\n/ya /tidak")


# Finish
@bot.message_handler(commands=["ya"])
def send_help_message(msg):
    bot.reply_to(msg, "Terima Kasih Atas Kunjungannya. Gunakan Tomblok Bot Untuk Mengatasi Masalah Stunting ☺️🙏")
    bot.reply_to(msg, "Dibuat Oleh : Imroatu Solicah")

@bot.message_handler(commands=["tidak"])
def send_help_message(msg):
    bot.reply_to(msg, "Tomblok Bot Mohon Maaf Jika Jawaban Belum Membantu ☺️🙏")
    bot.reply_to(msg, "Dibuat Oleh : Imroatu Solicah")


@bot.message_handler(content_types=["sticker"])
def send_content_message(msg):
    bot.reply_to(msg, "Tomblok Bot Tidak Paham")
    bot.reply_to(msg, "Silahkan Ikuti Rules Tomblok Bot")


bot.polling()
