# ConfigKeep
**ConfigKeep** merupakan sebuah project yang dibuat untuk membackup config-config yang ada pada network device SLC.

**ConfigKeep** memiliki fitur fitur berikut:
* Autobackup config network device
* Autodelete backup config network untuk setiap config yang sudah berumur lebih dari 3 bulan (90 hari)

ConfigKeep akan dijalankan harian menggunakan crontab

## Getting Started
### Setup
Lakukan setup sesuai step dibawah
* Instalasi Python (version 3.8.x or later)
* Instalasi Rust (version 1.63.0 or later)
* Jalankan command berikut pada terminal (pastikan sudah memasukan bin python kedalam PATH)
  ```
  $ pip install -r requirements.txt
  ```
* Masukan credential berupa username dan password pada file `.env`.
  ```.env
  # Contoh
  # Username active directory untuk login ke network device
  USERNAME=PB23-1
  # Password active directory untuk login ke network device
  PASSWORD=yuri<3
  # Username yang dipakai untuk login ke beberapa network device
  NETWORK_DEVICE_USERNAME=admin
  # Password yang dipakai untuk login ke beberapa network device dan password untuk enable device cisco
  NETWORK_DEVICE_PASSWORD=!yuri!
  ```

## Coding Convention
### Project Structure
```text
project/
|-- src/
|    |-- main.py
|    |-- models/ # Folder berisi model, contoh isi folder berupa
|    |--  |-- __init__.py
|    |--  |-- network_device.py
|    |-- utils/ # Folder berisi helper function dan constants, contoh isi folder berupa
|    |--  |-- __init__.py
|    |--  |-- time.py
|    |-- backup_service/ # Folder berisi hal-hal yang berkaitan dengan sistem backup, contoh isi folder berupa
|    |--  |-- __init__.py
|    |--  |-- backup_service.py
|    |--  |-- remove_config.py
|    |-- data/ # Folder berisi data data network device, contoh isi folder berupa
|    |--  |-- ip_addresses.txt
```
### Backup Directory Structure
Directory backup akan memiliki struktur seperti berikut
```
project/
|-- backups/ # folder berisi backup, folder akan di gitignore
|--    |-- [year]/
|--    |--  |-- [year]-[month]/
|--    |--  |--  |-- [year]-[month]-[date]/
|--    |--  |--  |--  |-- .log
|--    |--  |--  |--  |-- networkdevice1.config
```
Contoh directory backup:
```
project/
|-- backups/
|--    |-- 2024/
|--    |--  |-- 2024-08/
|--    |--  |--  |-- 2024-08-02/
|--    |--  |--  |--  |-- .log
|--    |--  |--  |--  |-- networkdevice1.config
```

