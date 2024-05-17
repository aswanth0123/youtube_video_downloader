# importing all the required modules 
from django.shortcuts import render, redirect 
from pytube import *
from django.contrib import messages
  
# defining function 
def download1(request): 
  
    # checking whether request.method is post or not 
    if request.method == 'POST': 
        
        # getting link from frontend 
        # try:

            link = request.POST['link'] 
            video = YouTube(link) 
            v_type=request.POST['type']
            if v_type=='audio':
                stream = video.streams.get_audio_only()
            elif v_type=='high':
                stream = video.streams.get_highest_resolution()
            else:
                stream = video.streams.get_lowest_resolution()
            
            # op=request.FILES["folder_upload"]
            # print('op:',type(op))

            stream.download() 
            
        # except:
            messages.success(request,'Not a valid link')
        # returning HTML page 
            return render(request, 'index.html') 
        
            
    return render(request, 'index.html')