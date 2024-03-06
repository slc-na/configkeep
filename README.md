# ConfigKeep
**ConfigKeep** merupakan sebuah project yang dibuat untuk membackup config-config yang ada pada network device SLC.

**ConfigKeep** memiliki fitur fitur berikut:
* Autobackup config network device setiap harinya tepat pada pukul `00:00`
* Autodelete backup config network untuk setiap config yang sudah berumur lebih dari 3 bulan (90 hari)

## Getting Started
### Setup
Lakukan setup sesuai step dibawah
* Instalasi Python (version 3.8.x or later)
* Jalankan command berikut pada terminal (pastikan sudah memasukan bin python kedalam PATH)
  ```
  $ pip install netmiko
  $ pip install python-dotenv
  ```
* Masukan credential berupa username dan password pada file `.env`.
  ```.env
  # Contoh
  USERNAME=PB23-1
  PASSWORD=yuri<3
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
|    |--  |-- backup_manager.py
|    |-- data/ # Folder berisi data data network device, contoh isi folder berupa
|    |--  |-- ip_addresses.txt
|    |--  backups/ # Folder berisi backup - backup yang akan dibikin, folder ini akan di-gitignore
```
### Backup Directory Structure
Directory backup akan memiliki struktur seperti berikut
```
project/
|-- backups/
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

