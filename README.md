# install library rembg, onnxruntime and pillow

```bash
pip install pillow rembg onnxruntime
```
# use the function

```python
profile_sdm_tinggi('input.jpg', 'output.png', 'red', "#4102D3", 0.320, 0.07, 0.4, 0, -3, 1.5)
#profile_sdm_tinggi(1.input.jpg,2.output.png,3.bg_color',4.bar_color,5.eye_position,6.bar_height,7.bar_width,8.offset,9.slope,10.contrast):
```
You can adjust the bar position by changing the number values:
0.320 (eye position), 0.07 (bar height), 0.4 (bar width), 0 (horizontal offset), -3 (bar slope in degrees), and 1.5 (image contrast).
These numeric arguments are optional, use them to match your picture.
Remember to delete the existing input.jpg and replace it with your own image.

## Preview
![woody with mostchreal style](output.png)