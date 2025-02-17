import matplotlib
matplotlib.use('Agg')  # Ensure no GUI backend is used

import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import Plot
from .serializers import PlotSerializer

class PlotAPIView(APIView):
    def post(self, request, format=None):
        serializer = PlotSerializer(data=request.data)
        if serializer.is_valid():
            plot = serializer.save()

            x = np.array(plot.x_values)
            y = np.array(plot.y_values)
            plt.plot(x, y)

            buf = BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)

            return HttpResponse(buf, content_type='image/png')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        plot = Plot.objects.last()
        if not plot:
            return Response({"detail": "No plots available."}, status=status.HTTP_404_NOT_FOUND)

        x = np.array(plot.x_values)
        y = np.array(plot.y_values)
        plt.plot(x, y)

        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        return HttpResponse(buf, content_type='image/png')
