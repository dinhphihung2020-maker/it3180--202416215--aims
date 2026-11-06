Câu 1. Vì sao release/* không merge vào master? So sánh với GitFlow.
Trả lời:

Trong quy trình của Lab 04, nhánh release/* được sử dụng để lưu giữ phiên bản phát hành ổn định. Sau khi phát hành v1.0.0, nhánh release/lab04 được giữ nguyên để phục vụ bảo trì và kiểm tra phiên bản đó.

Trong khi đó, master tiếp tục phát triển các tính năng mới. Vì vậy, không merge toàn bộ release/lab04 trở lại master để tránh đưa những thay đổi của phiên bản cũ vào dòng phát triển mới một cách không cần thiết.

So với GitFlow:
- GitFlow thường merge nhánh release vào cả master và develop sau khi hoàn tất phát hành.
- Quy trình trong Lab 04 giữ nhánh release làm baseline ổn định, còn master tiếp tục phát triển độc lập. Khi cần sửa lỗi ở nhiều phiên bản, có thể sử dụng cherry-pick để đưa thay đổi phù hợp sang từng nhánh.
Câu 2. Vì sao lên phiên bản 1.0.0 mà không phải 0.4.0?
Trả lời:

Theo Semantic Versioning (SemVer), phiên bản có định dạng:

MAJOR.MINOR.PATCH

Các phiên bản 0.x.x thường được sử dụng trong giai đoạn phát triển ban đầu, khi phần mềm chưa cam kết tính ổn định của giao diện và chức năng.

Việc phát hành 1.0.0 thể hiện phần mềm đã đạt một cột mốc ổn định, có các chức năng cơ bản hoàn chỉnh và sẵn sàng được sử dụng như một phiên bản chính thức.

Do đó, sau Lab 01–03 (0.1.0, 0.2.0, 0.3.0), dự án chọn 1.0.0 thay vì 0.4.0 để đánh dấu cột mốc phát hành ổn định đầu tiên.