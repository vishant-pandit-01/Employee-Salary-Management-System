class Management:
    def salary(self):
        Name = input("Enter your name: ")
        Phone=int(input("enter you phone:"))
        Total_salary = float(input("Enter your monthly salary: "))
        Total_days = 30
        Leave_days = int(input("Enter number of leave days: "))

        Attendance = Total_days - Leave_days
        Per_day_salary = Total_salary / Total_days
        Deduction = Per_day_salary * Leave_days
        Receive_salary = Total_salary - Deduction

        print("\n----- Salary Details -----")
        print("Name:", Name)
        print("phone:", Phone)
        print("Monthly salary:",Total_salary)
        print("Total Attendance:", Attendance)
        print("Leave Deduction:", Deduction)
        print("Received Salary:", Receive_salary)
                
        with open("salary_data.txt", "a") as file:

            file.write("\n----- Salary Record -----\n")
            file.write(f"Name: {Name}\n")
            file.write(f"phone: {Phone}\n")
            file.write(f"monthly salary: {Total_salary}\n")
            file.write(f"Total Attendance: {Attendance}\n")
            file.write(f"Leave Deduction: {Deduction}\n")
            file.write(f"Received Salary: {Receive_salary}\n")

            print("\nData saved successfully in salary_data")


x2 = Management()
x2.salary()
