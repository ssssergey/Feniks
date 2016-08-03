from .models import UserProfile
from .forms import UserRegisterForm


def retrieve(request):
    ''' note that this requires an authenticated
    user before we try calling it '''
    try:
        profile = request.user
    except UserProfile.DoesNotExist:
        profile = UserProfile()
        profile.save()
    return profile


def set(request):
    profile = retrieve(request)
    profile_form = UserRegisterForm(request.POST, instance=profile)
    profile_form.save()
