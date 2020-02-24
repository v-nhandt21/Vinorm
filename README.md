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