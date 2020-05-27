import os
import xadmin
from xadmin import views
from import_export import resources
from .models import DataItem
from django.apps import apps
from .db_utils import process_excel_file, process_data, save_file

class DataItemResource(resources.ModelResource):
    def __init__(self):
        super(DataItemResource,self).__init__()
        field_list = apps.get_model('task', 'DataItem')._meta.fields
        self.verbose_name_dict = {}
        for i in field_list:
            self.verbose_name_dict[i.name] = i.verbose_name

    def get_export_fields(self):
        fields = self.get_fields()
        for filed in fields:
            filed_name = self.get_field_name()
            if filed_name in self.verbose_name_dict.keys():
                filed.column_name = self.verbose_name_dict[filed_name]

    class Meta:
        model = DataItem
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('img_name', 'txt', 'task')
        fields = ('mid', 'img_name', 'txt', 'task')
        exclude = ('id')


from task.models import LabelClass, LabelSubClass, Task, DataItem

class LabelClassInline(object):
    model = LabelClass
    extra = 0

class TaskAdmin(object):
    list_display = ['id','name', 'creator', 'has_finished', 'creator']
    search_fields = ['name', 'creator']
    readonly_fields = ['has_finished', 'has_distributed', 'creator']
    inlines = [LabelClassInline]


    def save_models(self):
        obj = self.new_obj
        obj.creator = self.request.user
        obj.save()

    def queryset(self):
        qs = super(TaskAdmin, self).queryset()
        user = self.request.user
        if user.is_superuser == 1:
            return qs
        qs = qs.filter(creator = user)
        return qs

class LabelClassAdmin(object):
    list_display = ['name', 'task']
    ordering = ['task']

    def queryset(self):
        qs = super(LabelClassAdmin, self).queryset()
        user = self.request.user
        if user.is_superuser == 1:
            return qs
        qs = qs.filter(task__creator = user)
        return qs

class LabelSubClassAdmin(object):
    list_display = ['name', 'parent', 'get_task']
    ordering = ['parent__task', 'parent']

    def queryset(self):
        qs = super(LabelSubClassAdmin, self).queryset()
        user = self.request.user
        if user.is_superuser == 1:
            return qs
        qs = qs.filter(parent__task__creator = user)
        return qs

class DataItemAdmin(object):
    list_display = ['mid', 'task']
    ordering = ['task']
    list_filter = ['task']
    # 配置导入导出按钮
    import_export_args = {
        'import_resource_class': DataItemResource
    }
    import_excel = True

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            # 可以增加逻辑代码
            file = request.FILES.get('excel')
            data = file.readlines()
            save_file(file.name, data)
            data_list = process_data(data)
        return super(DataItemAdmin, self).post(request, args, kwargs)

    def queryset(self):
        qs = super(DataItemAdmin, self).queryset()
        user = self.request.user
        if user.is_superuser == 1:
            return qs
        qs = qs.filter(task__creator = user)
        return qs

xadmin.site.register(Task, TaskAdmin)
xadmin.site.register(LabelClass, LabelClassAdmin)
xadmin.site.register(LabelSubClass, LabelSubClassAdmin)
xadmin.site.register(DataItem, DataItemAdmin)

class GlobalSettings(object):
    # 修改title
    site_title = '图文联合标注平台'
    # 修改footer
    site_footer = '图文联合标注平台'
    # 收起菜单
    menu_style = 'accordion'


xadmin.site.register(views.CommAdminView, GlobalSettings)
