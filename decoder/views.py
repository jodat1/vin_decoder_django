from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from playwright.sync_api import sync_playwright
from .serializers import VINDecoderInputSerializer

class DecodeVINAPIView(APIView):
    def post(self, request):
        serializer = VINDecoderInputSerializer(data=request.data)
        if serializer.is_valid():
            vin = serializer.validated_data['vin']

            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)  # Launch in headless mode
                page = browser.new_page()

                try:
                    page.goto("https://vpic.nhtsa.dot.gov/decoder")
                    page.fill('#VIN', vin)  # Fill the VIN input field
                    page.click('#btnSubmit')  # Click the decode button

                    # Wait for the results to be visible
                    page.wait_for_selector('#decodedModelYear')
                    
                    year = page.query_selector('#decodedModelYear').inner_text()
                    make = page.query_selector('#decodedMake').inner_text()
                    model = page.query_selector('#decodedModel').inner_text()

                    result = {"year": year, "make": make, "model": model}
                    return Response(result, status=status.HTTP_200_OK)
                finally:
                    browser.close()
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
