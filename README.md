# HomeCompleter
A chatbot for advertising and introducing furniture from Ikea.

## Change directory (cd) vào thư mục

-Chuyển sang thư mục "HomeCompleter" ta : *cd HomeCompleter*
-Nếu dùng Visual Code Studio thì có thể vào File->Open Folder->HomeCompleter

## Create environment

-Tạo môi trường để khởi động app.py: *python -m venv .venv* hoặc *py -m venv .venv*

## Activate environment

-Kích hoạt môi trường ảo:
+Windows: *.\.venv\Scripts\activate*
(Nếu gặp lỗi về "Execution Policies", chạy: Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
sẽ cho phép máy có quyền chạy lệnh)
+Linux: *source ./venv/bin/activate*

## Install modules using the python-pip command:
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