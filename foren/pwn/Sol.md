+ Lấy payload từ tcp.stream eq 509
+ Lấy  được địa chỉ ở trong HTTP object list (file ipconfig.me)

![image](https://github.com/KMANVK/imaginary_ctf_2023/assets/94669750/ffd1d8ea-e46d-47b1-93c5-a2c55ff7390c)

+ Dùng nmap tìm port 

+ Thiết lập kết nối với dịch vụ từ xa bằng chức năng connect từ thư viện pwn.
+ Sau đó, nó sẽ gửi 54 tải trọng đầu tiên đến dịch vụ từ xa và nhận phản hồi, đồng thời in dữ liệu nhận được.

+ Tập lệnh nhận được "leak" từ dịch vụ từ xa và tính toán giá trị "offset"
+ Cuối cùng là in flag ra bằng `conn.interactive()` để tương tác với dịch vụ.
