import re

def hex_to_rgb(hex_code):
    """将十六进制颜色代码转换为 RGB 值"""
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

def print_colored_wall_e(hex_code):
    """根据用户输入的十六进制颜色代码打印二进制 Wall-E 图案"""
    # 验证十六进制代码格式
    if not re.match(r'^#?[0-9A-Fa-f]{6}$', hex_code):
        print("请输入有效的 RGB 十六进制代码，例如 #FF5733 或 FF5733")
        return

    # 转换为 RGB 值
    rgb = hex_to_rgb(hex_code)
    r, g, b = rgb

    # ANSI 转义序列设置颜色
    color_code = f"\033[38;2;{r};{g};{b}m"

    # 二进制 Wall-E 图案
    wall_e_binary = [
        "               __                          ",
        "               _q0M000N&pp_                    ",
        "            _gN00M00N0M0000Q\\                  ",
        "           a000M000M00M000M0&Wc                ",
        "          p#NMM0N000M00000M000#Qp              ",
        "         jN00M000000000M00M0#MM0Mg             ",
        "        ]000000MMM00M0M0NK0MM0MNM0&            ",
        "        0N00MNRE\"#S$       ~F@MMM00           ",
        "       ]#00b7~&                D000#          ",
        "       j00M/~ &          -      Q0##          ",
        "       Q0MF                     (00#          ",
        "       0N0O\\  \\                  NN0          ",
        "       0N#9\\_p__                `0MM          ",
        "       0#8 &M@7^T: ,    -+^+     T00          ",
        "       0M_pggQg,__     _jj,,,.    00          ",
        "       #l0ZT`_$pT7M0NN#05Q_ `~~#q &#          ",
        "        #&m0*14@HtWM$M- NKX 6  4Mq_T          ",
        "      pR5X 4    ^%B& Mm        ]  &           ",
        "      Md J  ^    a0\"  &        f    #         ",
        "      IQ  Ma____p#M    &_____,/     ~         ",
        "      :E     ``  ^*6 *q   `                   ",
        "      4K^  \\     !                r           ",
        "       *   -                                  ",
        "        !          ,                          ",
        "        `       _m&xan0:,                     ",
        "           \\    O&f                            ",
        "           m^     :\\r                          ",
        "            %                                  ",
        "            MMp                                ",
        "            ~\\\"0&f#  ,                         ",
        "            \\) ^O42E^'                         ",
        "        _      \\                               ",
        "     ,g#        -                gg_          ",
        " _pgB0NMg                       j0B0NNg_      "
    ]

    # 打印图案
    print(color_code)  # 设置颜色
    for line in wall_e_binary:
        print(line)  # 打印每一行
    print("\033[0m")  # 重置颜色

if __name__ == "__main__":
    # 用户输入十六进制颜色代码
    hex_code = input("请输入 RGB 的十六进制代码（例如 #FF5733 或 FF5733）：")
    print_colored_wall_e(hex_code)
