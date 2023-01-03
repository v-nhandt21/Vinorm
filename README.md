Install the International Components for Unicode
```
brew instalal icu4c
```
Install ViNorm package
```
pip install vinorm_mac
```
Using in python script
```python
from vinorm import TTSnorm
S=TTSnorm("Hàm này được phát triển từ 8/2019. Có phải tháng 12/2020 đã có vaccine phòng ngừa Covid-19 xmz ?")
```
Some option
```python
TTSnorm(text, punc = False, unknown = True, lower = True, rule = False )
```
- **lower**: If true, get normalization with lowercase
- **rule**: If true, just get normalization wit Regex, not using Dictionary Checking (this flag is not used with another flag)
- **punc**: If true, do not replace punctuation with dot and coma
- **unknown**: If true, replace unknown word, discard word undefine and do not contain vowel, do not spell word with vowel

From version 2.0, do not replace unknown words, skip them for espeak handle in phonetization step
- This version does not parse case: "Tổ chức WTO"
WTO do not in dictionary -> unknown -> keep origin, do not spell as in version 1.0, this aim to use with espeak, let espeak handle, but the drawback is the output of espeak for this case is "ve1kɛɜpte1ɔ7", it does not split each syllable.
- For new entity, need to update in the dictionary

For update lastest version access: https://github.com/NoahDrisort/vinorm

For version 1.0: spell words that is unknown by each character, check previous commit

For C++ version: https://github.com/NoahDrisort/vinorm_cpp_version

### Update pypi
```sh
python setup.py sdist bdist_wheel
twine upload dist/*
```
