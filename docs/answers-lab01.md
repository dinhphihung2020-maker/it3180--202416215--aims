# Lab 01 – Discussion Answers

## 1. Vì sao dùng `git mv` thay vì di chuyển file bằng thao tác thông thường?

`git mv` giúp thực hiện việc di chuyển hoặc đổi tên file và cập nhật trạng thái tương ứng trong Git. Nhờ đó, thao tác được thể hiện rõ ràng trong quá trình làm việc.

Tuy nhiên, Git thực chất vẫn nhận diện việc đổi tên file dựa trên sự tương đồng nội dung giữa file trước và sau khi di chuyển, chứ không lưu một thao tác rename riêng biệt. Vì vậy, nếu di chuyển file bằng File Explorer rồi dùng `git add` và `git rm`, Git vẫn có thể nhận diện đó là một file được đổi tên.

Trong bài thực hành này, sử dụng `git mv` giúp thao tác rõ ràng, thuận tiện và dễ kiểm tra lịch sử bằng `git log --follow`.

## 2. `release/lab01` có phải là baseline không? Vì sao?

Có. `release/lab01` đóng vai trò là baseline của Lab 01 vì nó lưu lại một trạng thái mã nguồn cụ thể đã hoàn thành và được xác định bằng commit.

Baseline giúp xác định chính xác phiên bản được dùng để nộp bài, kiểm tra và đối chiếu về sau. Khi tiếp tục phát triển các Lab tiếp theo trên `master`, trạng thái của `release/lab01` vẫn được giữ nguyên, không bị ảnh hưởng bởi những thay đổi mới.

Trong bài thực hành, em đã kiểm tra bằng lệnh `git rev-parse master release/lab01` và nhận được hai mã commit giống nhau, chứng minh hai nhánh có cùng trạng thái tại thời điểm tạo release.

## 3. Vì sao không commit trực tiếp lên `master` dù chỉ làm việc một mình?

Không commit trực tiếp lên `master` giúp duy trì quy trình phát triển có kiểm soát, kể cả khi chỉ có một người thực hiện dự án.

Việc tạo nhánh riêng cho từng mục đích giúp tách biệt các thay đổi, dễ theo dõi lịch sử và hạn chế ảnh hưởng đến phiên bản ổn định. Pull Request tạo cơ hội kiểm tra lại mã nguồn, nội dung thay đổi và kết quả kiểm thử trước khi tích hợp vào `master`.

Ngoài ra, cách làm này hình thành thói quen làm việc theo quy trình nhóm, giúp dự án dễ mở rộng và cộng tác hơn trong tương lai.