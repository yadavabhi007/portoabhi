from .models import SocialProfile


def social_profile_context_processor(request):
    try:
        linkedin = SocialProfile.objects.get(heading='Linkedin')
        github = SocialProfile.objects.get(heading='Github')
        instagram = SocialProfile.objects.get(heading='Instagram')
        facebook = SocialProfile.objects.get(heading='Facebook')
        return {'linkedin':linkedin, 'github':github, 'instagram':instagram, 'facebook':facebook}
    except:
        return {}

