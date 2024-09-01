from flask import Flask,request


app = Flask(__name__)      # this should be same as file name              app.py 



# creating an idea repository , this where idea will be stored
ideas={
    1:{
        "id":1,
        "idea_name":"ondc",
        "idea_description":"this is my first idea",
        "idea_author":"meraj"
        },
        2:{
            "id":2,
            "idea_name":"save soil",
            "idea_description":"details about save soil",
            "idea_author":"meraj2"
            }
}

"""fetching  all the data """

"""ths is same as fetching all data with query param """

# # create an restful endpoint for fetching all the ideas 
# @app.get("/ideaapp/api/v1/ideas")
# def get_all_ideas():
#     # logic to fetch ideas 
#     return ideas

#   1    http://127.0.0.1:8080/ideaapp/api/v1/ideas     type this on postman to fetch data with get    this is called api 

""" posting data """




@app.post("/ideaapp/api/v1/ideas")
def create_idea():
    # logic to create a new idea 

    # first read the request body
    request_body= request.get_json()
    # check if the idea is passed is not already present 
    
    if request_body["id"] and request_body["id"] in ideas:
        return  "idea already exist", 400   # 400 is httpt request code tht is bad request 

    # insert the passed idea in the ideas dict 
    
    ideas[request_body["id"]]= request_body
    #return the response saying idea got saved 
    return "idea created and saved successfully",201

#   2    http://127.0.0.1:8080/ideaapp/api/v1/ideas    type this on post man with post   after typing which u want to post in json format in raw body 







"""fetching data based on id """


@app.get("/ideaapp/api/v1/ideas/<idea_id>")    # ida_id shud be in <>
def get_idea_id(idea_id):
    
    if int(idea_id) in ideas:
        
        return ideas[int(idea_id)],200
    
    else:
        return "not pressent" ,400

      #  3     http://127.0.0.1:8080/ideaapp/api/v1/ideas/1    type this on postman to fetch 




""" fetch data with query parameter"""



@app.get("/ideaapp/api/v1/ideas")
def get_all_ideas():
    idea_author=request.args.get("idea_author")
    
    if idea_author:
        # filtering ideas 
        idea_res={}
        for key,value in ideas.items():
            if value["idea_author"]==idea_author:
                idea_res[key]=value
        return idea_res
    return ideas
    
    
    #   http://127.0.0.1:8080/ideaapp/api/v1/ideas?idea_author=meraj    type this on postman to fetch 




"""updating the idea """

@app.put("/ideaapp/api/v1/ideas/<idea_id>")

def update_idea(idea_id):
    if int(idea_id) in ideas:
        # updating 
        ideas[int(idea_id)]=request.get_json()
        # returning the uodated result 
        return ideas[int(idea_id)]
    return "idea_id is passed is not present "

 #  http://127.0.0.1:8080/ideaapp/api/v1/ideas/2   type this with  key value pairs in   body 
 
 
 
 
 
 
"""delete of idea"""
 
@app.delete("/ideaapp/api/v1/ideas/<idea_id>")

def delete_idea(idea_id):
    if int(idea_id) in ideas:
        ideas.pop(int(idea_id))
        return "idea got successfully deleted "
    return  "idea id passed is not present "
 
    # http://127.0.0.1:8080/ideaapp/api/v1/ideas/4      in idea_id type that id which u want oto delete 
    
    
    
    
# below code is used to run the code in python  file 
if __name__ == "__main__":
    app.run(port=8080)
