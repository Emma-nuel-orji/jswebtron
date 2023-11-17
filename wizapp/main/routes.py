from flask import Blueprint, request, render_template, flash, url_for, flash, redirect, session
from flask_login import login_required, current_user
from flask_mail import Message

from wizapp import db, mail
from wizapp.forms import ContactForm
from wizapp import mail
from wizapp.models import Post, User

main = Blueprint('main', __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route('/blog')
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=8)
    return render_template("blog.html", posts=posts)


@main.route("/about")
def about():
    return render_template("about.html")


@main.route("/web")
def web():
    return render_template("web.html")


@main.route("/graphics")
def graphics():
    return render_template("graphics.html")


@main.route("/ourwork")
def ourwork():
    return render_template("ourwork.html")


@main.route("/socialmediamanagement")
def socialmediamanagement():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(categories="SPORTS").order_by(Post.date_posted.desc()).paginate(page=page, per_page=8)
    return render_template("socialmediamanagement.html", posts=posts)


@main.route("/video_ad")
def video_ad():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(categories="LIFESTYLE").order_by(Post.date_posted.desc()).paginate(page=page,
                                                                                                    per_page=8)
    return render_template("video-ad.html", posts=posts)


@main.route("/rightcolor")
def rightcolor():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(categories="ENTERTAINMENT").order_by(Post.date_posted.desc()).paginate(page=page,
                                                                                                        per_page=8)
    return render_template("rightcolor.html", posts=posts)


@main.route("/things_to_avoid")
def things_to_avoid():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(categories="RELATIONSHIP").order_by(Post.date_posted.desc()).paginate(page=page,
                                                                                                       per_page=8)
    return render_template("5-things-to-avoid.html", posts=posts)

@main.route("/clientinfo")
def clientinfo():
    return render_template("clientinfo.html")


@main.route("/digital_marketing")
def digital_marketing():
    return render_template("digital-marketing.html")


@main.route("/all_in_one")
def all_in_one():
    return render_template("all-in-one.html")


@main.route("/terms")
def terms():
    return render_template("terms-of-use.html")


@main.route("/privacy")
def privacy():
    return render_template("privacy-policy.html")


@main.route("/bestlogo")
def bestlogo():
    return render_template("bestlogo.html")


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    user = User
    form = ContactForm()
    if form.validate_on_submit():
        msg = Message(f'New Message from {user.email}', sender=f'{user.email}',
                      recipients=['eorji452@gmail.com'])
        msg.body = f"""
           Name :  {form.name.data}

           Email :  {form.contact_email.data}
           
           Phone :  {form.contact_phone.data}

           Brand Name :  {form.subject.data}

           Message :  {form.message.data}
           """
        mail.send(msg)
        flash('your message have been sent', 'success')
        return redirect(url_for('main.home'))
    return render_template('contact.html', title='contact Form', form=form)
