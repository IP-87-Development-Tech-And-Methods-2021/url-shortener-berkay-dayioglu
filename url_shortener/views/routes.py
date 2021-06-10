from .handlers import (
    public_resource_example,
    protected_resource_read_example,
    protected_resource_write_example,
    notfound,
    forbidden,
    create_user
)

PROTECTED = 'url_shortener.auth.protected'


def setup_routes(config):
    """ Configures application routes"""
    # Add public resources

    # User registration
    config.add_route('create_user',
                    request_method='POST',
                    pattern='/register')
    config.add_view(create_user,
                    route_name='create_user',
                    renderer='json')

    config.add_view(public_resource_example,
                    route_name='public_resource_example',
                    renderer='json')
    config.add_route('public_resource_example', '/public')

    # Add protected resources
    # pass `factory=PROTECTED` to the `add_route` method
    # in order to make this resource available for authenticated users only
    config.add_route('protected_resource_write_example',
                     request_method='PUT',
                     pattern='/resource/{key}',
                     factory=PROTECTED)
    config.add_view(protected_resource_write_example,
                    route_name='protected_resource_write_example',
                    permission='write')

    config.add_route('protected_resource_read_example',
                     request_method='GET',
                     pattern='/resource/{key}',
                     factory=PROTECTED)
    config.add_view(protected_resource_read_example,
                    route_name='protected_resource_read_example',
                    permission='read')

    # Add error views
    config.add_notfound_view(notfound)
    config.add_forbidden_view(forbidden)

    return config
