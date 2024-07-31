
# RabbitMQ: Mesaj Kuyruğu Sistemi

![RabbitMQ](https://upload.wikimedia.org/wikipedia/commons/7/71/RabbitMQ_logo.svg)

## 1. Giriş ve Temel Kavramlar
RabbitMQ, açık kaynaklı bir mesaj kuyruğu sistemidir. AMQP (Advanced Message Queuing Protocol) protokolünü kullanarak mesajları güvenli ve ölçeklenebilir bir şekilde iletir. RabbitMQ, mikro hizmetler, dağıtık sistemler ve gerçek zamanlı veri işleme gibi uygulamalarda yaygın olarak kullanılır.

## 2. RabbitMQ'nun Temel Bileşenleri

### a. Producer (Üretici):
- Mesajları oluşturan ve RabbitMQ'ya gönderen uygulama veya hizmettir.
- Mesajları belirli bir exchange'e gönderir.

### b. Consumer (Tüketici):
- Mesajları RabbitMQ'dan alan ve işleyen uygulama veya hizmettir.
- Mesajları belirli bir kuyruğa (queue) bağlanarak alır.

### c. Queue (Kuyruk):
- Mesajların saklandığı yerdir. Kuyruklar, tüketiciler tarafından mesajların alınmasını bekler.
- FIFO (First In First Out) prensibine göre çalışır, yani ilk giren mesaj ilk alınır.

### d. Exchange:
- Mesajların kuyruklara yönlendirildiği bileşendir.
- Farklı tipte exchange'ler vardır: direct, topic, headers, fanout.

### e. Binding:
- Exchange ile kuyruklar arasındaki ilişkiyi belirler. Hangi mesajların hangi kuyruklara yönlendirileceğini tanımlar.

### f. Virtual Host (vHost):
- RabbitMQ sunucusundaki mantıksal bölümlerdir. Her vHost, kendi kuyruk, exchange ve binding'lerine sahiptir.
- Farklı uygulamaları izole etmek için kullanılır.

### g. Connection ve Channel:
- **Connection**: Uygulama ve RabbitMQ arasında kurulan TCP bağlantısıdır.
- **Channel**: Bir connection üzerinde oluşturulan sanal bağlantılardır. Aynı connection üzerinde birden fazla channel açılabilir.

## 3. RabbitMQ'nun Mimarisi ve Çalışma Prensibi

### a. Mesaj Akışı:
1. Producer, bir mesajı exchange'e gönderir.
2. Exchange, binding kurallarına göre mesajı uygun kuyruğa yönlendirir.
3. Consumer, kuyruğa bağlanarak mesajı alır ve işler.

### b. Exchange Tipleri:
- **Direct Exchange**: Mesajları routing key ile eşleşen kuyruklara yönlendirir.
- **Topic Exchange**: Routing key'e göre mesajları joker karakterler (*, #) kullanarak yönlendirir.
- **Fanout Exchange**: Gelen tüm mesajları bağlı olan tüm kuyruklara gönderir.
- **Headers Exchange**: Mesaj başlıklarına göre yönlendirme yapar.

### c. RabbitMQ Yönetimi:
- RabbitMQ, web tabanlı bir yönetim paneli sunar. Bu panel üzerinden kuyruklar, exchange'ler ve binding'ler yönetilebilir.
- RabbitMQ Management Plugin ile [http://localhost:15672](http://localhost:15672) adresinden erişilebilir.

## 4. RabbitMQ Kullanım Senaryoları
- **İş Kuyruğu (Work Queue)**: İş yükünü birden fazla tüketiciye dağıtmak için kullanılır.
- **Yayın/Yayılma (Publish/Subscribe)**: Bir mesajın birden fazla tüketiciye iletilmesi gereken durumlarda kullanılır.
- **Yönlendirme (Routing)**: Mesajların belirli kriterlere göre belirli kuyruklara yönlendirilmesi.
- **İçerik Tabanlı Yönlendirme (Topic)**: Mesajların konu başlıklarına göre yönlendirilmesi.

## 5. RabbitMQ'nun Kurulumu ve Yapılandırması
Aşağıda, Docker Compose kullanarak RabbitMQ'nun nasıl kurulacağını ve Python ile producer ve consumer uygulamalarının nasıl oluşturulacağını göstereceğiz.
