from gradio_client import Client
from github import Github
import os
import time
auth_token = "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"
g = Github(auth_token)

def uploadImage(path):
    basename = os.path.basename(path)
    with open(path, 'rb') as file:
        file_content = file.read()

    repo = g.get_repo("ihy9u0oojlknm/publicnein")
    repo.create_file(basename, "", file_content, branch="main")




linkToFileToBeModified =   "https://raw.githubusercontent.com/ihy9u0oojlknm/publicnein/main/rimage_223.png"


for i in range(224, 260):
    print(i)

    client = Client("https://saarhgkjdbjkxs-sdxl-turbo-img2img-cpu.hf.space/--replicas/5524t/")
    
    result = client.predict(
                    linkToFileToBeModified,	# filepath  in 'Raw Image.' Image component
                    "centered portrait",	# str  in 'Prompt Input Text. 77 Token (Keyword or Symbol) Maximum' Textbox component
                    5,	# float (numeric value between 1 and 5) in 'Number of Iterations' Slider component
                    987654,	# float (numeric value between 0 and 987654321987654321) in 'Seed' Slider component
                    1,	# float (numeric value between 0.1 and 1) in 'Strength' Slider component 
                                                            api_name="/predict"
    )
    


    current_file_name = result
    new_file_name = 'C:\\Users\\arcad\\Pictures\\incremtal_video_genration\\simage_' + str(i) + '.png'
    os.rename(current_file_name, new_file_name)
    uploadImage(new_file_name)
    linkToFileToBeModified = "https://raw.githubusercontent.com/ihy9u0oojlknm/publicnein/main/" + os.path.basename(new_file_name)
    
    time.sleep(5)
    print("finished\n")

