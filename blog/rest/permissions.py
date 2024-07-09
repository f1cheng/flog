# _*_ coding:utf-8 _*_
from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    仅管理员用户可以修改，其他用户查看
    """
    def has_permission(self, request, view):
        #GET,HEAD,OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser
