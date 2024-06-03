
def add_lines(self):
    # 在页面上添加多条水平横线
    line_height = 10  # 每条线之间的高度
    y_start = 20  # 第一条线的起始高度
    page_height = 297  # A4页面高度
    margin = 10  # 左右边距

    num_lines = (page_height - y_start) // line_height

    for i in range(int(num_lines)):
        y_position = y_start + i * line_height
        self.line(margin, y_position, 210 - margin, y_position)