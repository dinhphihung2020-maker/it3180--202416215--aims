# Thảo luận Lab05

### Câu 1. Ưu, nhược điểm của upstream first so với release first?

Upstream first là phương pháp sửa lỗi trên nhánh phát triển chính trước, sau đó sử dụng cherry-pick để đưa bản sửa sang các nhánh release cần thiết.

Release first là phương pháp sửa lỗi trực tiếp trên nhánh release đang bị ảnh hưởng trước, sau đó cherry-pick bản sửa về master và các nhánh release khác.

- **Upstream first:** Ưu điểm là nhánh phát triển chính luôn được cập nhật bản sửa lỗi trước, phù hợp với các sản phẩm lớn phát triển theo sprint. Nhược điểm là việc áp dụng bản sửa vào các phiên bản cũ có thể gặp khó khăn do sự khác biệt giữa các phiên bản.
- **Release first:** Ưu điểm là ưu tiên khắc phục lỗi trên phiên bản đã phát hành mà người dùng đang sử dụng. Nhược điểm là cần quản lý nhiều commit cherry-pick và kiểm tra việc lan truyền bản sửa sang các nhánh khác.

Kết luận: Lựa chọn phương pháp phụ thuộc vào chiến lược phát triển và bảo trì phần mềm. Release first phù hợp khi cần ưu tiên sửa lỗi trên phiên bản đã phát hành, còn upstream first phù hợp khi ưu tiên nhánh phát triển chính.

### Câu 2. Nếu quên lan truyền bản sửa sang release/lab05, lệnh nào ở Phần F sẽ phát hiện?

Sử dụng lệnh:

```bash
git log --all --oneline --grep="cherry picked from commit <FIX_SHA>"
```

Lệnh này tìm các commit có thông tin truy vết đến commit sửa lỗi gốc.

Nếu lan truyền đầy đủ, kết quả phải có hai commit cherry-pick: một trên master và một trên release/lab05. Nếu chỉ có một commit, có khả năng bản sửa chưa được lan truyền đầy đủ.

Trong bài thực hành, lệnh trả về hai commit `a7760f4` và `f237cc6`, chứng minh hotfix đã được cherry-pick sang cả hai nhánh.