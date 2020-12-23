Install ViNorm package
```
pip install vinorm
```
Using in python script
```python
from vinorm import TTSnorm
S=TTSnorm("Hàm này được phát triển từ 8/2019, trả về định dạng là String đã được chuẩn hóa.")
```

Just get normalization without lowercase
```python
from vinorm import TTSrawUpper
S=TTSrawUpper("Hàm này được phát triển từ 8/2019, trả về định dạng là String đã được chuẩn hóa.")
```

Just get normalization wit Regex, not using Dictionary Checking
```python
from vinorm import TTSrule
S=TTSrule("Hàm này được phát triển từ 8/2019, trả về định dạng là String đã được chuẩn hóa.")
```


From version 2.0, do not replace unknow words, skip them for espeak handle in phonetization step
- This version does not parse case: "Tổ chức WTO"
WTO do not in dictionary -> unknow -> keep origin, do not spell as in version 1.0, this aim to use with espeak, let espeak handle, but the drawback is the output of espeak for this case is "ve1kɛɜpte1ɔ7", it does not split each syllable.
- For new entity, need to update in the dictionary

For update lastest version access: https://github.com/NoahDrisort/vinorm

For version 1.0: spell words that is unknow by each character, check previous commit

For C++ version: https://github.com/NoahDrisort/vinorm_cpp_version
