CREATE TABLE Orders (
    order_id Int32,
    user_id Int32,
    order_date DateTime,
    total_amount Decimal(18, 2),
    payment_status String
) ENGINE = S3('https://storage.yandexcloud.net/mentor-hw/Orders_data.csv', 'CSV');


CREATE TABLE OrderItems (
    item_id Int32,
    order_id Int32,
    product_name String,
    product_price Decimal(18, 2),
    quantity Int32
) ENGINE = S3('https://storage.yandexcloud.net/mentor-hw/OrderItems_data.csv', 'CSV');

