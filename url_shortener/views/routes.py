from .handlers import (
    public_resource_example,
    protected_resource_read_example,
    protected_resource_write_example,
    notfound,
    forbidden,
    create_user,
    login_user
)

PROTECTED = 'url_shortener.auth.protected'


def setup_routes(config):
    """ Configures application routes"""

    # User registration
    config.add_route('create_user',
                     request_method='POST',
                     pattern='/register')
    config.add_view(create_user,
                    route_name='create_user')

    # User login
    config.add_route('login_user',
                     request_method='POST',
                     pattern='/login')
    config.add_view(login_user,
                    route_name='login_user')

    # Add error views
    config.add_notfound_view(notfound)
    config.add_forbidden_view(forbidden)

    return config
