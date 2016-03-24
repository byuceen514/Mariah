from tethys_sdk.base import TethysAppBase, url_map_maker


class MyDemo(TethysAppBase):
    """
    Tethys app class for My Demo.
    """

    name = 'My Demo'
    index = 'my_demo:home'
    icon = 'my_demo/images/icon.gif'
    package = 'my_demo'
    root_url = 'my-demo'
    color = '#1abc9c'
    description = 'Place a brief description of your app here.'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='my-demo',
                           controller='my_demo.controllers.home'),
        )

        return url_maps