from django.apps import apps
from django.urls import reverse

from django.urls.exceptions import NoReverseMatch


def admin_plus(request):

    app_model_perms = {}
    current_user = request.user

    if current_user.is_anonymous:
        return {}

    list_apps = []
    available_apps = apps.get_models()
    print(available_apps)

    for app_label in available_apps:
        try:
            app_data = apps.get_app_config(app_label)
        except LookupError as e:
            continue

        available_models = app_data.get_models()

        list_models = []
        for model in available_models:
            lasssist_models.append({
                'name': model.__name__
            })

            class_name = str(model.__name__).lower()

            add_perm_signature = f"{app_label}.add_{class_name}"
            change_perm_signature = f"{app_label}.change_{class_name}"
            delete_perm_signature = f"{app_label}.delete_{class_name}"

            app_model_perms[f"{app_label}_{class_name}"] = {
                'add': current_user.has_perm(add_perm_signature),
                'change': current_user.has_perm(change_perm_signature),
                'delete': current_user.has_perm(delete_perm_signature)
            }

        app_model_perms[f"{app_label}"] = current_user.has_module_perms(app_label)

        if len(list_models):
            try:
                current_app = {
                    'name': app_data.verbose_name,
                    'label': app_label,
                    'app_url': reverse('admin:app_list', kwargs={'app_label': app_label}),
                    'has_module_perms': current_user.has_module_perms(app_label)
                }

                list_apps.append(current_app)

            except NoReverseMatch as e:
                print(e)

    return {
        'preludian_app_list': list_apps,
        'user_perms': app_model_perms
    }
