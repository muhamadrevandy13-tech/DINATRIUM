KALKULATOR ANALISIS KIMIA - STARTER PYTHON

Isi:
- app.py: backend Python Flask
- templates/index.html: tampilan kalkulator
- requirements.txt: dependensi

Fitur:
- Regresi linear kuadrat terkecil
- Pearson r, slope, intersep
- Konsentrasi sampel dari respons sampel
- Vx0 belum diimplementasikan karena rumusnya perlu dikonfirmasi dari SOP/Excel laboratorium

Deploy uji coba ke Render:
1. Ekstrak ZIP.
2. Buat repository baru di GitHub dan unggah semua file/folder di dalam ZIP.
3. Buka Render, pilih New > Web Service, lalu hubungkan repository.
4. Language: Python 3
5. Build Command: pip install -r requirements.txt
6. Start Command: gunicorn app:app
7. Pilih instance yang sesuai dan klik deploy.
8. Setelah deploy selesai, buka URL onrender.com yang diberikan Render.
9. Google Sites: Pages > + > Full page embed, lalu masukkan URL aplikasi; atau Insert > Embed > By URL untuk sematan dalam halaman.
10. Publish Google Sites.

Catatan: layanan gratis Render dapat tidur setelah tidak aktif sehingga kunjungan pertama mungkin lambat. Uji dan validasi hasil dengan data acuan sebelum digunakan untuk keputusan pengujian. Periksa kebijakan keamanan data instansi sebelum memakai hosting eksternal.
