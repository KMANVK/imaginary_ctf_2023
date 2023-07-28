+ Lấy payload từ tcp.stream eq 509
  
![image](https://github.com/KMANVK/imaginary_ctf_2023/assets/94669750/698f298b-6b22-4d38-a340-7686dd457e24)

+ Lấy  được địa chỉ ở trong HTTP object list (file ipconfig.me)

![image](https://github.com/KMANVK/imaginary_ctf_2023/assets/94669750/ffd1d8ea-e46d-47b1-93c5-a2c55ff7390c)

+ Dùng nmap tìm port


+ Viết kịch bản cho nó để gửi đến sever :  
1.Thiết lập kết nối với dịch vụ từ xa bằng chức năng connect từ thư viện pwn.
  
2.Sau đó, nó sẽ gửi 54 tải trọng đầu tiên đến dịch vụ từ xa và nhận phản hồi, đồng thời in dữ liệu nhận được.

3.Tập lệnh nhận được "leak" từ dịch vụ từ xa và tính toán giá trị "offset"

4.Cuối cùng là in flag ra bằng `conn.interactive()` để tương tác với dịch vụ.
