import json

from rest_framework.renderers import JSONRenderer


class ProfileJSONRenderer(JSONRenderer):
    charset= 'utf-8'

    def render(self, data, accepted_media_types=None, renderer_context=None):
        errors= data.get("error", None)

        if errors is not None:
            return super(ProfileJSONRenderer, self).render(data)
        
        # return a namespace of profile
        return json.dumps({"profile": data})