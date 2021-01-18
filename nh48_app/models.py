from django.db import models
from datetime import date
from nh48_user.models import NHUser


class Post(models.Model):
    time_posted = models.DateTimeField(auto_now=True)
    mountain_image = models.ImageField(upload_to='images/', null=True, blank=True)
    poster = models.ForeignKey(NHUser, on_delete=models.CASCADE, related_name="poster")
    caption = models.CharField(max_length=280, null=True, blank=True)
    OPTIONS = (('washington', 'Washington'), ('adams', 'Adams'), ('jefferson', 'Jefferson'), ('monroe', 'Monroe'), ('madison', 'Madison'), ('lafayette', 'Lafayette'), ('lincoln', 'Lincoln'), ('south twin', 'South Twin'), ('carter dome', 'Carter Dome'), ('moosilauke', 'Moosilauke'), ('eisenhower', 'Eisenhower'), ('north twin', 'North Twin'), ('carrigain', 'Carrigain'), ('bond', 'Bond'), ('middle carter', 'Middle Carter'), ('west bond', 'West Bond'), ('garfield', 'Garfield'), ('liberty', 'Liberty'), ('south carter', 'South Carter'), ('wildcat', 'Wildcat'), ('hancock', 'Hancock'), ('south kinsman', 'South Kinsman'), ('field', 'Field'), ('osceola', 'Osceola'), ('flume', 'Flume'), ('south hancock', 'South Hancock'), ('pierce', 'Pierce'), ('north kinsman', 'North Kinsman'), ('willey', 'Willey'), ('bondcliff', 'Bondcliff'), ('zealand', 'Zealand'), ('north tripyramid', 'North Tripyramid'), ('cabot', 'Cabot'), ('east osceola', 'East Osceola'), ('middle tripyramid', 'Middle Tripyramid'), ('cannon', 'Cannon'), ('wildcat d', 'Wildcat D'), ('hale', 'Hale'), ('jackson', 'Jackson'), ('tom', 'Tom'), ('moriah', 'Moriah'), ('passaconaway', 'Passaconaway'), ("owls head", "Owl's Head"), ('galehead', 'Galehead'), ('whiteface', 'Whiteface'), ('waumbek', 'Waumbek'), ('isolation', 'Isolation'), ('tecumseh', 'Tecumseh'))
    mountain = models.CharField(max_length=25, choices=OPTIONS)

