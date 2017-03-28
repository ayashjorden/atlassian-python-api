import logging
from atlassian import AtlassianRestAPI


log = logging.getLogger('atlassian.servicedesk')
REST_EP = '/rest/servicedeskapi/%s'


class Servicedesk(AtlassianRestAPI):

    def info(self):
        return self.get(REST_EP % 'info')

    def request_create(self,  service_desk_id, request_type_id, request_fields):
        for f in ['summary', 'description']:
            if f not in request_fields:
                raise ValueError('%s is missing in request_fields' % f)
        return self.post(REST_EP % 'request', data={
            'serviceDeskId': service_desk_id,
            'requestTypeId': request_type_id,
            'requestFieldValues': request_fields
        })
