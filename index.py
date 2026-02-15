class Management:
    def salary(self):
        name = input("Enter your name: ")
        phone=int(input("enter you phone:"))
        total_salary = float(input("Enter your monthly salary: "))
        total_days = 30
        leave_days = int(input("Enter number of leave days: "))

        attendance = total_days - leave_days
        per_day_salary = total_salary / total_days
        deduction = per_day_salary * leave_days
        receive_salary = total_salary - deduction

        print("\n----- Salary Details -----")
        print("Name:", name)
        print("phone:", phone)
        print("Monthly salary:",total_salary)
        print("Total Attendance:", attendance)
        print("Leave Deduction:", deduction)
        print("Received Salary:", receive_salary)

        with open("salary_data.txt", "a") as file:

            file.write("\n----- Salary Record -----\n")
            file.write(f"Name: {name}\n")
            file.write(f"phone: {phone}\n")
            file.write(f"monthly salary: {total_salary}\n")
            file.write(f"Total Attendance: {attendance}\n")
            file.write(f"Leave Deduction: {deduction}\n")
            file.write(f"Received Salary: {receive_salary}\n")

            print("\nData saved successfully in salary_data")


x2 = Management()
x2.salary()