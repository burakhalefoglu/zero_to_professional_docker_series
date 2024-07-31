
# Apache Kafka: Dağıtık Streaming Platformu

Apache Kafka, yüksek performanslı, dağıtık bir streaming platformudur. Başlangıçta LinkedIn tarafından geliştirilmiş ve daha sonra Apache Software Foundation tarafından açık kaynaklı olarak yayınlanmıştır. Kafka, gerçek zamanlı veri akışı uygulamaları ve büyük veri işleme için yaygın olarak kullanılır.

## Temel Bileşenler ve Kavramlar

### Broker:
- Kafka broker'ları, Kafka kümesinin temel yapı taşlarıdır. Bir broker, gelen veri akışlarını alır, depolar ve talepler doğrultusunda tüketicilere sunar.
- Bir Kafka kümesi, birden fazla broker'dan oluşur.

### Zookeeper:
- Kafka, Zookeeper'ı dağıtık yapılandırma ve senkronizasyon yönetimi için kullanır.
- Zookeeper, Kafka broker'larının durumunu izler ve görev atamalarını yönetir.

### Topic:
- Kafka'da veri akışları "topic"ler olarak organize edilir. Bir topic, veri kayıtlarının kategorize edildiği yerlerdir.
- Topic'ler, daha fazla ölçeklenebilirlik ve hata toleransı için bölümlere (partition) ayrılır.

### Partition:
- Her topic, bir veya daha fazla partition'a bölünür.
- Partition'lar, verilerin paralel olarak işlenmesini ve yüksek verimlilik sağlar.
- Her partition, belirli bir sıra içinde mesajları saklar ve sıralı erişim sağlar.

### Producer:
- Producer'lar, Kafka'ya veri gönderen uygulamalardır.
- Veriler, belirli topic'lere gönderilir.

### Consumer:
- Consumer'lar, Kafka'dan veri çeken uygulamalardır.
- Consumer'lar, belirli topic'lerden veri okuyarak işleyebilirler.

### Consumer Group:
- Bir consumer group, aynı topic'ten veri tüketen bir veya daha fazla consumer'dan oluşur.
- Her consumer, bir veya daha fazla partition'dan veri çeker, bu da verilerin paralel olarak işlenmesini sağlar.

### Offset:
- Offset, bir partition'daki her bir mesajın benzersiz kimliğidir.
- Consumer'lar, belirli bir offset'ten başlayarak mesajları okuyabilirler.

## Kafka'nın Mimarisi ve Veri Akışı

### Veri Gönderme (Producer):
- Producer, bir topic'e veri gönderir. Mesajlar, topic'in partition'larına yazılır.
- Producer, mesajları doğrudan belirli bir partition'a yönlendirebilir veya Kafka'ya bırakabilir.

### Veri Depolama (Broker):
- Kafka broker'ları, mesajları disk üzerinde saklar.
- Partition'lar, her bir broker'da saklanabilir ve yedeklenebilir.

### Veri Tüketme (Consumer):
- Consumer'lar, belirli bir topic'ten ve partition'dan mesajları okur.
- Her consumer, bir consumer group'un parçası olabilir ve bu sayede veriler paralel olarak işlenir.

### Yedeklilik ve Hata Toleransı:
- Kafka, partition'ları yedekleyerek veri kaybını önler.
- Her partition'ın bir lideri ve yedekleri vardır. Lider partition, okuma ve yazma işlemlerini yönetir.

## Kafka'nın Kullanım Alanları

### Gerçek Zamanlı Veri İşleme:
- Gerçek zamanlı veri akışı uygulamaları için idealdir. Örneğin, gerçek zamanlı analiz, işlem izleme ve olay işleme.

### Mesajlaşma Sistemi:
- Uygulamalar arası mesajlaşma ve entegrasyon için kullanılır. Mikro hizmet mimarilerinde yaygın olarak kullanılır.

### Veri Akışı Boru Hatları (Data Pipelines):
- Büyük veri işleme ve ETL (Extract, Transform, Load) süreçleri için veri akış boru hatları oluşturur.

### Log Toplama ve İzleme:
- Log verilerinin toplanması ve analiz edilmesi için kullanılır.

## Kafka'nın Avantajları

### Yüksek Performans ve Ölçeklenebilirlik:
- Kafka, büyük veri akışlarını yüksek verimlilikle işleyebilir ve kolayca ölçeklendirilebilir.

### Dağıtık ve Hata Toleransı:
- Dağıtık mimarisi sayesinde yüksek erişilebilirlik ve hata toleransı sağlar.

### Gerçek Zamanlı İşleme:
- Gerçek zamanlı veri işleme ve analiz imkanı sunar.

### Esneklik:
- Farklı veri kaynaklarından veri alabilir ve farklı veri hedeflerine veri gönderebilir.
