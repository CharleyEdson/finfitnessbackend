from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import netWorth
from .serializers import netWorthSerializer
from netWorth.models import netWorth
from Asset.serializers import AssetSerializer
from django.shortcuts import get_object_or_404
from authentication.models import User
from Asset.models import Asset
from Liability.models import Liability
from datetime import date


# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_net_worth(request):
    net_worth = netWorth.objects.filter(user_id=request.user.id).order_by('-id')[:1]
    serializer = netWorthSerializer(net_worth, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_historical_net_worth(request):
    net_worth = netWorth.objects.filter(user_id=request.user.id).order_by('-date')
    serializer = netWorthSerializer(net_worth, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_net_worth(request,pk):
    net_worth = get_object_or_404(netWorth,pk=pk)
    net_worth.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


#When database get's large, slice the objects retried using [:1]
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def calculate_net_worth(request):
    today = date.today()
    print(
    'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'GET':

        cash = Asset.objects.filter(user_id=request.user.id).filter(asset_type='Cash').order_by('-date')
        cashes = []
        for obj in cash:
            cashes.append(obj.value)
        cash_networth = cashes[0]

        cash_networth = 0

        real_estate = Asset.objects.filter(user_id=request.user.id).filter(asset_type='Real Estate').order_by('-date')
        real_estates = []
        for obj_R in real_estate:
            real_estates.append(obj_R.value)
        real_estate_networth = real_estates[0]

        brokerage = Asset.objects.filter(user_id=request.user.id).filter(asset_type='Brokerage').order_by('-date')
        brokerages = []
        for obj_B in brokerage:
            brokerages.append(obj_B.value)
        brokerage_networth = brokerages[0]
        retirement = Asset.objects.filter(user_id=request.user.id).filter(asset_type='Retirement').order_by('-id')
        retirements = []
        for obj_Ret in retirement:
            retirements.append(obj_Ret.value)
        retirement_networth = retirements[0]
        misc = Asset.objects.filter(user_id=request.user.id).filter(asset_type='Misc').order_by('-date')
        miscs = []
        for obj_M in misc:
            miscs.append(obj_M.value)
        misc_networth = miscs[0]
        total_assets = int(cash_networth) + int(real_estate_networth) + int(brokerage_networth) + int(retirement_networth) + int(misc_networth) 
        
        mortgage = Liability.objects.filter(user_id=request.user.id).filter(type_of_liability='Mortgage').order_by('-date')
        mortgages = []
        for obj_Mort in mortgage:
            mortgages.append(obj_Mort.value)
        mortgage_networth = mortgages[0]
        auto_loan = Liability.objects.filter(user_id=request.user.id).filter(type_of_liability='Auto Loan').order_by('-date')
        auto_loans = []
        for obj_auto in auto_loan:
            auto_loans.append(obj_auto.value)
        auto_loan_networth = auto_loans[0]
        student_loan = Liability.objects.filter(user_id=request.user.id).filter(type_of_liability='Student Loan').order_by('-date')
        student_loans = []
        for obj_student in student_loan:
            student_loans.append(obj_student.value)
        student_loan_networth = student_loans[0]
        cc_loan = Liability.objects.filter(user_id=request.user.id).filter(type_of_liability='Credit Card Loan').order_by('-date')
        cc_loans = []
        for obj_cc in cc_loan:
            cc_loans.append(obj_cc.value)
        cc_loan_networth = cc_loans[0]
        misc_loan = Liability.objects.filter(user_id=request.user.id).filter(type_of_liability='Misc').order_by('-date')
        misc_loans = []
        for obj_miscl in misc_loan:
            misc_loans.append(obj_miscl.value)
        misc_loan_networth = misc_loans[0]
        total_liabilities = int(mortgage_networth) + int(auto_loan_networth) + int(student_loan_networth) + int(cc_loan_networth) + int(misc_loan_networth)
        total_net_worth = total_assets - total_liabilities
        print(total_assets)
        print(total_liabilities)
        print(total_net_worth)
        # return(Response(total_net_worth))
        new_net_worth = netWorth.objects.create(user=request.user, netWorth=total_net_worth, asset_total=total_assets, liabilities_total=total_liabilities, date=today)
        net_worth = netWorth.objects.filter(user_id=request.user.id)
        serializer = netWorthSerializer(net_worth, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def calculate_net_worth_once_a_day(request):
    today = date.today()
    print(
    'User ', f"{request.user.id} {request.user.email} {request.user.username}")             
    try:
        cash = Asset.objects.filter(user_id=request.user.id).filter(asset_type='Cash').order_by('-id')
        cashes = []
        for obj in cash:
            cashes.append(obj.value)
        cash_networth = cashes[0]
    except:
        cash_networth = 0
    try: 
        real_estate = Asset.objects.filter(user_id=request.user.id).filter(asset_type='Real Estate').order_by('-id')
        real_estates = []
        for obj_R in real_estate:
            real_estates.append(obj_R.value)
        real_estate_networth = real_estates[0]
    except:
        real_estate_networth = 0
    try: 
        brokerage = Asset.objects.filter(user_id=request.user.id).filter(asset_type='Brokerage').order_by('-id')
        brokerages = []
        for obj_B in brokerage:
            brokerages.append(obj_B.value)
        brokerage_networth = brokerages[0]
    except:
        brokerage_networth = 0
    try:
        retirement = Asset.objects.filter(user_id=request.user.id).filter(asset_type='Retirement').order_by('-id')
        retirements = []
        for obj_Ret in retirement:
            retirements.append(obj_Ret.value)
        retirement_networth = retirements[0]
    except:
        retirement_networth = 0
    try:
        misc = Asset.objects.filter(user_id=request.user.id).filter(asset_type='Misc').order_by('-id')
        miscs = []
        for obj_M in misc:
            miscs.append(obj_M.value)
        misc_networth = miscs[0]
    except:
        misc_networth = 0
    total_assets = int(cash_networth) + int(real_estate_networth) + int(brokerage_networth) + int(retirement_networth) + int(misc_networth) 
    
    try:
        mortgage = Liability.objects.filter(user_id=request.user.id).filter(type_of_liability='Mortgage').order_by('-id')
        mortgages = []
        for obj_Mort in mortgage:
            mortgages.append(obj_Mort.value)
        mortgage_networth = mortgages[0]
    except:
        mortgage_networth = 0
    try:
        auto_loan = Liability.objects.filter(user_id=request.user.id).filter(type_of_liability='Auto Loan').order_by('-id')
        auto_loans = []
        for obj_auto in auto_loan:
            auto_loans.append(obj_auto.value)
        auto_loan_networth = auto_loans[0]
    except:
        auto_loan_networth = 0
    try:
        student_loan = Liability.objects.filter(user_id=request.user.id).filter(type_of_liability='Student Loan').order_by('-id')
        student_loans = []
        for obj_student in student_loan:
            student_loans.append(obj_student.value)
        student_loan_networth = student_loans[0]
    except:
        student_loan_networth = 0
    try:
        cc_loan = Liability.objects.filter(user_id=request.user.id).filter(type_of_liability='Credit Card Loan').order_by('-id')
        cc_loans = []
        for obj_cc in cc_loan:
            cc_loans.append(obj_cc.value)
        cc_loan_networth = cc_loans[0]
    except:
        cc_loan_networth = 0
    try:
        misc_loan = Liability.objects.filter(user_id=request.user.id).filter(type_of_liability='Misc').order_by('-id')
        misc_loans = []
        for obj_miscl in misc_loan:
            misc_loans.append(obj_miscl.value)
        misc_loan_networth = misc_loans[0]
    except:
        misc_loan_networth = 0
    total_liabilities = int(mortgage_networth) + int(auto_loan_networth) + int(student_loan_networth) + int(cc_loan_networth) + int(misc_loan_networth)
    total_net_worth = total_assets - total_liabilities
    current_net_worth = netWorth.objects.filter(user_id=request.user.id).order_by('-id').first()
    try:
        if current_net_worth.date == today:
            current_net_worth.netWorth = total_net_worth
            current_net_worth.asset_total=total_assets
            current_net_worth.liabilities_total=total_liabilities
            current_net_worth.save()
        else:
            new_net_worth = netWorth.objects.create(user=request.user, netWorth=total_net_worth, asset_total=total_assets, liabilities_total=total_liabilities, date=today)
    except:
        new_net_worth = netWorth.objects.create(user=request.user, netWorth=total_net_worth, asset_total=total_assets, liabilities_total=total_liabilities, date=today)
    net_worth = netWorth.objects.filter(user_id=request.user.id)
    serializer = netWorthSerializer(net_worth, many=True)
    return Response(serializer.data)
