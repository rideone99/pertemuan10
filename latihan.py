a = {'ari': '081267888','dina':'087677776'}
print('a = {ari: 081267888, dina:087677776}\n')


print('tampilkan kontak ari :', a['ari'])
a['riko']='087654544'
print('tambahkan kontak riko',a)
a['dina']='088999776'
print('mengganti kontak dina',a)
print('menampilkan semua nama: ')
print(a.keys())
print('menampilakan semua nomor: ')
print(a.values())
print('menampilkan semua nama dan nomor:')
print(a)
del a['dina']
print('menghapus kontak dina',a)