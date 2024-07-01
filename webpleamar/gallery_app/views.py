from django.shortcuts import render
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.

@login_required
@permission_required('users.can_post_gallery')
def upload_media(request):
    pass