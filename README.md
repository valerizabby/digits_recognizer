# Распознавание цифр

Модель распознавания цифр, обученная на датасете [Mnist](https://www.tensorflow.org/datasets/catalog/mnist?hl=ru "ссылка на тф мниста"), обернутая в телеграм бота. В работе обучаются и сравниваются [LeNet](https://arxiv.org/pdf/2301.04275.pdf "Статья ленет"), [MobileNet](https://arxiv.org/pdf/1704.04861v1.pdf "мобайлнет") и моя сеть, реализованы на TensorFlow, обучены на GPU в GoogleColab. Процесс обучения логируется и представлен для читателя в TensorBoard 

## Датасет 
В работе используется известный датасет [Mnist](https://www.tensorflow.org/datasets/catalog/mnist?hl=ru "ссылка на тф мниста"), состоящий из 70000 фотографий рукописных цифр 28 $\times$ 28 пикселей. Картинки имеют вид: 

![Image alt](https://github.com/valerizabby/digits_recognizer/blob/main/pictures/exmp.png?raw=true)

Применим padding с $pad = 2$ и получим размерность датасета (70000, 32, 32, 1). 
