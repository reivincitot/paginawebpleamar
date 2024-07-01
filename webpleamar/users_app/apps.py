from django.apps import AppConfig
from django.db.models.signals import post_migrate


class UsersAppConfig(AppConfig):
    name = "users_app"

    def ready(self):
        from django.contrib.auth.models import Group, Permission
        from django.contrib.contenttypes.models import ContentType
        from .models import CustomUser

        def create_groups_and_permissions(sender, **kwargs):
            content_type = ContentType.objects.get_for_model(CustomUser)
            permissions = [
                ('can_post_gallery', 'Puede realizar publicaciones en la galería'),
                ('can_organize_groups', 'Puede organizar grupos'),
                ('can_manage_users', 'Puede manejar usuarios'),
                ('can_modify_posts', 'Puede modificar publicaciones'),
                ('can_modify_competitions', 'Puede modificar competiciones')
            ]

            for codename, name in permissions:
                Permission.objects.get_or_create(codename=codename, name=name, content_type=content_type)

            groups_permissions = {
                'usuario_basico': ['can_post_gallery'],
                'capitanes': ['can_post_gallery', 'can_organize_groups'],
                'administradores': [
                    'can_post_gallery', 'can_organize_groups', 'can_manage_users', 
                    'can_modify_posts', 'can_modify_competitions'
                ],
                'presidente': [
                    'can_post_gallery', 'can_organize_groups', 'can_manage_users', 
                    'can_modify_posts', 'can_modify_competitions'
                ],
            }

            for group_name, perms in groups_permissions.items():
                group, created = Group.objects.get_or_create(name=group_name)
                for perm in perms:
                    try:
                        permission = Permission.objects.get(codename=perm)
                        group.permissions.add(permission)
                    except Permission.DoesNotExist:
                        print(f"Permission {perm} does not exist.")

        post_migrate.connect(create_groups_and_permissions, sender=self)
