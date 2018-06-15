from icalendar import Calendar

def events_with_response(url, responses=['ACCEPTED', 'TENTATIVE']):
    """Get events only with certain responses
    """

    with open(url, 'rb') as f:
        cal = Calendar.from_ical(f.read())

    events = [e for e in cal.walk('vevent')]

    filtered = [e for e in events if e['PARTSTAT']]

