def determine_bonus_rate(job_level):
  # Determine the bonus rate based on the job level
  if job_level >= 10:
      return 0.25
  elif 5 <= job_level <= 9:
      return 0.20
  else:
      return 0.10

def calculate_bonus(last_name, salary, job_level):
  # Get the bonus rate based on the job level
  bonus_rate = determine_bonus_rate(job_level)

  # Calculate the bonus
  bonus_amount = salary * bonus_rate

  # Display the results
  print(f"Employee Last Name: {last_name}")
  print(f"Bonus Amount: ${bonus_amount:.2f}")

# Example usage
last_name = input("Enter the employee's last name: ")
salary = float(input("Enter the employee's salary: "))
job_level = int(input("Enter the employee's job level: "))
calculate_bonus(last_name, salary, job_level)