from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin


def update_views(request, object):
    # Initialize context as an empty dictionary
    context = {}

    # Get the HitCount model and retrieve the hit count for the provided object
    hit_count = get_hitcount_model().objects.get_for_object(object)

    # Retrieve the current number of hits for the object
    hits = hit_count.hits

    # Initialize hitcontext within the context dictionary
    hitcontext = context["hitcount"] = {"pk": hit_count.pk}

    # Use the HitCountMixin to update the hit count for the object
    hit_count_response = HitCountMixin.hit_count(request, hit_count)

    # Check if the hit count was successfully updated
    if hit_count_response.hit_counted:
        # Increment the hit count by 1
        hit = hits + 1

        # Update hitcontext with information about the hit count
        hitcontext["hitcounted"] = hit_count_response.hit_counted
        hitcontext["hit_message"] = hit_count_response.hit_message
