def load_dictionary(file_path):
    name_to_id={}
    id_to_name={}
    with open(file_path,"r",encoding="utf-8") as file:
        for line in file:
            line=line.strip()
            parts=line.split("\t")
            if(len(parts)!=2):continue
            name=parts[0]
            id=int(parts[1])
            name_to_id[name]=id
            id_to_name[id]=name

    return name_to_id,id_to_name

entity_to_id,id_to_entity=load_dictionary("entity2id.txt")
print("正向字典测试")
print(entity_to_id)

print("反向字典测试")
print(id_to_entity)


        
