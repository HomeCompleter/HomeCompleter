# HomeCompleter
A chatbot for advertising and introducing furniture from Ikea

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

## Select file to activate flask

-Chọn file app.py để kích hoạt flask: *$env:FLASK_APP = "app.py"*

## Activate flask

-Khởi động flask: *flask --debug run*
(--debug: Cập nhật lại ứng dụng mỗi khi có thay đổi) 
