from django.contrib import admin
from hsg.models import Group, GroupContact, GroupEmail, PostAddress, RegInfo


# class RegInfoInline(admin.TabularInline):
#     model = Group.registration.through
#     raw_id_fields = ('year', 'form',)
#     max_num = 1

class GroupAddressInline(admin.StackedInline):
    model = PostAddress
    exclude = ['person', ]

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return extra - obj.address.count()
        return extra


class GroupEmailInline(admin.StackedInline):
    model = GroupEmail
    max_num = 3

    def get_extra(self, request, obj=None, **kwargs):
        extra = 3
        if obj:
            return extra - obj.listemail.count()
        return extra


class GroupAdmin(admin.ModelAdmin):
    inlines = [
        GroupEmailInline,
        GroupAddressInline,
    ]
#     exclude = ('registration',)


class RegInfoContactInline(admin.TabularInline):
    model = GroupContact


class RegInfoAdmin(admin.ModelAdmin):
    inlines = [RegInfoContactInline,
               ]
    fieldsets = [
        (None,          {'fields': ['group', 'date', 'members']}),
        ('Process',     {'fields': ['documents', 'constitution', 'form',
                                    'duedate', 'comment']})
    ]
    list_display = ('group', 'date', 'form', 'comment')
    list_filter = ['date', 'group__name']
    search_fields = ['group__name']

admin.site.register(Group, GroupAdmin)
admin.site.register(RegInfo, RegInfoAdmin)
admin.site.register(GroupContact)
