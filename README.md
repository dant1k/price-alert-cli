![CI](https://github.com/dant1k/price-alert-cli/actions/workflows/ci.yml/badge.svg)

# price-alert-cli

CLI для отслеживания аномальных цен и объёмов по криптовалютам.

## Установка
```bash
git clone https://github.com/dant1k/price-alert-cli
cd price-alert-cli
pip install -e .
price-alert BTC

Пример: если цена упала на 5% — вы получите уведомление.

## Пример использования

```bash
$ price-alert BTC
⚡ Цена BTC изменилась на -5.3% за час

Если цена упадёт или вырастет на больше чем 5% за указанный период — вы получите уведомление.
