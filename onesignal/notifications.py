
class Notification(object):
    def __init__(self):
        super(self, Notification).__init__()
        self.included_segments = []
        self.excluded_segments = []
        self.filters = []
        self.include_player_ids = []
        self.app_ids = []
        self.platforms_to_deliver_to = []
        self.content = None
        
        def add_segment(segment_name):
            self.included_segments.append(segment_name)

        def add_excluded_segment(segment_name):
            self.excluded_segments.append(segment_name)

        def add_filter(self, **kwargs):
            field = kwargs.get('field')
            if field in ["last_session", "first_session", "session_count",
                         "session_time", "amount_spent", "language", "app_version",
                         "country"]:
                self._add_filter_relation_value(
                    relation=kwargs.get('relation'),
                    value=kwargs.get('value'),
                    operator=kwargs.get('operator', "AND")))
            elif field in ["bought_sku", "tag"]:
                self._add_filter_relation_key_value(
                    key=kwargs.get('key'),
                    relation=kwargs.get('realtion'),
                    value=kwargs.get('value'),
                    operator=kwargs.get('operator', "AND"))
            elif field in ["location"]:
                self._add_lat_lng_radius(
                    lat=kwargs.get('lat'),
                    lng=kwargs.get('lng'),
                    value=kwargs.get('value'),
                    operator=kwargs.get('operator', "AND"))

        def _add_filter_relation_value(self, relation, value, operator="AND"):
            self.filter.append({"relation": relation, "value": value, "operator": operator})

        def _add_filter_relation_key_value(self, key, relation, value, operator="AND"):
            self.filter.append({"relation": relation, "key": key, "value": value, "operator": operator})

        def _add_lat_lng_radius(self, lat, lng, radius, operator="AND"):
            self.filter.append({"radius": radius, "lat": lat, "lng": lng, "operator": operator})

        def add_player_ids(self, player_ids):
            self.include_player_ids = self.include_player_ids + player_ids

        def add_app_id(self, app_id):
            self.app_ids.append(app_id)

        def add_app_ids(self, add_ids):
            self.app_ids = self.app_ids + add_ids

        
class Content(object):
    def __init__(self):
        super(self, Content).__init__()
        self.contents = {}
        self.headings = {}
        self.subtitle = {}
        self.template_id = None
        self.content_available = False
        self.mutable_content = False

    def add_content(text, lang="en"):
        self.contents[lang] = text

    def add_heading(text, lang="en"):
        self.headings[lang] = text

    def add_subtitle(text, lang="en"):
        self.subtitle[lang] = text


class Attachments(object):
    def __init__(self):
        super(self, Attachments).__init__()
        self.data = None
        self.url = None
        self.ios_attachments = {}
        self.big_picture = {"big_picture": None, "adm_big_picture": None, "chrome_big_picture": None}

    def set_ios_attachments(media_id, media_url):
        self.ios_attachments[media_id] = media_url

    def set_android_big_picture(self, url):
        self.big_picture["big_picture"] = url

    def set_amazon_big_picture(self, url):
        self.big_picture["adm_big_picture"] = url

    def set_chrome_big_picture(self, url):
        self.big_picture["chrome_big_picture"] = url

    def set_big_picture(self, url):
        for k in self.big_picture.keys():
            self.big_picture[k] = url
            
class ActionButtons(object):
    def __init__(self):
        super(self, ActionButtons).__init__()
        self.buttons = {"mobile": [], "web":[]}
        self.ios_category = None

    def add_mobile_button(self, button_id, text, icon):
        self.buttons["mobile"].append({"id": button_id, "text": text, "icon": icon})

    def add_web_button(self, button_id, text, icon, url):
        self.buttons["web"].append({"id": button_id, "text": text, "icon": icon, "url": url})

    def add_button(self, button_id, text, icon, url):
        self.add_mobile_button(button_id=button_id, text=text, icon=icon)
        self.add_web_button(button_id=button_id, text=text, icon=icon, url=url)

    

class Appearance(object):
    ANDROID_VISIBILITY_PUBLIC = 1
    ANDROID_VISIBILITY_PRIVATE = 0
    ANDROID_VISIBILITY_SECRET = -1

    IOS_BADGE_TYPE_NONE = "None"
    IOS_BADGE_TYPE_SET_TO = "SetTo"
    IOS_BADGE_TYPE_INCREASE = "Increase"
    
    def __init__(self):
        super(self, Appearance).__init__()
        self.android_channel_id = None
        self.existing_android_channel_id = None
        self.background_layout = {"android_background_layout":{
            "image": None,
            "headings_color": None,
            "contents_color": None
            }}
        self.small_icon = {
            "small_icon": None, "adm_small_icon": None
        }
        self.large_icon = {
            "large_icon": None,
            "adm_large_icon": None
        }
        self.web = {
            "chrome_web_icon": None,
            "chrome_web_image": None
        }
        self.sound = {"ios_sound": None, "android_sound": None, "adm_sound": None, "wp_sound": None }
        self.android_led_color = None
        self.android_accent_color = None
        self.android_visibility = Appearance.ANDROID_VISIBILITY_PUBLIC
        self.ios_badge_type = None
        self.ios_badgeCount = None
        self.collapse_id = None

        def set_android_background_layout(self, **kwargs):
            for k, v in kwargs.iteritems():
                self.background_layout["android_background_layout"][k] = v

    
class Delivery(object):
    DELAYED_OPTION_TIMEZONE = "timezone"
    DELAYED_OPTION_LAST_ACTIVE = "last-active"
    DELAYED_OPTION_SEND_AFTER = "send_after"
    
    def __init__(self):
        super(self, Delivery).__init__()
        self.send_after = None
        self.delayed_option = None
        self.delivery_time_of_day = None
        self.ttl = 259_200
        self.priority = None

    def set_send_after(self, **kwargs):
        pass

    def _parse_to_json(self):
        return _parse_to_json(self)
    
class GroupingCollapsing(object):
    def __init__(self):
        super(self, GroupingCollapsing).__init__()
        self.group = {"android_group": None, "amazon_group": None }
        self.group_message = {"android_group_message": {}, "adm_group_message": {}} # include $[notif_count]

    def set_android_group(self, group_id):
        self.group["android_group"] = group_id

    def set_amazon_group(self, group_id):
        self.group["amazon_group"] = group_id

    def set_group(self, group_id):
        self.set_android_group(group_id=group_id)
        self.set_amazon_group(group_id=group_id)

    def set_android_group_message(self, text, lang="en"):
        self.group_message["android_group_message"][lang] = text

    def set_amazon_group_message(self, text, lang="en"):
        self.group_message["adm_group_message"][lang] = text

    def set_group_message(self, text, lang="en"):
        self.set_android_group_message(text=text, lang=lang)
        self.set_amazon_group_message(text=text, lang=lang)

    def _parse_to_json(self):
        return _parse_to_json(self)
    
def _parse_to_json(obj):
    o_dict = {}
    for attr in obj.__dict__.keys():
        attr_val = getattr(obj, attr)
        if isinstance(attr_val, dict):
            for k, v in attr_val.iteritems():
                o_dict[k] = attr_val
        else:
            o_dict[attr] = attr_val
    return o_dict
