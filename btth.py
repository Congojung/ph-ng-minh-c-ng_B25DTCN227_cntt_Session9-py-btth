branch_names = ["Highlands Nhà Thờ", "Highlands Bà Triệu", "Highlands Nguyễn Du", "Highlands Landmark 81", "Highlands Trần Hưng Đạo"]
daily_revenues = [15500000, 28000000, 9200000, 45000000, 11000000]
target_achieved = [True, True, False, True, False]

while True :
    choice = input('''
        ===== HỆ THỐNG QUẢN LÝ DOANH THU HIGHLANDS =====
        1. Hiển thị báo cáo doanh thu tổng hợp
        2. Thống kê chi nhánh Cao nhất / Thấp nhất
        3. Lọc danh sách cơ sở kém (Không đạt chỉ tiêu)
        4. Thoát chương trình
        ================================================
        Nhập lựa chọn của bạn (1-4): ''')
    
    match choice :
        case '1': 
            print('--- BÁO CÁO DOANH THU TỔNG HỢP ---')
            print(f'{'Tên cơ sở':<30}| {'Doanh thu':<15}| {'Trạng thái':<10}')
            print('-'*60)

            for i, branch in enumerate(branch_names):
                print(f'{branch:<30}| {daily_revenues[i]:<15}| {'Đạt' if target_achieved[i] else 'Không Đạt':<10}')

            print('-'*60)
            print(f'=> TỔNG DOANH THU TOÀN VÙNG: {sum(daily_revenues)} VND')

        case '2': 
            max_revenue = max(daily_revenues)
            min_revenue = min(daily_revenues)

            max_index = daily_revenues.index(max_revenue)
            min_index = daily_revenues.index(min_revenue)

            max_branch = branch_names[max_index]
            min_branch = branch_names[min_index]

            print(f'''
            --- THỐNG KÊ CƠ SỞ NỔI BẬT ---
            - Cơ sở có doanh thu CAO NHẤT: {max_branch} ({max_revenue} VND)
            - Cơ sở có doanh thu THẤP NHẤT: {min_branch} ({min_revenue} VND)''')

        case '3': 
            failed_branches = []
            for i, branch in enumerate(branch_names):
                if(not target_achieved[i]):
                    failed_branches.append(branch)
                    
            print('--- DANH SÁCH CƠ SỞ CẦN HỖ TRỢ TRA CỨU ĐƯỢC ---')
            print(failed_branches)

        case '4': 
            print("Thoát chương trình.")
            break

        case _: 
            print("[Loi] Lua chon khong hop le, vui long nhap lai so tu 1 den 4!")
            continue

