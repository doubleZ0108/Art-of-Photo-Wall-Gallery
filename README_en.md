# Art of Photo Wall Gallery

[中文(zh-cn)](https://github.com/doubleZ0108/Art-of-Photo-Wall-Gallery/blob/master/README.md) | [English(en)](https://github.com/doubleZ0108/Art-of-Photo-Wall-Gallery/blob/master/README_en.md)

* [Background Story](#background-story)
* [How to run?](#how-to-run)
* [Project Structure](#project-structure)
* [TODOs](#todos)
* [About the Author](#about-the-author)

------

## Background Story

🎂Wondering how to look back on my 20th with a picture on my 21st birthday

📅At age 20, start using a calendar to keep track of your day

🎁So I thought of putting together a calendar for each week of the year as a souvenir, but I couldn't find the right tool, so I started to give myself this special gift in the early morning of January 08, 2019.

📸The background of the photo wall is a blurry Mosaic of the calendar of the year; In the lower left corner is the Python code that generated this image; The text is handwritten on the photo by Procreate in the hope that it will preserve the unique memories of each stage and that you will begin to record your life in a special way

![birthday-gift](README.assets/birthday-gift.png)

<br/>

## How to run?

1. Install the required dependencies `pip intall -r requirements.txt`

2. Put all raw images in the folder `img/`

3. Run `src/generate.py` script，the argument are as follow：

   - `-s` `--size`：adjust the original image to the same size(400*400 as default)  [🌰 --size 400 300]
   - `-b` `--blur`：gaussian blur level(0~10，6 as default)  [🌰 --blur 4]

   ```bash
   python src/generate.py		# use the default parameter to generate a photo wall gallery
   python src/generate.py -s 300 300	# size of the wall is 300*300
   python src/generate.py -b 10	# the blur level is 10
   python src/generate.py --size 400 300 --blur 4
   ```

4. The result iamge is store in: `img/result/result.png`

   > **[Effect Screenshot]**
   >
   > <img src="README.assets/image-20210110112530881.png" alt="image-20210110112530881" width="75%;" />

<br/>

## Project Structure

- **OS**：macOS Catalina 10.15.7
- **Python env**：Python 3.7.4
- **Dependencies**：numpy, opencv_python, Pillow

```bash
.
├── README.md
├── img			# original image
│   ├── result		# result image
│   │   └── result.png
│   ├── test-0.jpg
│   ├── test-1.jpg
│   ├── ...
├── requirements.txt
└── src
    ├── generate.py	# main function for generate
    └── util.py
```

<br>

## TODOs

- [x] Photo-Wall-Gallery generation
- [x] Photo Wall Blur (Gaussian Blur)
- [ ] It is not recommended that the total number of original photos be prime
- [ ] The problem of distortion caused by different sizes of original photos has not been considered

<br/>

## About the Author

| Name👤       | Zhe ZHANG                                           |
| ----------- | --------------------------------------------------- |
| University🏫 | Tongji Univ.                                        |
| Email✉️      | [dbzdbz@tongji.edu.cn](mailto:dbzdbz@tongji.edu.cn) |
