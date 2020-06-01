# E-diary hacking scripts.

File `scripts.py` contains several functions which can fix the electronic diary.

Electron diary is a site based on Django, which contains marks of schoolkids.

### How to use

Python3 should be already installed.

1. You need to place the script in the directory of the site file next to the `manage.py` file.
2. You need to run Django shell, [more.](https://stackoverflow.com/questions/44999890/django-nameerror-name-album-not-defined/44999958#44999958)
3. You need to import `scripts.py`.
```python
import scripts
```
4. After these steps, you can work with the electronic diary.

#### Examples

This example shows:
- Find a schoolkid
- Fix all bad schoolkid grades
- Delete all schoolkid chastisements
- Create commendation for the schoolkid

```python
import scripts

schoolkid = scripts.find_schoolkid(schoolkid_name='John Doe')
scripts.fix_marks(schoolkid=schoolkid)
scripts.remove_chastisements(schoolkid=schoolkid)
scripts.create_commendation(schoolkid_name='John Doe', subject_name='Math')
``` 

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
