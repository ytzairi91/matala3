
import json

def main():
    path= "C:\\Users\\ytzai\\Desktop\\txt.txt"
    text_file=open(path,'r',encoding='utf-8')
    txt= text_file.read()
    meta_data=dict()
    names= dict()
    messagesDic = dict()
    final_dic= dict()
    
    messages = txt.split("\n")[1:]
    id=1 
    
    split_by_gap=txt.split(" ")
    split_by_gap_cn=txt.split(" ")[10:]
    
    meta_data["Chat name"]= split_by_gap_cn[split_by_gap_cn.index("11:39")+3:split_by_gap_cn.index("נוצרה")] 
    meta_data["Creation data"]= split_by_gap[0:2]
    
    path_f_file = "C:\\Users\\ytzai\\Desktop.txt"


    
    for message in messages:
        
        
        messageSplit = message.split(",")
        messagesDic["datetime"] = message[0:message.find("-")]
        messagesDic["id"] = message[len(messagesDic["datetime"])+2:-1].split(":")[0]
        messagesDic["text"] = message[3+len(messagesDic["id"]+  messagesDic["datetime"])
    
                              :]    
        if names.get(messagesDic["id"]) == None:
            names[messagesDic["id"]] = id;
            messagesDic["id"] = id;
            id= id+1
             
            meta_data["Num of participants"]= id-1  
            final_dic["messages"]=dict(messagesDic)
            final_dic["meta data"]=meta_data
            
            file=open(path_f_file,"w",encoding = 'utf-8')
            json.dumps(final_dic,file,ensure_ascii=False , indent=6) 
            file.close()
            file=open(path_f_file,"r",encoding= 'utf-8')
            print(json.load(file))
            file.close()

    


if(__name__ =="__main__" ):
    main()
    
    
  