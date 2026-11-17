from pathlib import Path
import re
p=Path("index.html")
s=p.read_text(encoding="utf-8")
old='const PHOTOS={"Горячее":'
new='const PHOTOS={"Супы": {"Борщ (говядина)": "photos/borshch_govyadina.jpg", "Борщ (курица)": "photos/borshch_kurica.jpg", "Борщ (без мяса)": "photos/borshch_bez_myasa.jpg"}, "Горячее":'
if old not in s:
    raise SystemExit("Не найден ожидаемый блок PHOTOS в index.html. Файл не изменён.")
s=s.replace(old,new,1)
p.write_text(s,encoding="utf-8")
print("Готово: фотографии трёх видов борща подключены к карточкам каталога.")
