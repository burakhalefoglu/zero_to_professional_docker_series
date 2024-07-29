
# Kibana Query Language (KQL) Kullanımı

Kibana Query Language (KQL), Kibana'da Elasticsearch verilerini sorgulamak için kullanılan bir sorgulama dilidir. KQL, basit ve sezgisel bir sözdizimi sunar, bu da kullanıcıların verileri filtrelemelerini ve analiz etmelerini kolaylaştırır.

## Temel KQL Sözdizimi

### Basit Sorgular

Bir alanın belirli bir değere sahip olup olmadığını kontrol etmek için basit sorgular kullanabilirsiniz.

\`\`\`kql
status:200
\`\`\`
Bu sorgu, \`status\` alanı \`200\` olan tüm belgeleri getirir.

### Çoklu Koşullar

Birden fazla koşulu \`AND\` veya \`OR\` operatörleriyle birleştirebilirsiniz.

\`\`\`kql
status:200 AND extension:"jpg"
\`\`\`
Bu sorgu, \`status\` alanı \`200\` ve \`extension\` alanı \`"jpg"\` olan tüm belgeleri getirir.

\`\`\`kql
status:200 OR status:404
\`\`\`
Bu sorgu, \`status\` alanı \`200\` veya \`404\` olan tüm belgeleri getirir.

### Parantez Kullanımı

Koşulları gruplayarak daha karmaşık sorgular oluşturabilirsiniz.

\`\`\`kql
(status:200 OR status:404) AND extension:"jpg"
\`\`\`
Bu sorgu, \`status\` alanı \`200\` veya \`404\` olan ve \`extension\` alanı \`"jpg"\` olan tüm belgeleri getirir.

### Joker Karakterler

Joker karakterler (\`*\` ve \`?\`) kullanarak kısmi eşleşmeler yapabilirsiniz.

\`\`\`kql
extension:jp*
\`\`\`
Bu sorgu, \`extension\` alanı \`jp\` ile başlayan (\`jpg\`, \`jpeg\`, vb.) tüm belgeleri getirir.

\`\`\`kql
extension:jp?g
\`\`\`
Bu sorgu, \`extension\` alanı \`jpg\` veya \`jpeg\` gibi \`jp\` ile başlayıp, \`g\` ile biten tüm belgeleri getirir.

### Negasyon

Bir koşulun olmamasını belirlemek için \`NOT\` operatörünü kullanabilirsiniz.

\`\`\`kql
NOT status:404
\`\`\`
Bu sorgu, \`status\` alanı \`404\` olmayan tüm belgeleri getirir.

### Alan Varlığı Kontrolü

Bir alanın var olup olmadığını kontrol edebilirsiniz.

\`\`\`kql
status:*
\`\`\`
Bu sorgu, \`status\` alanı mevcut olan tüm belgeleri getirir.

\`\`\`kql
NOT status:*
\`\`\`
Bu sorgu, \`status\` alanı olmayan tüm belgeleri getirir.

### Aralık Sorguları

Sayılar ve tarihler için aralık sorguları yapabilirsiniz.

\`\`\`kql
bytes > 1000
\`\`\`
Bu sorgu, \`bytes\` alanı 1000'den büyük olan tüm belgeleri getirir.

\`\`\`kql
bytes >= 1000 AND bytes <= 2000
\`\`\`
Bu sorgu, \`bytes\` alanı 1000 ile 2000 arasında olan tüm belgeleri getirir.

\`\`\`kql
timestamp >= "2021-01-01" AND timestamp < "2022-01-01"
\`\`\`
Bu sorgu, \`timestamp\` alanı 1 Ocak 2021 ile 1 Ocak 2022 arasında olan tüm belgeleri getirir.

## KQL Kullanımı Örnekleri

### Örnek 1: Belirli Bir IP Adresini Sorgulama

\`\`\`kql
clientip:"192.168.1.1"
\`\`\`
Bu sorgu, \`clientip\` alanı \`192.168.1.1\` olan tüm belgeleri getirir.

### Örnek 2: Belirli Bir URL'yi İçeren Sorgu

\`\`\`kql
url.path:"/home"
\`\`\`
Bu sorgu, \`url.path\` alanı \`/home\` olan tüm belgeleri getirir.

### Örnek 3: Hata Durum Kodlarını Sorgulama

\`\`\`kql
status:(400 OR 401 OR 403 OR 404 OR 500)
\`\`\`
Bu sorgu, \`status\` alanı 400, 401, 403, 404 veya 500 olan tüm belgeleri getirir.

### Örnek 4: Belirli Bir Zaman Aralığını Sorgulama

\`\`\`kql
@timestamp >= "2022-01-01T00:00:00" AND @timestamp < "2023-01-01T00:00:00"
\`\`\`
Bu sorgu, \`@timestamp\` alanı 1 Ocak 2022 ile 1 Ocak 2023 arasında olan tüm belgeleri getirir.

Bu dokümantasyon, KQL'nin temel kullanımını ve sorgulama tekniklerini açıklamaktadır. Daha fazla bilgi için Elasticsearch ve Kibana'nın resmi dokümantasyonlarına başvurabilirsiniz.
