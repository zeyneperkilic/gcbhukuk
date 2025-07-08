from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = 'gcb_hukuk_secret_key_2024'

# E-posta konfigürasyonu
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Gmail kullanıyorsanız
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'  # Avukatın e-posta adresi
app.config['MAIL_PASSWORD'] = 'your_app_password'  # Gmail uygulama şifresi
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hakkinda')
def hakkinda():
    return render_template('hakkinda.html')

@app.route('/hizmetler')
def hizmetler():
    return render_template('hizmetler.html')

@app.route('/iletisim', methods=['GET', 'POST'])
def iletisim():
    if request.method == 'POST':
        try:
            # Form verilerini al
            ad = request.form.get('ad')
            soyad = request.form.get('soyad')
            email = request.form.get('email')
            mesaj = request.form.get('mesaj')
            
            # E-posta içeriği oluştur
            subject = f"GCB Hukuk - Yeni İletişim Mesajı: {ad} {soyad}"
            body = f"""
            Yeni bir iletişim mesajı alındı:
            
            Ad Soyad: {ad} {soyad}
            E-posta: {email}
            
            Mesaj:
            {mesaj}
            
            Bu mesaj GCB Hukuk web sitesinden gönderilmiştir.
            """
            
            # E-postayı gönder
            msg = Message(subject, recipients=['info@gcbhukuk.com'])
            msg.body = body
            mail.send(msg)
            
            flash('Mesajınız başarıyla gönderildi. En kısa sürede size dönüş yapacağız.', 'success')
            return redirect(url_for('iletisim'))
            
        except Exception as e:
            flash('Mesaj gönderilirken bir hata oluştu. Lütfen tekrar deneyin.', 'error')
            return redirect(url_for('iletisim'))
    
    return render_template('iletisim.html')

@app.route('/neden-biz')
def neden_biz():
    return render_template('neden_biz.html')

@app.route('/hemen-ara')
def hemen_ara():
    return render_template('hemen_ara.html')

@app.route('/giris')
def giris():
    return render_template('giris.html')

@app.route('/kayit')
def kayit():
    return render_template('kayit.html')

if __name__ == '__main__':
    app.run(debug=True) 