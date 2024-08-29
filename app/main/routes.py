from flask import Blueprint, request, render_template, flash, url_for, flash, redirect, session
from flask_login import login_required, current_user
from flask_mail import Message

from app import db, mail
from app.forms import ContactForm, ContactusForm, ClientinfoForm
from app import mail
from app.models import Post, User

main = Blueprint('main', __name__)


@main.route("/", methods=['GET', 'POST'])
def home():
    user = User
    form = ContactusForm()
    if form.validate_on_submit():
        msg = Message(f'New Message from {user.email}', sender=f'{user.email}',
                      recipients=['info@jswebtron.com'])
        msg.body = f"""
           Brand Name :  {form.brand_name.data}

           Email: {form.contactemail.data}
           
           Phone :  {form.phonenumber.data}
        
           Social Media Management : {form.management.data}
           
           Search Engine Optimization : {form.searchengine.data}
           
           Full Branding Packages : {form.branding.data}
           
           Website Development : {form.website.data}
           
           Digital Marketing : {form.digital.data}
           
           Graphic Designs : {form.graphic.data}
           
           Logo Creation : {form.logocreation.data}
           
           Video Creation : {form.videocreation.data}
           
           """
        mail.send(msg)
        flash('your message have been sent', 'success')
        return redirect(url_for('main.home'))
    return render_template("index.html", title='Contact Form', form=form)


@main.route('/blog', methods=['GET', 'POST'])
def blog():
    return render_template("blog.html")


@main.route("/about", methods=['GET', 'POST'])
def about():
    user = User
    form = ContactusForm()
    if form.validate_on_submit():
        msg = Message(f'New Message from {user.email}', sender=f'{user.email}',
                      recipients=['info@jswebtron.com'])
        msg.body = f"""
           Brand Name :  {form.brand_name.data}

           Email: {form.contactemail.data}
           
           Phone :  {form.phonenumber.data}
        
           Social Media Management : {form.management.data}
           
           Search Engine Optimization : {form.searchengine.data}
           
           Full Branding Packages : {form.branding.data}
           
           Website Development : {form.website.data}
           
           Digital Marketing : {form.digital.data}
           
           Graphic Designs : {form.graphic.data}
           
           Logo Creation : {form.logocreation.data}
           
           Video Creation : {form.videocreation.data}
           
           """
        mail.send(msg)
        flash('your message have been sent', 'success')
        return redirect(url_for('main.home'))
    return render_template('about.html', title='Contactus Form', form=form)



@main.route("/web", methods=['GET', 'POST'])
def web():
    user = User
    form = ContactusForm()
    if form.validate_on_submit():
        msg = Message(f'New Message from {user.email}', sender=f'{user.email}',
                      recipients=['info@jswebtron.com'])
        msg.body = f"""
           Brand Name :  {form.brand_name.data}

           Email: {form.contactemail.data}
           
           Phone :  {form.phonenumber.data}
        
           Social Media Management : {form.management.data}
           
           Search Engine Optimization : {form.searchengine.data}
           
           Full Branding Packages : {form.branding.data}
           
           Website Development : {form.website.data}
           
           Digital Marketing : {form.digital.data}
           
           Graphic Designs : {form.graphic.data}
           
           Logo Creation : {form.logocreation.data}
           
           Video Creation : {form.videocreation.data}

           
           """
        mail.send(msg)
        flash('your message have been sent', 'success')
        return redirect(url_for('main.home'))
    return render_template("web.html", title='Contactus Form', form=form)


@main.route("/app", methods=['GET', 'POST'])
def app():
    user = User
    form = ContactusForm()
    if form.validate_on_submit():
        msg = Message(f'New Message from {user.email}', sender=f'{user.email}',
                      recipients=['info@jswebtron.com'])
        msg.body = f"""
           Brand Name :  {form.brand_name.data}

           Email: {form.contactemail.data}
           
           Phone :  {form.phonenumber.data}
        
           Social Media Management : {form.management.data}
           
           Search Engine Optimization : {form.searchengine.data}
           
           Full Branding Packages : {form.branding.data}
           
           Website Development : {form.website.data}
           
           Digital Marketing : {form.digital.data}
           
           Graphic Designs : {form.graphic.data}
           
           Logo Creation : {form.logocreation.data}
           
           Video Creation : {form.videocreation.data}

           
           """
        mail.send(msg)
        flash('your message have been sent', 'success')
        return redirect(url_for('main.home'))
    return render_template("app.html", title='Contactus Form', form=form)


@main.route("/graphics", methods=['GET', 'POST'])
def graphics():
    user = User
    form = ContactusForm()
    if form.validate_on_submit():
        msg = Message(f'New Message from {user.email}', sender=f'{user.email}',
                      recipients=['info@jswebtron.com'])
        msg.body = f"""
          
          Brand Name :  {form.brand_name.data}

           Email: {form.contactemail.data}
           
           Phone :  {form.phonenumber.data}
        
           Social Media Management : {form.management.data}
           
           Search Engine Optimization : {form.searchengine.data}
           
           Full Branding Packages : {form.branding.data}
           
           Website Development : {form.website.data}
           
           Digital Marketing : {form.digital.data}
           
           Graphic Designs : {form.graphic.data}
           
           Logo Creation : {form.logocreation.data}
           
           Video Creation : {form.videocreation.data}
           
           """
        mail.send(msg)
        flash('your message have been sent', 'success')
        return redirect(url_for('main.home'))
    return render_template("graphics.html", title='Contactus Form', form=form)


@main.route("/ourwork", methods=['GET', 'POST'])
def ourwork():
    user = User
    form = ContactusForm()
    if form.validate_on_submit():
        msg = Message(f'New Message from {user.email}', sender=f'{user.email}',
                      recipients=['info@jswebtron.com'])
        msg.body = f"""
          
          Brand Name :  {form.brand_name.data}

           Email: {form.contactemail.data}
           
           Phone :  {form.phonenumber.data}
        
           Social Media Management : {form.management.data}
           
           Search Engine Optimization : {form.searchengine.data}
           
           Full Branding Packages : {form.branding.data}
           
           Website Development : {form.website.data}
           
           Digital Marketing : {form.digital.data}
           
           Graphic Designs : {form.graphic.data}
           
           Logo Creation : {form.logocreation.data}
           
           Video Creation : {form.videocreation.data}
           
           """
        mail.send(msg)
        flash('your message have been sent', 'success')
        return redirect(url_for('main.home'))
    return render_template("ourwork.html", title='Contactus Form', form=form)


@main.route("/socialmediamanagement", methods=['GET', 'POST'])
def socialmediamanagement():
    user = User
    form = ContactusForm()
    if form.validate_on_submit():
        msg = Message(f'New Message from {user.email}', sender=f'{user.email}',
                      recipients=['info@jswebtron.com'])
        msg.body = f"""
        
          Brand Name :  {form.brand_name.data}

           Email: {form.contactemail.data}
           
           Phone :  {form.phonenumber.data}
        
           Social Media Management : {form.management.data}
           
           Search Engine Optimization : {form.searchengine.data}
           
           Full Branding Packages : {form.branding.data}
           
           Website Development : {form.website.data}
           
           Digital Marketing : {form.digital.data}
           
           Graphic Designs : {form.graphic.data}
           
           Logo Creation : {form.logocreation.data}
           
           Video Creation : {form.videocreation.data}
           
           """
        mail.send(msg)
        flash('your message have been sent', 'success')
        return redirect(url_for('main.home'))
    return render_template("socialmediamanagement.html", title='Contactus Form', form=form)


@main.route("/video_ad", methods=['GET', 'POST'])
def video_ad():
    user = User
    form = ContactusForm()
    if form.validate_on_submit():
        msg = Message(f'New Message from {user.email}', sender=f'{user.email}',
                      recipients=['info@jswebtron.com'])
        msg.body = f"""
        
          Brand Name :  {form.brand_name.data}

           Email: {form.contactemail.data}
           
           Phone :  {form.phonenumber.data}
        
           Social Media Management : {form.management.data}
           
           Search Engine Optimization : {form.searchengine.data}
           
           Full Branding Packages : {form.branding.data}
           
           Website Development : {form.website.data}
           
           Digital Marketing : {form.digital.data}
           
           Graphic Designs : {form.graphic.data}
           
           Logo Creation : {form.logocreation.data}
           
           Video Creation : {form.videocreation.data}     
                 
           """
        mail.send(msg)
        flash('your message have been sent', 'success')
        return redirect(url_for('main.home'))
    return render_template("video-ad.html", title='Contactus Form', form=form)


@main.route("/rightcolor", methods=['GET', 'POST'])
def rightcolor():
    user = User
    form = ContactusForm()
    if form.validate_on_submit():
        msg = Message(f'New Message from {user.email}', sender=f'{user.email}',
                      recipients=['info@jswebtron.com'])
        msg.body = f"""
          
          Brand Name :  {form.brand_name.data}

           Email: {form.contactemail.data}
           
           Phone :  {form.phonenumber.data}
        
           Social Media Management : {form.management.data}
           
           Search Engine Optimization : {form.searchengine.data}
           
           Full Branding Packages : {form.branding.data}
           
           Website Development : {form.website.data}
           
           Digital Marketing : {form.digital.data}
           
           Graphic Designs : {form.graphic.data}
           
           Logo Creation : {form.logocreation.data}
           
           Video Creation : {form.videocreation.data}
           
           """
        mail.send(msg)
        flash('your message have been sent', 'success')
        return redirect(url_for('main.home'))
    return render_template("rightcolor.html", title='Contactus Form', form=form)


@main.route("/things_to_avoid", methods=['GET', 'POST'])
def things_to_avoid():
    user = User
    form = ContactusForm()
    if form.validate_on_submit():
        msg = Message(f'New Message from {user.email}', sender=f'{user.email}',
                      recipients=['info@jswebtron.com'])
        msg.body = f"""
          
          Brand Name :  {form.brand_name.data}

           Email: {form.contactemail.data}
           
           Phone :  {form.phonenumber.data}
        
           Social Media Management : {form.management.data}
           
           Search Engine Optimization : {form.searchengine.data}
           
           Full Branding Packages : {form.branding.data}
           
           Website Development : {form.website.data}
           
           Digital Marketing : {form.digital.data}
           
           Graphic Designs : {form.graphic.data}
           
           Logo Creation : {form.logocreation.data}
           
           Video Creation : {form.videocreation.data}
           
           """
        mail.send(msg)
        flash('your message have been sent', 'success')
        return redirect(url_for('main.home'))
    return render_template("5-things-to-avoid.html", title='Contactus Form', form=form)


@main.route("/clientinfo", methods=['GET', 'POST'])
def clientinfo():
    user = User
    form = ClientinfoForm()
    if form.validate_on_submit():
        msg = Message(f'New Message from {user.email}', sender=f'{user.email}',
                      recipients=['info@jswebtron.com'])
        msg.body = f"""
          
          Client Name :  {form.name.data}

           Email: {form.email.data}
           
           Phone :  {form.phone.data}
        
           Company's Name : {form.companyname.data}
           
           Company address  : {form.companyaddress.data}
           
           Address Line 1 : {form.addressline.data}
           
           city : {form.city.data}
           
           What are your products or services? : {form.products.data}
           
           Who is your target audience? : {form.target.data}
           
           Describe your brand in as much detail as possible : {form.describe.data}
           
           What do you hope to achieve by working with us? : {form.achieve.data}
           
           Brand colors : {form.brandcolor.data}
           
           Do you have a tagline or slogan? : {form.slogan.data}
           
           How can customers contact you? : {form.cos_contact.data}
           
           Social media : {form.socialmedia.data}
           
           """
        mail.send(msg)
        flash('your message have been sent', 'success')
        return redirect(url_for('main.clientinfo'))
    return render_template("clientinfo.html", title='Contactus Form', form=form)


@main.route("/digital_marketing", methods=['GET', 'POST'])
def digital_marketing():
    user = User
    form = ContactusForm()
    if form.validate_on_submit():
        msg = Message(f'New Message from {user.email}', sender=f'{user.email}',
                      recipients=['info@jswebtron.com'])
        msg.body = f"""
          
          Brand Name :  {form.brand_name.data}

           Email: {form.contactemail.data}
           
           Phone :  {form.phonenumber.data}
        
           Social Media Management : {form.management.data}
           
           Search Engine Optimization : {form.searchengine.data}
           
           Full Branding Packages : {form.branding.data}
           
           Website Development : {form.website.data}
           
           Digital Marketing : {form.digital.data}
           
           Graphic Designs : {form.graphic.data}
           
           Logo Creation : {form.logocreation.data}
           
           Video Creation : {form.videocreation.data}
           
           """
        mail.send(msg)
        flash('your message have been sent', 'success')
        return redirect(url_for('main.home'))
    return render_template("digital-marketing.html", title='Contactus Form', form=form)


@main.route("/all_in_one", methods=['GET', 'POST'])
def all_in_one():
    user = User
    form = ContactusForm()
    if form.validate_on_submit():
        msg = Message(f'New Message from {user.email}', sender=f'{user.email}',
                      recipients=['info@jswebtron.com'])
        msg.body = f"""
         
         Brand Name :  {form.brand_name.data}

           Email: {form.contactemail.data}
           
           Phone :  {form.phonenumber.data}
        
           Social Media Management : {form.management.data}
           
           Search Engine Optimization : {form.searchengine.data}
           
           Full Branding Packages : {form.branding.data}
           
           Website Development : {form.website.data}
           
           Digital Marketing : {form.digital.data}
           
           Graphic Designs : {form.graphic.data}
           
           Logo Creation : {form.logocreation.data}
           
           Video Creation : {form.videocreation.data}
           
           """
        mail.send(msg)
        flash('your message have been sent', 'success')
        return redirect(url_for('main.home'))
    return render_template("all-in-one.html", title='Contactus Form', form=form)


@main.route("/terms", methods=['GET', 'POST'])
def terms():
    user = User
    form = ContactusForm()
    if form.validate_on_submit():
        msg = Message(f'New Message from {user.email}', sender=f'{user.email}',
                      recipients=['info@jswebtron.com'])
        msg.body = f"""
          
           Brand Name :  {form.brand_name.data}

           Email: {form.contactemail.data}
           
           Phone :  {form.phonenumber.data}
        
           Social Media Management : {form.management.data}
           
           Search Engine Optimization : {form.searchengine.data}
           
           Full Branding Packages : {form.branding.data}
           
           Website Development : {form.website.data}
           
           Digital Marketing : {form.digital.data}
           
           Graphic Designs : {form.graphic.data}
           
           Logo Creation : {form.logocreation.data}
           
           Video Creation : {form.videocreation.data}
           
           """
        mail.send(msg)
        flash('your message have been sent', 'success')
        return redirect(url_for('main.home'))
    return render_template("terms-of-use.html", title='Contactus Form', form=form)


@main.route("/privacy", methods=['GET', 'POST'])
def privacy():
    user = User
    form = ContactusForm()
    if form.validate_on_submit():
        msg = Message(f'New Message from {user.email}', sender=f'{user.email}',
                      recipients=['info@jswebtron.com'])
        msg.body = f"""
          
          Brand Name :  {form.brand_name.data}

           Email: {form.contactemail.data}
           
           Phone :  {form.phonenumber.data}
        
           Social Media Management : {form.management.data}
           
           Search Engine Optimization : {form.searchengine.data}
           
           Full Branding Packages : {form.branding.data}
           
           Website Development : {form.website.data}
           
           Digital Marketing : {form.digital.data}
           
           Graphic Designs : {form.graphic.data}
           
           Logo Creation : {form.logocreation.data}
           
           Video Creation : {form.videocreation.data}
           
           """
        mail.send(msg)
        flash('your message have been sent', 'success')
        return redirect(url_for('main.home'))
    return render_template("privacy-policy.html", title='Contactus Form', form=form)


@main.route("/bestlogo", methods=['GET', 'POST'])
def bestlogo():
    user = User
    form = ContactusForm()
    if form.validate_on_submit():
        msg = Message(f'New Message from {user.email}', sender=f'{user.email}',
                      recipients=['info@jswebtron.com'])
        msg.body = f"""
           Brand Name :  {form.brand_name.data}

           Email: {form.contactemail.data}
           
           Phone :  {form.phonenumber.data}
        
           Social Media Management : {form.management.data}
           
           Search Engine Optimization : {form.searchengine.data}
           
           Full Branding Packages : {form.branding.data}
           
           Website Development : {form.website.data}
           
           Digital Marketing : {form.digital.data}
           
           Graphic Designs : {form.graphic.data}
           
           Logo Creation : {form.logocreation.data}
           
           Video Creation : {form.videocreation.data}
           
           """
        mail.send(msg)
        flash('your message have been sent', 'success')
        return redirect(url_for('main.home'))
    return render_template("bestlogo.html", title='Contactus Form', form=form)


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    user = User
    form = ContactForm()
    if form.validate_on_submit():
        msg = Message(f'New Message from {user.email}', sender=f'{user.email}',
                      recipients=['info@jswebtron.com'])
        msg.body = f"""
           Name :  {form.name.data}

           Email :  {form.contact_email.data}
           
           Phone :  {form.contact_phone.data}

           Brand Name :  {form.brand_name.data}

           Message :  {form.message.data}
           """
        mail.send(msg)
        flash('your message have been sent', 'success')
        return redirect(url_for('main.home'))
    return render_template('contact.html', title='contact Form', form=form)


