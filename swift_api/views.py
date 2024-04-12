from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ListItem
from datetime import datetime
from .mock_data import MOCK_DATA
import json

@csrf_exempt
def filter_list(request):
    if request.method == 'POST':
        filter_criteria_json = request.body.decode('utf-8')
        filter_criteria = json.loads(filter_criteria_json)

        if filter_criteria:
            filtered_list = []
            for item in MOCK_DATA:
                include_item = True

                if filter_criteria.get('AccountNumber') is not None and filter_criteria.get('AccountNumber') != '':
                    if filter_criteria['AccountNumber'] != item['AccountNumber']:
                        include_item = False

                if filter_criteria.get('TransactionId') is not None and filter_criteria.get('TransactionId') != '':
                    if filter_criteria['TransactionId'] != item['TransactionId']:
                        include_item = False


                if filter_criteria.get('TransferStatus') is not None and filter_criteria.get('TransferStatus') != '':
                    if filter_criteria['TransferStatus'] != item['TransferStatus']:
                        include_item = False


                if filter_criteria.get('TransactionType') is not None and filter_criteria.get('TransactionType') != '':
                    if filter_criteria['TransactionType'] != item['TransactionType']:
                        include_item = False


                if filter_criteria.get('CommissionDate') is not None and filter_criteria.get('CommissionDate') != '':
                    if filter_criteria['CommissionDate'] != item['CommissionDate']:
                        include_item = False

                if filter_criteria.get('CommissionApplied') is not None and filter_criteria.get('CommissionApplied') != '':
                    if filter_criteria['CommissionApplied'] != item['CommissionApplied']:
                        include_item = False

                if filter_criteria.get('CommissionState') is not None and filter_criteria.get('CommissionState') != '':
                    if filter_criteria['CommissionState'] != item['CommissionState']:
                        include_item = False

                if filter_criteria.get('OpperationStartDate') is not None and filter_criteria.get('OpperationStartDate') != '':
                    if filter_criteria['OpperationStartDate'] > item['OpperationDate']:
                        include_item = False


                if filter_criteria.get('OpperationEndDate') is not None and filter_criteria.get('OpperationEndDate') != '':
                    if filter_criteria['OpperationEndDate'] < item['OpperationDate']:
                        include_item = False

                if include_item:
                    filtered_list.append(item)

            return JsonResponse(filtered_list, safe=False)

        else:
            # If no filter criteria provided, return all items
            return JsonResponse(MOCK_DATA, safe=False)

    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)