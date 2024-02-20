# API Project

This project is a collection of Python scripts that use a REST API to gather data from an employee TODO list and export it in different formats.

## Requirements

•  Python 3.4 or higher

•  urllib or requests module


## Usage

To use this project, you need to clone this repository and run the scripts with a valid employee ID as a parameter. For example:

```bash
git clone https://github.com/alx-system_engineering-devops/0x15-api.git
cd 0x15-api
python3 0-gather_data_from_an_API.py 2

The scripts will display or save the employee TODO list progress in the following formats:

•  0-gather_data_from_an_API.py: Displays the employee name and the number and title of completed tasks on the standard output.

•  1-export_to_CSV.py: Saves the employee tasks in a CSV file named USER_ID.csv, where USER_ID is the employee ID.

•  2-export_to_JSON.py: Saves the employee tasks in a JSON file named USER_ID.json, where USER_ID is the employee ID.

•  3-dictionary_of_list_of_dictionaries.py: Saves all the tasks from all employees in a JSON file named todo_all_employees.json.

Example
Here is an example of the output of the 0-gather_data_from_an_API.py script with the employee ID 2:

Employee Ervin Howell is done with tasks(8/20):
distinctio vitae autem nihil ut molestias quo
voluptas quo tenetur perspiciatis explicabo natus
aliquam aut quasi
veritatis pariatur delectus
nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
repellendus veritatis molestias dicta incidunt
excepturi deleniti adipisci voluptatem et neque optio illum ad
totam atque quo nesciunt
