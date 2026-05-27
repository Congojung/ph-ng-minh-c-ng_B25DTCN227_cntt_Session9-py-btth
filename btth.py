# Dữ liệu thô ban đầu
branch_names = ["Highlands Nhà Thờ", "Highlands Bà Triệu", "Highlands Nguyễn Du", "Highlands Landmark 81", "Highlands Trần Hưng Đạo"]
daily_revenues = [15500000, 28000000, 9200000, 45000000, 11000000]  # VNĐ
target_achieved = [True, True, False, True, False]  # True = Đạt, False = Không đạt

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ DOANH THU HIGHLANDS =====")
    print("1. Hiển thị báo cáo doanh thu tổng hợp")
    print("2. Thống kê chi nhánh Cao nhất / Thấp nhất")
    print("3. Lọc danh sách cơ sở kém (Không đạt chỉ tiêu)")
    print("4. Thoát chương trình")
    print("================================================")

    choice = input("Nhập lựa chọn của bạn (1-4): ")

    # Xử lý ngoại lệ: nếu nhập không phải số từ 1-4
    if not choice.isdigit() or int(choice) not in range(1, 5):
        print("[Lỗi] Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 4!")
        continue

    choice = int(choice)

    if choice == 1:
        # Chức năng 1: Hiển thị báo cáo tổng hợp
        print("\n[BÁO CÁO DOANH THU TỔNG HỢP]")
        print(f"{'Chi nhánh':<25}{'Doanh thu':<15}{'Trạng thái':<12}")
        print("-" * 55)
        for i in range(len(branch_names)):
            status = "Đạt" if target_achieved[i] else "Không Đạt"
            print(f"{branch_names[i]:<25}{daily_revenues[i]:<15,}{status:<12}")
        print("-" * 55)
        print(f"Tổng doanh thu toàn hệ thống: {sum(daily_revenues):,} VNĐ")

    elif choice == 2:
        # Chức năng 2: Thống kê cao nhất / thấp nhất
        max_rev = max(daily_revenues)
        min_rev = min(daily_revenues)
        max_index = daily_revenues.index(max_rev)
        min_index = daily_revenues.index(min_rev)

        print("\n[THỐNG KÊ DOANH THU]")
        print(f"Chi nhánh cao nhất: {branch_names[max_index]} với {max_rev:,} VNĐ")
        print(f"Chi nhánh thấp nhất: {branch_names[min_index]} với {min_rev:,} VNĐ")

    elif choice == 3:
        # Chức năng 3: Lọc cơ sở kém
        failed_branches = []
        for i in range(len(branch_names)):
            if not target_achieved[i]:
                failed_branches.append(branch_names[i])
        print("\n[DANH SÁCH CƠ SỞ KHÔNG ĐẠT CHỈ TIÊU]")
        print(failed_branches)

    elif choice == 4:
        # Chức năng 4: Thoát
        print("\nHệ thống ghi nhận dữ liệu hoàn tất. Tạm biệt!")
        break
