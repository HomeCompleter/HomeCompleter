# Introduction
HomeCompleter is a chatbot used for advertising and introducing furniture from Ikea. We use HomeCompleter to
support customers in various ways. Here is how to use HomeCompleter for personal purposes:

## Change directory (cd) vào thư mục
-Chuyển sang thư mục chứa project "HomeCompleter" ta nhập lệnh sau vào Terminal: *cd HomeCompleter*
-Nếu dùng Visual Code Studio thì có thể vào File->Open Folder->HomeCompleter

## Create environment
-Tạo môi trường để khởi động app.py: *python -m venv .venv* hoặc *py -m venv .venv*
-Tùy vào cách sử dụng, bước này có thể bỏ qua nêu cần thiết

## Activate environment
-Kích hoạt môi trường ảo:
+Windows: *.\.venv\Scripts\activate*
(Nếu gặp lỗi về "Execution Policies", chạy: Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
sẽ cho phép máy có quyền chạy lệnh)
+Linux: *source ./venv/bin/activate*

## Install modules using the python-pip command:
-Install các thư viện dùng trong project:
*pip install flask*
*pip install numpy*
*pip install torch*
*pip install nltk*
*pip install pandas*
*pip install numpy*
*pip install openai*

## Select file to activate flask
-Chọn file app.py để kích hoạt flask: *$env:FLASK_APP = "app.py"*

## Activate flask
-Khởi động flask: *flask --debug run*
(--debug: Cập nhật lại ứng dụng mỗi khi có thay đổi) 

# File Explained
a) app.py: là ứng dụng web sử dụng Flask để điều khiển các thao tác trên web
b) _finding.py: chứa các function dùng để tra cứu, tìm kiếm các sản phẩm dựa trên yêu cầu của người dùng
c) _getdata.py: xử lý dữ liệu ban đầu thành dữ liệu đơn giản hơn để chatbot truy cập tới
d) chat.py: chức năng trò chuyện với chatbot dưới phần terminal
e) model.py: dùng để xây dựng Neuron cho quá trình Machine Learning, tạo ra các model cho chatbot
f) nltk_utils.py: thao tác xử lý ngôn ngữ tự nhiên được thực hiện ở đây

# Upcoming
-Cập nhật dữ liệu cho chatbot
-Personalize chatbot, thân thiện hơn với người dùng
-Thống kê lại dữ liệu cho mỗi lần khách hàng sử dụng