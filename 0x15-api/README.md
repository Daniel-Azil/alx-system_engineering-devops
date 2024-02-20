# API Project

This project is a collection of Python scripts that use a REST API to gather data from an employee TODO list and export it in different formats.

## Requirements

•  Python 3.4 or higher

•  urllib or requests module


## Usage

To use this project, you need to clone this repository and run the scripts with a valid employee ID as a parameter. For example:

<pre>
git clone https://github.com/alx-system_engineering-devops/0x15-api.git
cd 0x15-api
python3 0-gather_data_from_an_API.py 2
</pre>
The scripts will display or save the employee TODO list progress in the following formats:

•  0-gather_data_from_an_API.py: Displays the employee name and the number and title of completed tasks on the standard output.

    Example:
            sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 2
            Employee Ervin Howell is done with tasks(8/20):
                distinctio vitae autem nihil ut molestias quo
                voluptas quo tenetur perspiciatis explicabo natus
                aliquam aut quasi
                veritatis pariatur delectus
                nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
                repellendus veritatis molestias dicta incidunt
                excepturi deleniti adipisci voluptatem et neque optio illum ad
                totam atque quo nesciunt
            sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 4
            Employee Patricia Lebsack is done with tasks(6/20):
                odit optio omnis qui sunt
                doloremque aut dolores quidem fuga qui nulla
                sint amet quia totam corporis qui exercitationem commodi
                sequi dolorem sed
                eum ipsa maxime ut
                tempore molestias dolores rerum sequi voluptates ipsum consequatur
            sylvain@ubuntu$
            sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 4 | tr " " "S" | tr "\t" "T" 
            EmployeeSPatriciaSLebsackSisSdoneSwithStasks(6/20):
            TSoditSoptioSomnisSquiSsunt
            TSdoloremqueSautSdoloresSquidemSfugaSquiSnulla
            TSsintSametSquiaStotamScorporisSquiSexercitationemScommodi
            TSsequiSdoloremSsed
            TSeumSipsaSmaximeSut
            TStemporeSmolestiasSdoloresSrerumSsequiSvoluptatesSipsumSconsequatur
            sylvain@ubuntu$


•  1-export_to_CSV.py: Saves the employee tasks in a CSV file named USER_ID.csv, where USER_ID is the employee ID.

    Example:
            sylvain@ubuntu$ python3 1-export_to_CSV.py 2
            sylvain@ubuntu$ cat 2.csv
            "2","Antonette","False","suscipit repellat esse quibusdam voluptatem incidunt"
            "2","Antonette","True","distinctio vitae autem nihil ut molestias quo"
            "2","Antonette","False","et itaque necessitatibus maxime molestiae qui quas velit"
            "2","Antonette","False","adipisci non ad dicta qui amet quaerat doloribus ea"
            "2","Antonette","True","voluptas quo tenetur perspiciatis explicabo natus"
            "2","Antonette","True","aliquam aut quasi"
            "2","Antonette","True","veritatis pariatur delectus"
            "2","Antonette","False","nesciunt totam sit blanditiis sit"
            "2","Antonette","False","laborum aut in quam"
            "2","Antonette","True","nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis"
            "2","Antonette","False","repudiandae totam in est sint facere fuga"
            "2","Antonette","False","earum doloribus ea doloremque quis"
            "2","Antonette","False","sint sit aut vero"
            "2","Antonette","False","porro aut necessitatibus eaque distinctio"
            "2","Antonette","True","repellendus veritatis molestias dicta incidunt"
            "2","Antonette","True","excepturi deleniti adipisci voluptatem et neque optio illum ad"
            "2","Antonette","False","sunt cum tempora"
            "2","Antonette","False","totam quia non"
            "2","Antonette","False","doloremque quibusdam asperiores libero corrupti illum qui omnis"
            "2","Antonette","True","totam atque quo nesciunt"
            sylvain@ubuntu$

•  2-export_to_JSON.py: Saves the employee tasks in a JSON file named USER_ID.json, where USER_ID is the employee ID.
Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
File name must be: USER_ID.json

    Example:
            sylvain@ubuntu$ python3 2-export_to_JSON.py 2
            sylvain@ubuntu$ cat 2.json
            {"2": [{"task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": false, "username": "Antonette"}, {"task": "distinctio vitae autem nihil ut molestias quo", "completed": true, "username": "Antonette"}, {"task": "et itaque necessitatibus maxime molestiae qui quas velit", "completed": false, "username": "Antonette"}, {"task": "adipisci non ad dicta qui amet quaerat doloribus ea", "completed": false, "username": "Antonette"}, {"task": "voluptas quo tenetur perspiciatis explicabo natus", "completed": true, "username": "Antonette"}, {"task": "aliquam aut quasi", "completed": true, "username": "Antonette"}, {"task": "veritatis pariatur delectus", "completed": true, "username": "Antonette"}, {"task": "nesciunt totam sit blanditiis sit", "completed": false, "username": "Antonette"}, {"task": "laborum aut in quam", "completed": false, "username": "Antonette"}, {"task": "nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis", "completed": true, "username": "Antonette"}, {"task": "repudiandae totam in est sint facere fuga", "completed": false, "username": "Antonette"}, {"task": "earum doloribus ea doloremque quis", "completed": false, "username": "Antonette"}, {"task": "sint sit aut vero", "completed": false, "username": "Antonette"}, {"task": "porro aut necessitatibus eaque distinctio", "completed": false, "username": "Antonette"}, {"task": "repellendus veritatis molestias dicta incidunt", "completed": true, "username": "Antonette"}, {"task": "excepturi deleniti adipisci voluptatem et neque optio illum ad", "completed": true, "username": "Antonette"}, {"task": "sunt cum tempora", "completed": false, "username": "Antonette"}, {"task": "totam quia non", "completed": false, "username": "Antonette"}, {"task": "doloremque quibusdam asperiores libero corrupti illum qui omnis", "completed": false, "username": "Antonette"}, {"task": "totam atque quo nesciunt", "completed": true, "username": "Antonette"}]}sylvain@ubuntu$

•  3-dictionary_of_list_of_dictionaries.py: Saves all the tasks from all employees in a JSON file named todo_all_employees.json.

Records all tasks from all employees
Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
File name must be: todo_all_employees.json

    Example:
            sylvain@ubuntu$ python3 3-dictionary_of_list_of_dictionaries.py
            sylvain@ubuntu$ cat todo_all_employees.json
            {"1": [{"username": "Bret", "task": "delectus aut autem", "completed": false}, {"username": "Bret", "task": "quis ut nam facilis et officia qui", "completed": false}, {"username": "Bret", "task": "fugiat veniam minus", "completed": false}, {"username": "Bret", "task": "et porro tempora", "completed": true}, {"username": "Bret", "task": "laboriosam mollitia et enim quasi adipisci quia provident illum", "completed": false}, {"username": "Bret", "task": "qui ullam ratione quibusdam voluptatem quia omnis", "completed": false}, {"username": "Bret", "task": "illo expedita consequatur quia in", "completed": false}]}

