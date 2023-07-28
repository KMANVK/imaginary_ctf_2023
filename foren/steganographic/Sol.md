+ Tìm kiếm và tải ảnh gốc của chall ở [wiki](https://commons.wikimedia.org/wiki/File:Parco_Parolini_Bassano_del_Grappa_-_Dalla_collezione_ENTER.png)
+ So sánh các giá trị RGB giữa ảnh gốc và ảnh chall
+ Phát hiện :
+ 1.giá trị red chall - giá trị red gốc => ra 1010....(nghi ngờ là binary)
+ 2.giá trị blue chall - giá trị blue gốc => ra 1111...
+ 3.Tương tư như thế thì green trả về 0000...
+ Viết kịch bản để lấy các giá trị của red ra và decode nó.(lưu ý padding == zero vì độ dài ko khớp)


  
