from django.contrib import admin

from .models import Tweet, Reaction, ReactionType, TweetImages,Reply,ReplyReaction


@admin.display(description='Short Text')
def get_short_text(obj):
    return f'{obj.text[:20]}...'


class TweetImagesInline(admin.TabularInline):
    model = TweetImages
    extra = 1


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    inlines = [
        TweetImagesInline
    ]
    date_hierarchy = 'created_add'
    actions_on_bottom = True
    actions_on_top = False
    empty_value_display = "--empty--"
    # exclude = ['profile', 'image']
    # fields = ['text', ]
    fields = (('text','profile'),'image')
    list_display = ['id','get_profile_fullname','get_reactions_str',get_short_text,'image','created_add']
    list_display_links = [get_short_text, 'id']
    list_editable = ['image', ]
    list_filter = ['created_add','profile']
    list_per_page = 2
    save_as = True
    save_on_top = True
    search_fields = ['text','profile__user__username__exact']
    sortable_by = ['created_add','id']

    @admin.display(description='Fullname')
    def get_profile_fullname(self,obj):
        return obj.profile.user.get_full_name()


@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    pass


@admin.register(ReactionType)
class ReactionTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Reply)
class ReplayAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_add'
    actions_on_bottom = True
    actions_on_top = False
    empty_value_display = "-"
    fields = (('text','profile'),'tweet')
    list_display = ['id','get_full_name',get_short_text,'created_add','get_reactions_str','profile']
    list_display_links = [get_short_text,]
    list_editable = ['profile']
    search_fields = ['text','profile__user__username']
    list_filter = ['created_add','id']
    sortable_by = ['id','created_add']

    @admin.display(description='fullname')
    def get_full_name(self,obj):
        return obj.profile.user.get_full_name()


@admin.register(ReplyReaction)
class ReplyReactionsAdmin(admin.ModelAdmin):
    pass





