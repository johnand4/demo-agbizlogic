from rest_framework.viewsets import ModelViewSet
from scenario.serializers import DepreciationsSerializer
from scenario.models import Depreciations, Scenario
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated



class DepreciationsViewSet(ModelViewSet):
    """ API endpoint for the Depreciations model.
    """

    serializer_class = DepreciationsSerializer
    queryset = Depreciations.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """ Override this method to filter queryset based on URL parameters.
            Default queryset is all Scenario objects. Invalid arguments return empty queryset.
        """

        queryset = Depreciations.objects.all()
        query_params = self.request.query_params

        # Filter by scenario
        if "scenario" in query_params:
            scenario_query = Scenario.objects.filter(id=query_params["scenario"])

            if scenario_query:
                queryset = Depreciations.objects.filter(scenario=scenario_query[0])
            else:
                queryset = None

        # If there are query parameters that aren't supported, return empty array
        for key in query_params.keys():
            if key not in {'scenario', 'fields'}:
                queryset = None

        return queryset
