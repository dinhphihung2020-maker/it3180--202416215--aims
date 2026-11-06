CÂU HỎI THẢO LUẬN – LAB 03

Câu 1. Merge base là gì?

Merge base là commit tổ tiên chung gần nhất của hai nhánh Git đang được hợp nhất.

Git sử dụng merge base để xác định những thay đổi được thực hiện trên mỗi nhánh kể từ commit chung đó, từ đó kết hợp các thay đổi khi thực hiện thao tác merge.

Ví dụ: Hai nhánh master và feature được tạo từ cùng một commit A. Sau đó, mỗi nhánh có những commit riêng. Nếu A là tổ tiên chung gần nhất thì A chính là merge base của hai nhánh.

Câu 2. Vì sao các nhánh master/release/* nên sử dụng revert?

Các nhánh master và release/* thường chứa lịch sử phát triển ổn định và được chia sẻ với nhiều người. Vì vậy, việc thay đổi lịch sử của những nhánh này có thể gây ảnh hưởng đến các thành viên khác.

git reset: Di chuyển con trỏ nhánh về một commit trước đó, có thể làm thay đổi lịch sử commit.

git revert: Tạo một commit mới để đảo ngược thay đổi của commit trước đó mà không xóa commit cũ khỏi lịch sử.

Do đó, nên sử dụng git revert trên các nhánh master và release/* để giữ nguyên lịch sử phát triển, đảm bảo tính minh bạch và tránh gây xung đột cho những người đang làm việc chung trên repository.

Kết luận

Qua bài thực hành, em đã hiểu cách sử dụng merge base, phân biệt git reset và git revert, đồng thời biết cách lựa chọn phương pháp phù hợp khi xử lý các thay đổi trên nhánh cá nhân và nhánh dùng chung.