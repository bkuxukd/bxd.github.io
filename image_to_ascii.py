from PIL import Image

# 定义字符集，从暗到亮
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    """调整图片大小"""
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.55)  # 0.55 用于调整字符的宽高比
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    """将图片转换为灰度图"""
    return image.convert("L")

def map_pixels_to_ascii(image):
    """将像素映射到ASCII字符"""
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return ascii_str

def convert_image_to_ascii(image_path, new_width=100):
    """将图片转换为ASCII字符画"""
    try:
        # 打开图片
        image = Image.open(image_path)
    except Exception as e:
        return f"无法打开图片: {str(e)}"

    # 转换图片
    image = resize_image(image, new_width)
    image = grayscale_image(image)
    ascii_str = map_pixels_to_ascii(image)

    # 格式化输出
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join([ascii_str[index: index + new_width] 
                          for index in range(0, ascii_str_len, new_width)])
    
    return ascii_img

def main():
    image_path = input("请输入图片路径: ")
    width = int(input("请输入输出宽度 (默认100): ") or 100)
    
    ascii_art = convert_image_to_ascii(image_path, width)
    print("\n字符画结果:\n")
    print(ascii_art)

if __name__ == "__main__":
    main()
