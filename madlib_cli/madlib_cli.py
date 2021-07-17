import re

def greeting ():
    print ('''
Welcome ...
Put words as called for in the spaces and create a story by  create a story like Mad Libs it'sfun.
What you've created may end up being fantastic, screamingly funny, shocking, silly, crazy or just
plain dumb.
It all depends upon the words you've chosen and how they "fit" into the Madlibs story! 
    ''')

def read_template (file_path):
    with open(file_path) as f:
        data_as_string = f.read()
        return data_as_string

def parse(data_as_string):
        list_data_to_change = re.findall(r"\{(.*?)\}",data_as_string)
        return list_data_to_change

def generate_template_for_update(temp, list_data_to_change):
    for i in range(len(list_data_to_change)):
        temp = temp.replace('{'+list_data_to_change[i]+'}','{}')
    return temp   
    

def generate_list_items (list_data_to_change):
    user_list = []
    for i in range(len(list_data_to_change)):
        item =input(f' > Enter a {list_data_to_change[i]}: ')
        user_list.append(item)
    return user_list

def merge (list_new_iteam, tamplate_updated):
    new_file_path_test = "new_file_test.txt"
    with open(new_file_path_test, 'w+') as f:
#         template = '''I the {} and {} {} have {}
# {}'s {} sister and plan to steal her {}
# {}!'''
        # data_updated = template.format(list_new_iteam[0],list_new_iteam[1],list_new_iteam[2],list_new_iteam[3],list_new_iteam[4],list_new_iteam[5],list_new_iteam[6],list_new_iteam[7])
        data_updated = tamplate_updated.format(*list_new_iteam)
        f.write(data_updated)
        return data_updated

if __name__ == "__main__":
    greeting ()
    file_path = 'assets/file.txt'
    data_as_string = read_template(file_path)
    list_data_to_change = parse(data_as_string)
    tamplate_updated = generate_template_for_update(data_as_string, list_data_to_change)
    list_new_iteam = generate_list_items(list_data_to_change)
    data_updated = merge(list_new_iteam, tamplate_updated)
    print(data_updated)
