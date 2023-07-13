# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import MemeImage
from .forms import MemeForm
from django.contrib import messages
from .methods import generate_meme
from io import BytesIO

def meme_generator(request):
    form = MemeForm()
    if request.method == 'POST':
        form = MemeForm(request.POST, request.FILES)
        if form.is_valid():
            meme_image = form.save()
            return redirect('meme_download', meme_id=meme_image.id)
    
    context = {'form': form}
    return render(request, 'generator/meme_generator.html', context)

def meme_library(request):
    """
        View All Images
    """
    meme_images = MemeImage.objects.all()
    meme_images_count = len(meme_images)
    context = {'meme_images': meme_images, 'count':meme_images_count}
    return render(request, 'generator/meme_library.html', context)

def meme_download(request, meme_id):
    """
        Download meme
    """
    meme_image = get_object_or_404(MemeImage, id=meme_id)
    if request.method == 'POST':
        image_path = meme_image.image
        captions = [request.POST['caption1'], request.POST['caption2'],request.POST['caption3']]
        caption_colors = [request.POST['caption1_color'], request.POST['caption2_color'], 
                          request.POST['caption3_color']]
        caption_positions = [request.POST['caption1_position'], request.POST['caption2_position'], 
                             request.POST['caption3_position']]
        caption_bgcolors = [request.POST['caption1_bgcolor'], request.POST['caption2_bgcolor'], 
                            request.POST['caption3_bgcolor']]

        # Generate the meme image using the generate_meme function
        meme_image = generate_meme(image_path, captions, caption_colors, 
                    caption_positions, caption_bgcolors)

        # Save the meme image to a buffer
        buffered = BytesIO()
        meme_image.save(buffered, format='PNG')
        buffered.seek(0)

        # Create a response object with the image data
        response = HttpResponse(content_type='image/png')
        response['Content-Disposition'] = 'attachment; filename="meme.png"'
        response.write(buffered.getvalue())

        return response

def meme_generate(request):
    """
        meme update page.
    """
    meme_id = request.GET.get('default',None)
    try:
        meme_image = get_object_or_404(MemeImage, id=meme_id)
    except:
        meme_image = None

    context = {'meme_image': meme_image, 'meme_objs': MemeImage.objects.all()}
    return render(request, 'generator/meme_generator.html',context)

def meme_upload(request):
    """
        Upload Image
    """
    form = MemeForm()
    if request.method == 'POST':
        form = MemeForm(request.POST, request.FILES)
        if form.is_valid():
            meme_image = form.save()
            messages.success(request, f'Images with name {meme_image.name} \
                has sucessfully upload.')
            return redirect('meme_library')
        else:
            messages.error(request, f'Error: {form.errors}')
    context = {'form': form}
    return render(request, 'generator/meme_upload.html', context)

def meme_update(request, meme_id):
    """
        update image
    """
    meme_obj = get_object_or_404(MemeImage, id=meme_id)
    form = MemeForm(instance=meme_obj)
    if request.method == 'POST':
        form = MemeForm(request.POST, request.FILES, instance=meme_obj)
        if form.is_valid():
            meme_image = form.save()
            messages.success(request,f'meme with the name {meme_image.name}\
                 has update sucessfully.')
            return redirect('meme_library')
    
    context = {'form': form}
    return render(request, 'generator/meme_update.html', context)

def meme_delete(request, meme_id):
    """
        Delete Image
    """
    meme_obj = get_object_or_404(MemeImage, id=meme_id)
    if meme_obj:
        meme_obj.delete()
        messages.success(request, f'meme with the name {meme_obj.name} has Deleted sucessfully.')
        return redirect('meme_library')
    else:
        messages.error(request, f'Unable to delete meme images.')
        return redirect('meme_library')


# this is to view the meme
# def meme_view(request, meme_id):
#     meme_image = get_object_or_404(MemeImage, id=meme_id)
#     if request.method == 'POST':
#         image_path = meme_image.image
#         captions = [request.POST['caption1'], request.POST['caption2'], request.POST['caption3']]
#         caption_colors = [request.POST['caption1_color'], request.POST['caption2_color'], request.POST['caption3_color']]
#         caption_positions = [request.POST['caption1_position'], request.POST['caption2_position'], request.POST['caption3_position']]

#         # Generate the meme image using the generate_meme function
#         meme_image = generate_meme(image_path, captions, caption_colors, caption_positions)

#        # Convert PIL image to base64-encoded string
#         buffered = BytesIO()
#         format = meme_image.format if meme_image.format else 'PNG'
#         meme_image.save(buffered, format=format)
#         meme_image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
#         # Pass the meme image as base64 string to the template for display
#         context = {'meme_image_base64': meme_image_base64}

#         # Pass the meme image to the template for display
#         return render(request, 'generator/meme.html', context)


