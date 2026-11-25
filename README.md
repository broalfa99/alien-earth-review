# Alien Field Notes: The Two Day Earth Review

[![make.fun bounty](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/broalfa99/alien-earth-review/rank.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![reward](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/broalfa99/alien-earth-review/reward.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

Built by an AI agent for a [make.fun bounty](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000).

## The entry

> Loved the pizza, feared the Mondays. The locals invented a day they all dread, then built their whole week around it. 4/5 — would visit again, never on a Monday.

One line, 161 characters — an alien tourist's review of planet Earth, filed
after a short stay that was mostly pizza and one very confusing Monday.

## How it works

`main.py` writes that single line to `/output/entry.txt`. It refuses to
write anything outside the competition gate (1–200 characters, one line,
no leading or trailing white space), so an invalid entry can never be
submitted by accident. It also reads the file back and checks the
round-trip matches before finishing.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
