employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

employee_id = employee["employee_id"]

full_name = employee["full_name"]

employee["status"] = "official"

employee["base_salary"] = 15000000

del employee["department"]

print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)
# Dictionary employee gồm các key: employee_id, full_name, status, và department.
# Dòng employee_id = employee[0] gây lỗi vì dictionary không truy cập dữ liệu bằng vị trí index giống list mà phải truy cập bằng key. Vì vậy, muốn lấy mã nhân viên "NV001" cần dùng key employee_id.
# Dòng full_name = employee["name"] gây lỗi vì trong dictionary không tồn tại key "name". Key đúng để lấy họ tên nhân viên là "full_name".
# Dòng employee["employee_status"] = "official" chưa cập nhật đúng trạng thái vì key "employee_status" không tồn tại trong dictionary. Muốn cập nhật trạng thái nhân viên cần dùng key "status".
# Dòng employee.append("base_salary", 15000000) gây lỗi vì dictionary không có phương thức append(). Phương thức này chỉ dùng cho list. Muốn thêm lương cơ bản cần tạo thêm key "base_salary" và gán giá trị 15000000.
# Dòng del employee["team"] gây lỗi vì dictionary không có key "team". Muốn xóa thông tin phòng ban cần dùng key "department".