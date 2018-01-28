# (c) 2012-2018, Ansible by Red Hat
#
# This file is part of Ansible Galaxy
#
# Ansible Galaxy is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by
# the Apache Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# Ansible Galaxy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Apache License for more details.
#
# You should have received a copy of the Apache License
# along with Galaxy.  If not, see <http://www.apache.org/licenses/>.

import logging

from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from django.core.exceptions import ObjectDoesNotExist

from galaxy.main.models import Provider
from .base_views import ListAPIView
from ..githubapi import GithubAPI

__all__ = (
    'RepositorySourceList',
)

logger = logging.getLogger(__name__)


class ProviderRepositoryList(ListAPIView):
    """ Repositories available for a given provider and namespace """
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        # Return a list of repositories from the provider for a given namespace
        request_provider = kwargs.get('provider')
        request_namespace = kwargs.get('namespace')

        try:
            provider = Provider.objects.get(name__iexact=request_provider.lower(), active=True)
        except ObjectDoesNotExist:
            raise APIException("Invalid provider {0}".format(request_provider))

        sources += GithubAPI(user=request.user,
                                     provider_name=provider.name).user_namespaces()
        return Response(sources, status=status.HTTP_200_OK)
