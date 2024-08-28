# API Test Automation Project

Bu proje, kullanıcı kimlik doğrulama, gönderi yönetimi ve iade işlemlerini içeren bir sistem için otomatikleştirilmiş API testleri içerir. Testler, `pytest` ve `requests` kullanılarak Python'da yazılmıştır ve giriş yapma, sipariş tamamlama, iadeleri ele alma gibi senaryoları içerir.

## Proje Yapısı

- **config.py**: API URL'leri, kimlik bilgileri ve rapor dosyasının yolu gibi yapılandırma ayarlarını içerir.
- **conftest.py**: Testler için fixture'lar ve genel kurulum/teardown mantığını tanımlar, rapor başlatma dahil.
- **test_successful_login.py**: Başarılı bir giriş senaryosu için testi içerir.
- **test_wrong_password_login.py**: Yanlış şifre ile giriş testi içerir.
- **test_empty_username_login.py**: Boş kullanıcı adı ile giriş testi içerir.
- **test_empty_password_login.py**: Boş şifre ile giriş testi içerir.
- **test_empty_username_password_login.py**: Hem kullanıcı adı hem de şifrenin boş olduğu durumda giriş testi içerir.
- **test_complete_order.py**: Siparişi tamamlama testi içerir.
- **test_take_in_possession.py**: Bir öğeyi teslim alma senaryosunu içerir.
- **deliver_with_new_otp.py**: Yeni bir OTP ile teslimat testi içerir.
- **test_return.py**: İade senaryolarını ele alma testi içerir.
- **test_.py**: Tüm test senaryolarını bir araya getiren ve `report.html` dosyasını oluşturan ana test yürütücü.

## Gereksinimler

- Python 3.9+
- `pip` (Python paket yöneticisi)

### Python Paketleri

- `requests`: HTTP istekleri yapmak için.
- `pytest`: Testleri çalıştırmak için.
- `pytest-html`: HTML test raporları oluşturmak için.
- `pytest-order`: Test yürütme sırasını belirlemek için.

## Kurulum

1. **Depoyu Klonlayın**:

   ```bash
   git clone https://github.com/ugurakyay/Easy_Point_Test

   

2. **Sanal Ortam Oluştur**:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate


3. **Gerekli Paketler**:

   ```bash
 
   pip install -r requirements.txt

### Test Senaryoları
Proje aşağıdaki senaryoları kapsamaktadır:

Başarılı Giriş: Geçerli kimlik bilgileriyle başarılı bir giriş testi.

Yanlış Şifre ile Giriş: Yanlış şifre ile giriş testi.

Boş Kullanıcı Adı ile Giriş: Kullanıcı adı alanı boşken giriş testi.

Boş Şifre ile Giriş: Şifre alanı boşken giriş testi.

Hem Kullanıcı Adı Hem de Şifre Boşken Giriş: Her iki alanın da boş olduğu durumdaki giriş testi.

Siparişi Tamamlama: Giriş yapar, gönderileri alır ve belirli bir gönderi kimliği ve OTP kullanarak bir siparişi tamamlar.

Teslim Alma: Bir öğeyi teslim alma senaryosunu simüle eder.

Yeni OTP ile Teslimat: Yeni oluşturulan bir OTP ile teslimat sürecini test eder.

İade İşlemi: Giriş yapar, bir gönderiyi iade durumuyla alır ve iade işlemini tamamlar.

### Testlerin Çalıştırılması

**Testleri çalıştırmak**:

   ```bash
   pytest
   
   pytest -k test_successful_login

