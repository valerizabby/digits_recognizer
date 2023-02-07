# Распознавание цифр

Модель распознавания цифр, обученная на датасете [Mnist](https://www.tensorflow.org/datasets/catalog/mnist?hl=ru "ссылка на тф мниста"), обернутая в телеграм бота. В работе обучаются и сравниваются [LeNet](https://arxiv.org/pdf/2301.04275.pdf "Статья ленет"), и моя сеть, реализованы на TensorFlow, обучены на GPU в GoogleColab. Процесс обучения логируется и представлен в TensorBoard.

## Датасет 
В работе используется известный датасет [Mnist](https://www.tensorflow.org/datasets/catalog/mnist?hl=ru "ссылка на тф мниста"), состоящий из 70000 фотографий рукописных цифр 28 $\times$ 28 пикселей. Картинки имеют вид: 

![Image alt](https://github.com/valerizabby/digits_recognizer/blob/main/pictures/exmp.png?raw=true)

## Препроцессинг 
Применяем padding с $pad = 2$, делим датасет в отношении 6 к 1 на тренировочную и тестовую выборку соответственно. Из тренировочной берем 2000 экземляров на валидацию. 

## Модели
Рассмотрены и обучены две модели, их архитектуры представим с помощью [Netron](https://netron.app/). Интересно, что LeNet впервые была предствлена в [статье](https://arxiv.org/pdf/2301.04275.pdf "Статья ленет") 1998 года и тогда скорее использовали tanh и sigmoid активации (сейчас ReLu и Leaky Relu), а так же AveragePooling, а не MaxPooling.

My model            |  LeNet
:-------------------------------------:|:-------------------------------------:
![model_arch](https://github.com/valerizabby/digits_recognizer/blob/main/pictures/model40_32.jpg)  |  ![lenet_arch](https://github.com/valerizabby/digits_recognizer/blob/main/pictures/lenet.jpg)


## Обучение и результаты 
В GoogleColab на датасете Mnist обучены 2 модели: по 10 и 40 эпох. Accuracy посчитан на тестовой выборке. 

| Модель        | # эпох             | Accuracy (%) |
| ------------- |:------------------:| :-----------:|
| MyModel10     | 10                 |  99,25       |
| MyModel40     | 40                 |  99,24       |
| LeNet10       | 10                 |  97,17       |
| LeNet40       | 40                 |  97,53       |

My model            |  LeNet
:-------------------------------------:|:-------------------------------------:
![model acc](https://github.com/valerizabby/digits_recognizer/blob/main/pictures/mymodelacc.png)  |  ![lenet_arch](https://github.com/valerizabby/digits_recognizer/blob/main/pictures/lenetacc.png)


## TensorBoard
Подробнее процесс обучения можно рассмотреть в TensorBoard для [LeNet](https://tensorboard.dev/experiment/XBoQEzU8RXGX6AvHZ7zNYQ/#scalars) и [MyModel](https://tensorboard.dev/experiment/l3VbehpyRq6ySerHqZXlSg/#scalars&run=20230207-091753%2Ftrain). Перейти можно по гиперссылкам или: 
My model            |  LeNet
:-------------------------------------:|:-------------------------------------:
![model qr](http://qrcoder.ru/code/?https%3A%2F%2Ftensorboard.dev%2Fexperiment%2Fl3VbehpyRq6ySerHqZXlSg%2F%23scalars%26run%3D20230207-091753%252Ftrain&4&0)  |  ![lenet qr](http://qrcoder.ru/code/?https%3A%2F%2Ftensorboard.dev%2Fexperiment%2FXBoQEzU8RXGX6AvHZ7zNYQ%2F%23scalars&4&0)
## Телеграм-бот
В качестве Api будем использовать [Telegram-бота](https://t.me/digits_recognizer_bot). Имеет небольшой функционал, главная цель которого - принимать и обрабатывать запрос в виде картинки с цифрой. Так как модели обучались на *очень* хороших данных, то при тесте своих изображений (которые не всегда были с равномерным фоном или с хорошо масштабированной цифрой) оказалось, что модели могут не очень хорошо отвечать. Пример работы: 
<p align="center">

  <img src="https://github.com/valerizabby/digits_recognizer/blob/main/pictures/exmp.jpg" height="400">

</p>
