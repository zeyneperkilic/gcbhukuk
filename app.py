from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = 'gcb_hukuk_secret_key_2024'

# E-posta konfigürasyonu
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Gmail kullanıyorsanız
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'info@gcbhukuk.com'
app.config['MAIL_PASSWORD'] = 'xugx rgva hhwv tpca'
app.config['MAIL_DEFAULT_SENDER'] = 'info@gcbhukuk.com'

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
            telefon = request.form.get('telefon')
            alan = request.form.get('alan')
            mesaj = request.form.get('mesaj')
            
            # E-posta içeriği oluştur
            subject = f"GCB Hukuk - Yeni İletişim Mesajı: {ad} {soyad}"
            body = f"""
            Yeni bir iletişim mesajı alındı:
            
            Ad Soyad: {ad} {soyad}
            E-posta: {email}
            Telefon: {telefon}
            Hukuki Alan: {alan}
            
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

@app.route('/yayinlar')
def yayinlar():
    return render_template('yayinlar.html')

@app.route('/yayin/<int:yayin_id>')
def yayin_detay(yayin_id):
    # Örnek veri, gerçek uygulamada veritabanından çekilebilir
    yayinlar = {
        1: {"baslik": "Bankacılık Hukuku Güncellemeleri", "tarih": "15 Ocak 2025", "icerik": "2025 yılında bankacılık sektöründe yapılan yasal değişiklikler ve bunların müvekkillerimiz üzerindeki etkileri hakkında detaylı analiz."},
        2: {"baslik": "Şirketler Hukukunda Yeni Düzenlemeler", "tarih": "10 Ocak 2025", "icerik": "Türk Ticaret Kanunu'nda yapılan değişiklikler ve şirket yönetiminde dikkat edilmesi gereken yeni hükümler."},
        3: {"baslik": "Sermaye Piyasaları Reforms", "tarih": "5 Ocak 2025", "icerik": "Sermaye piyasalarında yapılan reformlar ve yatırımcıları etkileyen yeni düzenlemeler hakkında kapsamlı değerlendirme."},
        4: {"baslik": "Gayrimenkul Hukuku Güncellemeleri", "tarih": "1 Ocak 2025", "icerik": "Gayrimenkul sektöründe yapılan yasal değişiklikler ve alıcı-satıcı hakları konusunda önemli güncellemeler."},
        5: {"baslik": "İş Hukuku Yeni Düzenlemeler", "tarih": "28 Aralık 2024", "icerik": "İş hukukunda yapılan değişiklikler ve işçi-işveren ilişkilerini etkileyen yeni hükümler hakkında detaylı analiz."},
        6: {"baslik": "Vergi Hukuku Güncellemeleri", "tarih": "25 Aralık 2024", "icerik": "Vergi mevzuatında yapılan değişiklikler ve mükellefleri etkileyen yeni düzenlemeler hakkında kapsamlı değerlendirme."},
    }
    yayin = yayinlar.get(yayin_id)
    if yayin:
        return render_template('yayin_detay.html', yayin=yayin)
    else:
        return render_template('404.html'), 404

@app.route('/gizlilik')
def gizlilik():
    return render_template('gizlilik.html')

@app.route('/kvkk')
def kvkk():
    return render_template('kvkk.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) 