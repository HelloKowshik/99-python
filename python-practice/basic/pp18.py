d = {"name": "M", "salary": 18000}
# temp = d.pop("age")
# print(temp)

company_dict = {
    "Manager":
    [
        {
            "Name":"Hasan",
             "Languages Used":[
                 'C',
                 'C++',
                 'Rust'
             ]
        },
        {
            
            "Name":"Monaz",
             "Languages Used":[
                 'Python',
                 'Go',
                 'Haskel'
             ]
        }
    ]
}
print(company_dict['Manager'][1]['Languages Used'][1])
