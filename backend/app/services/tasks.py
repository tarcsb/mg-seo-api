from apscheduler.schedulers.background import BackgroundScheduler
from services import perform_seo_analysis
from models import SEOReport, User
import smtplib

scheduler = BackgroundScheduler()

# Periodic SEO Check
def check_seo_ranking():
    reports = SEOReport.query.all()
    for report in reports:
        new_results = perform_seo_analysis(report.url)
        if new_results['ranking'] != report.analysis_results['ranking']:
            send_alert_email(report.owner.email, report.url, new_results['ranking'])
        report.analysis_results = new_results
        db.session.commit()

# Send email alerts
def send_alert_email(user_email, url, new_ranking):
    with smtplib.SMTP('smtp.mailtrap.io', 2525) as server:
        server.login("username", "password")
        message = f'Subject: SEO Ranking Alert\n\nThe ranking for {url} has changed to {new_ranking}.'
        server.sendmail("noreply@seoapp.com", user_email, message)

# Schedule the task to run every day
scheduler.add_job(check_seo_ranking, 'interval', days=1)
scheduler.start()
