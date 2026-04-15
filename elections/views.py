
# Create your views here.
from django.shortcuts import render
from django.db.models import Sum
from .models import PollingUnit, AnnouncedPUResult, LGA
from .forms import PollingUnitForm, LGAForm
from django.utils import timezone

def home(request):
    return render(request, 'elections/home.html')



# =========================
# Q1: Polling Unit Results
# =========================
def polling_unit_results(request):
    form = PollingUnitForm()
    results = None

    if request.GET.get('polling_unit'):
        pu_id = request.GET.get('polling_unit')
        results = AnnouncedPUResult.objects.filter(
            polling_unit_uniqueid=pu_id
        )

    return render(request, 'elections/polling_unit.html', {
        'form': form,
        'results': results
    })


# =========================
# Q2: LGA Total Results
# =========================
def lga_results(request):
    form = LGAForm()
    results = None

    if request.GET.get('lga'):
        lga_id = request.GET.get('lga')

        pu_ids = PollingUnit.objects.filter(lga_id=lga_id).values_list('uniqueid', flat=True)

        results = AnnouncedPUResult.objects.filter(
            polling_unit_uniqueid__in=pu_ids
        ).values('party_abbreviation').annotate(
            total=Sum('party_score')
        ).order_by('-total')

    return render(request, 'elections/lga_results.html', {
        'form': form,
        'results': results
    })


# =========================
# Q3: Add Results
# =========================
def add_results(request):
    polling_units = PollingUnit.objects.all()

    if request.method == "POST":
        pu_id = request.POST.get('polling_unit')

        VALID_PARTIES = ['PDP', 'DPP', 'ACN', 'PPA', 'CDC', 'JP', 'ANPP', 'LABOUR', 'CPP']

        for party in VALID_PARTIES:
            score = request.POST.get(party)

            if score is None:
                continue

            try:
                AnnouncedPUResult.objects.create(
                    polling_unit_uniqueid=int(pu_id),
                    party_abbreviation=str(party).strip().upper()[:10],
                    party_score=int(score),
                    entered_by_user="web",
                    date_entered=timezone.now(),
                    user_ip_address=(request.META.get('REMOTE_ADDR') or '0.0.0.0')[:50],
                )
            except (ValueError, TypeError):
                continue

    return render(request, 'elections/add_results.html', {
        'polling_units': polling_units
    })