from .models import SocialProfile


def social_profile_context_processor(request):
    try:
        linkedin = SocialProfile.objects.get(heading='Linkedin')
        github = SocialProfile.objects.get(heading='Github')
        instagram = SocialProfile.objects.get(heading='Instagram')
        facebook = SocialProfile.objects.get(heading='Facebook')
        twitter = SocialProfile.objects.get(heading='Twitter')
        snapchat = SocialProfile.objects.get(heading='Snapchat')
        leetcode = SocialProfile.objects.get(heading='LeetCode')
        hackerrank = SocialProfile.objects.get(heading='HackerRank')
        return {'linkedin':linkedin, 'github':github, 'instagram':instagram, 'facebook':facebook, 'twitter':twitter, 'snapchat':snapchat, 'leetcode':leetcode, 'hackerrank':hackerrank}
    except:
        return {}

